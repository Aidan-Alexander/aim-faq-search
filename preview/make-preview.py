#!/usr/bin/env python3
"""Stitch the three Squarespace pieces into preview/index.html for local testing."""
import pathlib
root = pathlib.Path(__file__).resolve().parents[1]
sq = root / 'squarespace'
code = (sq / 'code-block.html').read_text()
footer = (sq / 'footer-injection.html').read_text()
css = (sq / 'custom-css.css').read_text()
base = (root / 'preview' / 'base.css').read_text()
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FAQ search preview</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Alan+Sans:wght@300..900&display=swap" rel="stylesheet">
<style>
{base}
</style>
<style>
/* ===== squarespace/custom-css.css (native CSS nesting stands in for Squarespace's LESS) ===== */
{css}
</style>
</head>
<body>
<div class="page">
<!-- ===== squarespace/code-block.html ===== -->
{code}
</div>
<!-- ===== squarespace/footer-injection.html ===== -->
{footer}
</body>
</html>
"""
(root / 'preview' / 'index.html').write_text(html)
print('wrote', root / 'preview' / 'index.html', len(html), 'bytes')
