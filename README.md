# Ashish Shubham — personal website

A responsive, static personal website ready for GitHub Pages. No framework, package installation, or build service is required. All content is rendered in HTML and works without JavaScript; the small script only opens source notes when linked.

## Publish on GitHub Pages

1. For your main personal site, create or use the repository **ashubham.github.io** under your GitHub account. A project repository also works.
2. Upload **index.html** and **.nojekyll** to the repository root. Upload the remaining files too if you want to keep the editable source alongside the page. Do not upload the enclosing folder or ZIP itself.
3. In **Settings → Pages**, choose **Deploy from a branch**, then **main** and **/ (root)**, and save.
4. Once GitHub’s Pages deployment finishes, open the URL shown in those settings. For the personal repository this is `https://ashubham.github.io/`; project repositories use `https://ashubham.github.io/REPOSITORY/`.

The HTML is completely self-contained, including styles, portrait, and favicon. It can also be opened directly from your computer. All internal navigation uses fragments, so project-path hosting works.

## Edit

- `content.json`: speaking, writing, patents, media, conference service, and projects.
- `styles.css`: colors, typography, layout, responsive and print styles.
- `build.py`: page template, biography, contact links, service summaries, and source notes.
- `assets/ashish-shubham.jpg`: authentic portrait from the ThoughtSpot author profile.
- `SOURCES.md`: research inventory and editorial decisions.

After editing, run `python3 build.py` and commit the resulting `index.html` along with the changed source. Python’s standard library is sufficient. You may alternatively edit `index.html` directly, but a later build would overwrite those direct edits.

## Content review

Research date: September 28, 2026. The page includes all nine speaking listings and all nine conference reviewer/committee listings from the supplied resume, plus additional publicly found material. Read `SOURCES.md` and the site’s source notes for unresolved dates and resume-only entries. The two future organizer listings are labeled scheduled. Review/update them after those events.

No original resume PDF, telephone number, private correspondence, tracking, or third-party scripts are included. Public professional contact email is included. GitHub Pages is public when enabled; this package has not been deployed.

The portrait and referenced works remain subject to their respective rights. No license over third-party material is implied.
