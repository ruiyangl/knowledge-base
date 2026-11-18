# Knowledge Base

Notes on investing, valuation and AI infrastructure, published with GitHub Pages at
https://ruiyangl.github.io/knowledge-base/

This repository is generated. The source is a private knowledge base; `publish.py` copies it here,
leaves out private pages and passages, gives files web-friendly names and rewrites the links
between them. Do not edit the pages here by hand: change the source, then run

    python3 publish.py           # build a preview; nothing is pushed
    python3 publish.py --push    # publish

Three things keep a note private: the `EXCLUDE` deny list in `publish.py`, `private: true` in a
page's front matter, and `<private>...</private>` around part of a page.
