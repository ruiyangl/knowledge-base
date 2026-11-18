# Knowledge base (generated site)

This repository is generated. Do not edit the pages here: the next build overwrites them.

- The notes live in `~/openclaw-data/main/knowledgeBase`. Edit them there, and read the
  `CLAUDE.md` in that folder first: it explains how to publish and how to keep things private.
- The only files that belong to this repository are `publish.py`, `_config.yml`, `_includes/`,
  `README.md`, `.gitignore` and this file. A build leaves them alone.
- Publishing is manual: `python3 publish.py` builds a preview and pushes nothing;
  `python3 publish.py --push` publishes. Run the second only when the user asks for it.
- The privacy rules (the `EXCLUDE` deny list, `private: true` in a page's front matter, and
  `<private>...</private>` passages) are implemented in `publish.py`. If you change them, test
  on a copy of the script in a scratch folder with made-up notes before running it here.
