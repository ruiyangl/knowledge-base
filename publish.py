#!/usr/bin/env python3
"""Copy the knowledge base into this site, leaving out private pages.

The knowledge base the agents use stays the source; never edit this repository
by hand. Each run rebuilds the site from the source:

  - pages and folders listed in EXCLUDE are left out, and any line that links
    to them is removed;
  - file and folder names are cleaned for the web: Notion's 32-character ids
    are dropped and names become lower-case with dashes, so
    "Investment/Road to 1m 34ef...52.md" becomes "investment/road-to-1m.md";
  - every link between pages is rewritten to the new names;
  - the home page (knowledgeBase.md) becomes index.md.

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

# Never published. Each entry is a path inside the source, written without
# Notion's id; it matches the page and the folder of the same name.
EXCLUDE = [
    "financeKnowledge/Investment/Trade log",
    "financeKnowledge/Investment/Compliances",
]

# Files of this repository that a rebuild leaves alone.
KEEP = {".git", ".gitignore", "_config.yml", "README.md", "publish.py"}

HOME_PAGE = "knowledgeBase.md"
NOTION_ID = re.compile(r"\s+[0-9a-f]{32}$")
LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)")


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


def is_excluded(rel):
    """True if a source path is an excluded page, or inside an excluded folder."""
    parts = [strip_id(os.path.splitext(p)[0]) if i == len(rel.split("/")) - 1 else strip_id(p)
             for i, p in enumerate(rel.split("/"))]
    clean = "/".join(parts)
    return any(clean == e or clean.startswith(e + "/") for e in EXCLUDE)


def is_markdown(path):
    if path.endswith(".md"):
        return True
    if os.path.splitext(path)[1]:
        return False
    with open(path, "rb") as handle:                  # e.g. 'financials': Markdown with no extension
        return b"\0" not in handle.read(4096)


def plan(source):
    """Map every published source file to its path in the site."""
    mapping, skipped = {}, []
    for folder, dirs, files in os.walk(source):
        dirs.sort()
        for name in sorted(files):
            full = os.path.join(folder, name)
            rel = os.path.relpath(full, source).replace(os.sep, "/")
            if is_excluded(rel):
                skipped.append(rel)
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


def rewrite(text, rel, mapping, warnings):
    """Point every link at the new names; drop lines that link to unpublished pages."""
    here = os.path.dirname(rel)
    new_here = os.path.dirname(mapping[rel])
    out = []
    for line in text.split("\n"):
        drop = False

        def fix(match):
            nonlocal drop
            bang, label, href = match.groups()
            if re.match(r"^[a-z][a-z0-9+.-]*:|^#|^/", href, re.I):
                return match.group(0)                      # web link, anchor, or absolute path
            path, _, fragment = href.partition("#")
            target = os.path.normpath(os.path.join(here, unquote(path))).replace(os.sep, "/")
            if target in mapping:
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
    return "\n".join(out)


def build(source):
    mapping, skipped = plan(source)
    for name in os.listdir(SITE):                         # clear the previous build
        if name not in KEEP:
            path = os.path.join(SITE, name)
            shutil.rmtree(path) if os.path.isdir(path) else os.remove(path)
    warnings = []
    for rel, target in mapping.items():
        src, dst = os.path.join(source, rel), os.path.join(SITE, target)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if target.endswith(".md"):
            with open(src, encoding="utf-8") as handle:
                text = rewrite(handle.read(), rel, mapping, warnings)
            with open(dst, "w", encoding="utf-8") as handle:
                handle.write(text)
        else:
            shutil.copyfile(src, dst)
    print(f"Published {len(mapping)} files from {source}")
    for rel in skipped:
        print(f"  left out: {rel}")
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
