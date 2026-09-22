# AIM FAQ search

Search box for the nested FAQ accordion on the AIM Squarespace site (the block is used on several pages). The search bar sits above the accordion, pinned to the right at 340px wide (full width on phones); the accordion keeps its full width. Typing filters the questions in place. While a search is active a dashed "Still have a question?" panel (Luma webinar button, candidates@ email) shows below the results, or on its own when nothing matches; with results on screen, the match count under the search bar carries a grey italic "Still have a question?" link that jumps down to it. The page heading is not part of the block; it lives in other Squarespace blocks.

## What goes where in Squarespace

| File | Paste into |
| --- | --- |
| `squarespace/code-block.html` | The FAQ page's **Code block**, replacing the current contents. Same FAQ HTML as before, wrapped in `<div class="faq">` with the search bar before it and the "Still have a question?" panel after it, `data-keywords` on each question, and the search `<script>` at the end. |
| `squarespace/footer-injection.html` | **Settings → Advanced → Code Injection → Footer**, replacing the existing "FAQs nested accordion" script. Same slide behaviour, minus two glitches (a flash of content at the end of a close, and text settling upwards after an open, fixed by opening panels as `flow-root` so their children's margins stay inside), plus the section rules below. This script is shared by every nested dropdown on the site, so the rules apply site-wide. |
| `squarespace/custom-css.css` | **Design → Custom CSS**: delete the old FAQs-page block (`#collection-6a85b9d499575f03a8b87741 { … }`) and paste this at the top level. Every rule is scoped to the block's `.faq` wrapper rather than a page id, so it works on every page the block is used on. Flat, plain CSS: do not paste it inside another block. It carries the four existing FAQ rules (parent headings now `#812c36` and bold, child headings `font-family: inherit` at normal weight) plus layout for the search. The search rules set no fonts, sizes or colours: the status is a `p`, the panel title a body-size `p` in the heading style, the button uses Squarespace's button classes, the input inherits paragraph type. |

## How it behaves

Sections (top-level headings of any nested dropdown on the site, via the footer script):

- Only one section is open at a time; opening one closes the other.
- Clicking an open section shut also closes its questions, so it reopens clean.
- A section closed automatically (because you opened another) keeps its open questions, so flicking back shows them as they were.
- A top-level `.dropdown` with class `dropdown-multi` is exempt from the first rule; the FAQ search sets it while a search is active, since a search opens every matching section.

Search (in the FAQ code block):

- Searching starts at 2 characters. Every word must be found (at the start of a word, so "fund" finds "funding" but not "refund"); accents, curly quotes, hyphens and apostrophes are ignored ("cofounder" finds "co-founder").
- Filler words are dropped from whole-question queries ("can i bring my kids" searches for "bring kids"). If no answer contains every word, it shows the answers containing the most words and says so.
- 4 matches or fewer: the answers open automatically. More than that: the matching questions are listed closed. Matched words are highlighted.
- The "Still have a question?" panel shows whenever a search is active (copy lives in the code block, edit it there). Its button and email link have a long version for desktop and a short one for phones, in `.faq-wide` / `.faq-narrow` spans. With results it sits below them and the status line links down to it; with none it is the only thing under the search bar.
- Clearing the box, pressing Escape, or the field's own (x) puts the accordion back exactly as it was before the search.
- `data-keywords="…"` on a question adds hidden search terms (synonyms people type that the text doesn't contain). Edit freely; they never display.
- Tunables at the top of the script: `MIN_QUERY`, `AUTO_EXPAND_MAX`. Search bar width is `.faq-search-field { max-width }` in the CSS; the CSS sets no fonts, sizes or colours, so the block follows the site's typography; `scroll-margin-top` on the panel is the offset the jump link leaves for a fixed header.

## Local preview

`preview/base.css` is a mock of the site theme (guessed base `.dropdown` styles + the existing FAQ page CSS). `python3 preview/make-preview.py` stitches it with the three Squarespace files into `preview/index.html`; serve it with the `aim-faq-search` entry in `.claude/launch.json` (port 8932) or any static server. Nothing in `preview/` goes to Squarespace.
