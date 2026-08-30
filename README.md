# Feynman Studio
<img width="1898" height="942" alt="Screenshot 2026-08-31 alle 01 54 13" src="https://github.com/user-attachments/assets/4bb95a16-ad73-4e74-91d6-e35b8c8003ad" />


**Advanced Diagram Editor** — a single-file, offline-capable web tool for drawing complex Feynman diagrams for theoretical physics research, aimed at researchers working in many-body perturbation theory and quantum dynamics.

🔗 **Live app:** open `index.html` directly in a browser, or serve it via GitHub Pages (see below).

## Features

- 40+ vertex shapes (circles, squares, triangles, diamonds, hexagons, stars, special shapes)
- 8 propagator line styles (solid, dashed, sine, square-wave, coil, gluon, etc.)
- Kernel / composite blocks as single indivisible elements
- Free text and LaTeX symbol placement, fully editable
- Independent decorations (free arrows/curves not anchored to diagram points)
- Multi-diagram tab system (Chrome-style tabs, each diagram independent)
- Export to **PNG, PDF, SVG, and TikZ/LaTeX**
- Light/dark theme toggle
- Snap-to-grid canvas with configurable spacing

## Usage

No installation, no server, no dependencies. Just open `index.html` in any modern browser.

> **Note:** the app does not autosave and always opens with a blank canvas by design. Use **Save Project** to export a `.json` file you can reopen later with **Load Project** — this is the only way to resume work across sessions. Image/TikZ exports are final renders and cannot be re-edited.

### Export formats

| Format | Editable later? | Notes |
|---|---|---|
| PNG / PDF | No | Raster image, LaTeX labels rendered via Unicode approximation |
| SVG | No | Vector, LaTeX labels rendered via Unicode approximation |
| TikZ/LaTeX | N/A (paste into a document) | Keeps raw LaTeX source untouched — use for publication-quality figures |
| Project (.json) | Yes | The only format that preserves full editability |

## License

MIT — see [LICENSE](LICENSE).

## Author

Alessandro Moreci — [alessandromoreci27@gmail.com](mailto:alessandromoreci27@gmail.com)

