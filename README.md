# Personal Start Page

A lightweight, responsive home page with quick links to frequently used sites.

## Use it locally

Open `index.html` in a browser.

## Customize it

Edit the links in the `Frequent links` section of `index.html`. Each link is a
standalone card, so cards can be added, removed, or reordered without changing
the layout CSS.

## Canonical bookmarks

Edit `bookmarks.json`, then run `python3 scripts/build-bookmarks.py` and commit both the JSON and generated JavaScript. The page works on GitHub Pages and directly from a local file on Starforge. The JSON is also the import source for the permission-protected Embry intranet. Personal and staff audience labels guide the intranet; the existing GitHub Pages page remains a public list. Service links do not grant access to their destinations.
