#!/usr/bin/env python3
"""Copy the knowledge base into this site, leaving out private pages.

The knowledge base the agents use stays the source; never edit this repository
by hand. Each run rebuilds the site from the source:

  - private material is left out, in three ways:
      * pages and folders listed in EXCLUDE (the deny list);
      * a page whose front matter says "private: true", together with the
        folder of the same name (its sub-pages and images);
      * any text between <private> and </private>, on one line or many;
    and any line that links to a page left out is removed. A file that is
    not a page (an image, a PDF) is left out when only private text uses it.
    A <private> tag that is not closed, or a stray </private>, stops the run
    before anything is changed;
  - CLAUDE.md, AGENTS.md and hidden files (names starting with a dot) are
    never published;
  - file and folder names are cleaned for the web: Notion's 32-character ids
    are dropped and names become lower-case with dashes, so
    "Investment/Road to 1m 34ef...52.md" becomes "investment/road-to-1m.md";
  - every link between pages is rewritten to the new names;
  - the home page (knowledge-base.md) becomes index.md;
  - inline formulas written $...$ become $$...$$, the form the site renders
    (MathJax, loaded in _includes/head-custom.html, draws them);
  - collapsible <details> blocks get markdown="1", so the tables and lists
    inside them are rendered instead of shown as plain text;
  - a backslash at the end of a line becomes a line break, and tables get
    the blank lines around them that the site needs to draw them.

GitHub Pages then turns each .md file into a web page.

Usage:
    python3 publish.py [SOURCE]          rebuild the site, show what changed
    python3 publish.py [SOURCE] --push   rebuild, commit and push to GitHub
SOURCE defaults to ~/openclaw-data/main/knowledgeBase.
"""

import datetime
import os
import re
import shutil
import subprocess
import sys
from urllib.parse import quote, unquote

DEFAULT_SOURCE = "~/openclaw-data/main/knowledgeBase"
SITE = os.path.dirname(os.path.abspath(__file__))

# Never published. Each entry is a path inside the source, without the .md;
# it matches the page and the folder of the same name.
EXCLUDE = [
    "finance-knowledge/investment/trade-log",
    "finance-knowledge/investment/compliances",
]

# Files of this repository that a rebuild leaves alone.
KEEP = {".git", ".gitignore", "_config.yml", "_includes", "README.md", "CLAUDE.md", "publish.py"}

# Instructions for the agents that work in the source; never published.
AGENT_FILES = {"CLAUDE.md", "CLAUDE.local.md", "AGENTS.md"}

# Web paths of the pages whose front matter says "private: true"; plan() fills it.
flagged = set()

# The private markers. A passage is "<private>" ... "</private>"; the body may
# not contain another private tag, so a passage always ends at its own tag.
PRIVATE_PASSAGE = r"<private\s*>(?:(?!</?private\b).)*</private\s*>"
PRIVATE_LINES = re.compile(rf"^[ \t]*{PRIVATE_PASSAGE}[ \t]*(?:\n|\Z)", re.I | re.S | re.M)
PRIVATE_SPAN = re.compile(PRIVATE_PASSAGE, re.I | re.S)
PRIVATE_TAG = re.compile(r"<(/?)private\b(\s*>)?", re.I)
# What is left of a line once its private text is gone: nothing, or only a
# list marker, a checkbox or a quote mark. Such a line is removed.
EMPTY_ITEM = re.compile(r"^[ \t>]*(?:[-*+]|\d+[.)])?[ \t]*(?:\[[ xX]\])?[ \t]*$")
FRONT_MATTER = re.compile(r"\A﻿?---[ \t]*\n(.*?)^---[ \t]*$", re.S | re.M)
PRIVATE_FLAG = re.compile(r"^[ \t]*private[ \t]*:[ \t]*(.*?)[ \t]*$", re.I | re.M)

HOME_PAGE = "knowledge-base.md"
NOTION_ID = re.compile(r"\s+[0-9a-f]{32}$")
LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)")
DETAILS = re.compile(r"<details(?![^>]*markdown=)([^>]*)>")
# Inline TeX written $...$ (as Notion and github.com accept). The site's Markdown
# engine only knows $$...$$, so these are converted. To leave prices such as
# "$1,017 and $1,065" alone, the text must not start with a digit or space and
# must contain one of \ _ ^ {.
INLINE_MATH = re.compile(r"(?<![\w$\\])\$(?=[^\s\d$)])([^$\n]*?[\\_^{][^$\n]*?)(?<=\S)\$(?!\$)")
# A line ending in a single backslash is a line break on github.com and in
# Notion; the site's engine shows the backslash, so it becomes two spaces.
LINE_BREAK = re.compile(r"(?<!\\)\\[ \t]*$")


def is_table_row(line):
    return line.lstrip().startswith("|")


def strip_id(name):
    """'Road to 1m 34ef...52.md' -> 'Road to 1m.md'."""
    stem, ext = os.path.splitext(name)
    return NOTION_ID.sub("", stem) + ext


def slug(name):
    """A web-friendly name: 'Buy One Share of S&P 500' -> 'buy-one-share-of-s-and-p-500'."""
    stem, ext = os.path.splitext(strip_id(name))
    stem = re.sub(r"([a-z])([A-Z])", r"\1-\2", stem)        # camelCase -> camel-Case
    stem = stem.replace("&", " and ").lower()
    stem = re.sub(r"[^a-z0-9]+", "-", stem).strip("-")
    return stem + ext.lower()


def web_path(rel):
    """'Investment/Trade log 202f...a83.md' -> 'investment/trade-log'."""
    parts = rel.split("/")
    parts[-1] = os.path.splitext(parts[-1])[0]
    return "/".join(slug(p) for p in parts)


def why_excluded(rel):
    """Why a source path is not published, or None if it is.
    Names are compared in their web form, so 'Trade log 202f...md' and
    'trade-log.md' are both excluded."""
    parts = rel.split("/")
    if parts[-1] in AGENT_FILES or any(p.startswith(".") for p in parts):
        return "agent or hidden file"
    clean = web_path(rel)

    def covers(paths):
        return any(clean == p or clean.startswith(p + "/") for p in paths)

    if covers(map(web_path, EXCLUDE)):
        return "deny list"
    if covers(flagged):
        return "marked private"
    return None


def is_excluded(rel):
    return why_excluded(rel) is not None


def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def is_private_page(text):
    """True if the front matter at the top of a page says 'private: true'.
    Anything but false / no / off / 0 counts as true, so a typo hides the page."""
    front = FRONT_MATTER.match(text)
    flag = PRIVATE_FLAG.search(front.group(1)) if front else None
    return bool(flag) and flag.group(1).strip("'\"").lower() not in ("false", "no", "off", "0")


def strip_private(text, rel, problems):
    """Take out every <private>...</private> passage.
    Returns the text that is left and the passages taken out. Tags that do not
    pair up are added to problems; the caller must then publish nothing."""
    opened = None
    for tag in PRIVATE_TAG.finditer(text):
        line = text.count("\n", 0, tag.start()) + 1
        closing, well_formed = tag.group(1), tag.group(2)
        if not well_formed:
            problems.append(f"{rel}:{line}: write the tag as <private> or </private>, nothing else inside it")
        elif closing and opened is None:
            problems.append(f"{rel}:{line}: </private> without a <private> before it")
        elif closing:
            opened = None
        elif opened is not None:
            problems.append(f"{rel}:{line}: <private> inside the <private> opened on line {opened}")
        else:
            opened = line
    if opened is not None:
        problems.append(f"{rel}:{opened}: <private> is never closed")

    removed = []

    def take(match, leave=""):
        removed.append(match.group(0))
        return leave

    text = PRIVATE_LINES.sub(take, text)                   # passages that fill whole lines
    if PRIVATE_SPAN.search(text):                          # passages inside a line
        # Each one is first replaced by a mark, a character the page does not
        # use, so the line it was in can be tidied or, if now empty, removed.
        mark = next(c for c in map(chr, range(0xE000, 0xF900)) if c not in text)
        text = PRIVATE_SPAN.sub(lambda m: take(m, mark), text)
        lines = []
        for line in text.split("\n"):
            if mark in line:
                line = re.sub(rf"^{mark}[ \t]*", "", line)
                line = re.sub(rf"[ \t]*{mark}(?=[ \t,.;:!?)]|$)", "", line).replace(mark, "")
                if EMPTY_ITEM.match(line):
                    continue
            lines.append(line)
        text = "\n".join(lines)
    return text, removed


def resolve(href, rel):
    """The source path a link in page rel points at; None for a web link, an anchor or an absolute path."""
    if re.match(r"^[a-z][a-z0-9+.-]*:|^#|^/", href, re.I):
        return None
    path = href.partition("#")[0]
    return os.path.normpath(os.path.join(os.path.dirname(rel), unquote(path))).replace(os.sep, "/")


def links(text, rel):
    """The source paths that the links in a piece of text point at."""
    targets = (resolve(match.group(3), rel) for match in LINK.finditer(text))
    return {target for target in targets if target}


def is_markdown(path):
    if path.endswith(".md"):
        return True
    if os.path.splitext(path)[1]:
        return False
    with open(path, "rb") as handle:                  # a Markdown note saved with no extension
        return b"\0" not in handle.read(4096)


def plan(source):
    """Map every published source file to its path in the site.
    Also returns the files left out, each with the reason."""
    found = []
    for folder, dirs, files in os.walk(source):
        dirs.sort()
        for name in sorted(files):
            full = os.path.join(folder, name)
            found.append((os.path.relpath(full, source).replace(os.sep, "/"), full))
    flagged.clear()
    flagged.update(web_path(rel) for rel, full in found if is_markdown(full) and is_private_page(read(full)))
    mapping, skipped = {}, []
    for rel, full in found:
        reason = why_excluded(rel)
        if reason:
            skipped.append((rel, reason))
            continue
        if rel == HOME_PAGE:
            target = "index.md"
        else:
            target = "/".join(slug(part) for part in rel.split("/"))
            if is_markdown(full) and not target.endswith(".md"):
                target += ".md"
        if target in mapping.values():
            sys.exit(f"Two files would both be published as {target}; rename one in the source.")
        mapping[rel] = target
    return mapping, skipped


def rewrite(text, rel, mapping, warnings, used):
    """Point every link at the new names; drop lines that link to unpublished pages.
    The source files that the lines kept link to are added to used."""
    new_here = os.path.dirname(mapping[rel])
    out = []
    in_code = in_math = False
    for line in text.split("\n"):
        drop = False
        linked = set()
        if line.lstrip().startswith("```"):
            in_code = not in_code
        elif line.strip() == "$$":
            in_math = not in_math
        elif not in_code and not in_math:
            line = INLINE_MATH.sub(r"$$\1$$", line)
            line = DETAILS.sub(r'<details markdown="1"\1>', line)
            line = LINE_BREAK.sub("  ", line)
            # A table must be set off by blank lines, or it is shown as text.
            is_table, was_table = is_table_row(line), out and is_table_row(out[-1])
            if line.strip() and out and out[-1].strip() and is_table != was_table:
                out.append("")

        def fix(match):
            nonlocal drop
            bang, label, href = match.groups()
            target = resolve(href, rel)
            if target is None:
                return match.group(0)                      # web link, anchor, or absolute path
            fragment = href.partition("#")[2]
            if target in mapping:
                linked.add(target)
                new = os.path.relpath(mapping[target], new_here or ".").replace(os.sep, "/")
                return f"{bang}[{label}]({quote(new)}{'#' + fragment if fragment else ''})"
            if target.startswith("../") or is_excluded(target):
                drop = True                                # outside the site, or private
            else:
                warnings.append(f"{rel}: broken link to {href}")
            return match.group(0)

        line = LINK.sub(fix, line)
        if not drop:
            out.append(line)
            used |= linked
    return "\n".join(out)


def build(source):
    mapping, skipped = plan(source)

    # Work out every page before touching the site, so a problem changes nothing.
    warnings, problems, pages, hidden = [], [], {}, {}
    used, private_links = set(), set()
    for rel, _ in skipped:                                # what the private pages link to
        full = os.path.join(source, rel)
        if is_markdown(full):
            private_links |= links(read(full), rel)
    for rel, target in mapping.items():
        if target.endswith(".md"):
            text, removed = strip_private(read(os.path.join(source, rel)), rel, problems)
            if removed:
                hidden[rel] = len(removed)
                private_links |= links("\n".join(removed), rel)
            pages[rel] = rewrite(text, rel, mapping, warnings, used)
    if problems:
        sys.exit("Nothing was published. Fix the private tags first:\n  " + "\n  ".join(problems))
    for rel in sorted(private_links - used):              # an image only private text shows
        if rel in mapping and rel not in pages:
            del mapping[rel]
            skipped.append((rel, "only used in private text"))

    for name in os.listdir(SITE):                         # clear the previous build
        if name not in KEEP:
            path = os.path.join(SITE, name)
            shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)
    for rel, target in mapping.items():
        src, dst = os.path.join(source, rel), os.path.join(SITE, target)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if rel in pages:
            with open(dst, "w", encoding="utf-8") as handle:
                handle.write(pages[rel])
        else:
            shutil.copyfile(src, dst)
    print(f"Published {len(mapping)} files from {source}")
    for rel, reason in skipped:
        print(f"  left out: {rel} ({reason})")
    for rel, count in hidden.items():
        print(f"  hid {count} private passage{'s' if count > 1 else ''} in {rel}")
    for warning in warnings:
        print(f"  warning: {warning}")


def git(*args):
    return subprocess.run(["git", "-C", SITE, *args], check=True, text=True, capture_output=True).stdout


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    source = os.path.expanduser(args[0] if args else DEFAULT_SOURCE)
    if not os.path.isfile(os.path.join(source, HOME_PAGE)):
        sys.exit(f"{source} does not look like the knowledge base (no {HOME_PAGE})")
    build(source)
    changes = git("status", "--porcelain")
    print(changes or "No changes.")
    if "--push" in sys.argv and changes:
        git("add", "-A")
        git("commit", "-m", f"Publish knowledge base {datetime.date.today()}")
        git("push")
        print("Pushed. GitHub Pages updates in a minute or two.")


if __name__ == "__main__":
    main()
