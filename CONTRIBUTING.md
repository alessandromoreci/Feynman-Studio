# Contributing to Feynman Studio

Thank you for helping! Feynman Studio is developed and maintained by Alessandro Moreci (University of Rome Tor Vergata). Every kind of contribution is welcome: bug reports, ideas, diagrams for the library, documentation and code.

## Reporting a bug

[Open an issue](https://github.com/alessandromoreci/Feynman-Studio/issues/new) and include:

- what you did, what you expected and what happened instead;
- your browser and operating system (e.g. Safari 18 on macOS 15, Chrome on Windows 11);
- if you can, the project file of the diagram that shows the problem (*Export → Save Project*, a `.json` file) or a screenshot;
- for a problem with an export, the exported file (TikZ, SVG, PDF or PNG) and, for TikZ, the LaTeX error message.

## Asking for a feature or a diagram

Open an issue describing what you would like to draw or do, ideally with a picture (a sketch, a figure from a paper with its reference). Ready-made diagrams for the Library are especially welcome: draw the diagram in the app, save the project, and attach the `.json` file.

## Asking for help

Questions on how to use the app are welcome as issues too (label *question*). The built-in guide (**Help**, in the bottom bar and in the logo menu) and the [README](README.md) cover most features.

## Working on the code

The whole application is one file, `index.html` — HTML, CSS and plain JavaScript, with no build step. To work on it:

1. Fork the repository and clone your fork.
2. Serve the folder locally, e.g. `python -m http.server 8000`, and open <http://localhost:8000/index.html> (opening the file directly also works).
3. Edit `index.html` and reload the page.

How the file is organised:

- the **state** of a diagram is a plain object `{ vertices, lines, symbols, annotations, kernelUnits }`; every change goes through `render()`, and every edit pushes one undo step;
- the code is split into commented sections (`// ---------- 2.9 · Momentum arrows …`), each with a short explanation of what it does; newer features hook into `beforeRenderHooks` / `afterRenderHooks` rather than editing the core;
- exports are built from the state, not from the screen: `buildExportSVG()` (PNG, PDF, SVG) and `buildExportTikz()` (TikZ);
- the interface, the comments and the documentation are in English.

`manifest.webmanifest`, `sw.js` and `icons/` make the website installable and usable offline; they are not needed to open `index.html` from the disk.

### Tests

The end-to-end tests open the app in Chromium (through Playwright), draw and edit diagrams like a user and check the exports (the TikZ code is also compiled with `pdflatex` when it is installed):

```bash
pip install -r tests/requirements.txt
python -m playwright install chromium
pytest tests
```

They run automatically on every push and pull request (GitHub Actions, `.github/workflows/tests.yml`). Please add a test for any new feature or fixed bug.

### Pull requests

- Keep each pull request focused on one change, and describe what it does and why.
- Make sure the tests pass and the browser console shows no errors.
- Projects saved by earlier versions must keep opening unchanged: if you add a property to an element, give it a default.
- Exports matter: check that a change looks the same on the canvas, in the PNG / PDF / SVG and in the compiled TikZ.

## Support and maintenance

Feynman Studio is maintained on a best-effort basis by its author. Issues and pull requests are usually answered within two weeks. Releases are tagged on GitHub and listed in the [CHANGELOG](CHANGELOG.md).

## Code of conduct

Everyone taking part in this project is expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
