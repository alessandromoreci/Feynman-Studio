<p align="center">
  <img src="docs/logo.svg" width="88" alt="Feynman Studio logo">
</p>

<h1 align="center">Feynman Studio</h1>

<p align="center">
  <b>A diagram editor for many-body physics.</b><br>
  Draw Green's functions, self-energies, phonon propagators and vertex kernels, label them in LaTeX,<br>
  and export them to TikZ, SVG, PDF or PNG, all inside your browser.
</p>

<p align="center">
  <a href="https://alessandromoreci.github.io/Feynman-Studio/"><img src="https://img.shields.io/badge/Open%20the%20app-0071e3?style=for-the-badge" alt="Open the app"></a>
  &nbsp;
  <a href="https://github.com/alessandromoreci/Feynman-Studio/archive/refs/heads/main.zip"><img src="https://img.shields.io/badge/Download-1d1d1f?style=for-the-badge" alt="Download"></a>
</p>

<p align="center">
  <a href="https://github.com/alessandromoreci/Feynman-Studio/wiki"><b>User guide and tutorials (wiki)</b></a>
</p>

<p align="center">
  <sub>Version 3.1 · one HTML file · no installation · no account · your diagrams never leave your computer</sub>
</p>

<br>

<p align="center">
  <img src="docs/hero.png" width="100%" alt="Feynman Studio: the Dyson equation, the GW and Fan–Migdal self-energies, a four-point kernel, a Hartree diagram and the phonon Dyson equation; the GW interaction is selected and its properties appear right above it">
</p>

<br>

## Contents

- **[User guide and tutorials (wiki)](https://github.com/alessandromoreci/Feynman-Studio/wiki)** — step by step: Dyson, *GW*, electron–phonon, Keldysh, kernels, LaTeX
- [What it is for](#what-it-is-for)
- [Quick start](#quick-start)
- [A tour of the interface](#a-tour-of-the-interface)
- [Drawing](#drawing) — vertices, lines, kernels, text and LaTeX, curved arrows, icons
- [Physics notation](#physics-notation) — Keldysh contour, electron–phonon, physics check
- [Editing](#editing) — selection bar, Customize, style, guides, transformations
- [The Library and your templates](#the-library-and-your-templates)
- [Export](#export)
- [Projects, tabs, versions and sharing](#projects-tabs-versions-and-sharing)
- [Install it as an app · iPad](#install-it-as-an-app--ipad)
- [Appearance](#appearance)
- [Keyboard shortcuts](#keyboard-shortcuts)
- [Tips](#tips)
- [How it works](#how-it-works)
- [Support and files](#support-and-files)
- [What's new](#whats-new)
- [Citing Feynman Studio](#citing-feynman-studio)

<br>

## What it is for

Feynman Studio is made for the diagrams of **condensed-matter and many-body theory**: Green's functions and their Dyson equations, self-energies (Hartree, Fock, *GW*, Fan–Migdal, Debye–Waller, Ehrenfest), polarizations and screened interactions, phonon propagators, vertex functions and two-particle kernels, on and off equilibrium.

| You are preparing… | What helps |
|---|---|
| **A paper** | TikZ code that compiles as it is, figures at the real column width (APS one or two columns), labels in the font size of your document, TikZ that sits inside an equation |
| **A thesis** | the thesis width (15 cm), the same look everywhere with *Uniform style* and *copy & paste style*, every diagram exported at once, your own templates for the diagrams you draw again and again, versions to go back to |
| **Slides and posters** | PNG up to 8× or PDF, transparent background or the dark colours of the canvas, a diagram copied as an image straight into your slides, only the part you selected |
| **A talk or a journal club** | the *Present* mode: your tabs as full-screen slides, no other program needed |
| **Lectures and notes** | ready-made diagrams to start from, icons that *explain* a diagram (where it is cut, what is included, what is approximated) |
| **Discussions with colleagues** | a link that carries the whole diagram (nothing is uploaded), editable `.json` projects |
| **Non-equilibrium work** | Keldysh components on lines (<, >, R, A, M, T, T̄, ⌉, ⌈) and Keldysh branches on vertices (−, +, M) |
| **Electron–phonon theory** | the phonon propagator as a spring and the coupling *g* as a rhombus, in the notation of Stefanucci and Perfetto |

<br>

## Quick start

1. **[Open the app](https://alessandromoreci.github.io/Feynman-Studio/)**, or download `index.html` and double-click it. Nothing to install — but you can [install it as an app](#install-it-as-an-app--ipad) if you like.
2. **Click** on the canvas to place vertices, then **click two vertices** to join them with a line.
3. **Double-click** any element to select it: its main properties appear right above it, in the **selection bar**.
4. Press <kbd>L</kbd> for the **Library** of ready-made diagrams, <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>E</kbd> to **export**, <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>S</kbd> to **save** the editable project.

<p align="center">
  <img src="docs/demo.gif" width="88%" alt="Placing two vertices, joining them, turning the line into a photon from the selection bar, then dragging the GW self-energy from the Library">
</p>

To see a full example, open [`examples/showcase.json`](examples/showcase.json) (the diagram at the top of this page) with <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>O</kbd> or by dropping it on the canvas. An illustrated ten-step guide is always available under **Help**, in the bottom bar and in the logo menu.

<p align="center">
  <img src="docs/help.png" width="80%" alt="The built-in illustrated guide">
</p>

<br>

## A tour of the interface

The canvas fills the window and the tools come to you when you need them.

| Where | What |
|---|---|
| **Logo** (top left) | the canvas menu: 16 canvases, grid spacing (6 to 120 px), snap to grid, minimap, bottom bar on / off; **Diagrams**: present, export all, versions, duplicate, find & replace, uniform style; links to Help, shortcuts, GitHub and issues |
| **Tabs** (top) | several diagrams open at once, each with its own undo; hover a tab to preview it, double-click to rename it, right-click to duplicate it or see its versions |
| **Tool bar** (above the canvas) | tool panel, vertex shape, line style, free text, library, undo / redo, focus mode |
| **Selection bar** (above what you select) | the properties you use most, plus **Customize**, copy / paste style, duplicate, delete and **More** |
| **Library** (bottom, <kbd>L</kbd>) | diagrams, kernels, icons and your own templates, to click or drag onto the canvas |
| **Export** (top right, <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>E</kbd>) | every format with a live preview, plus the project file |
| **Zoom bar** (bottom right) | pan, zoom, fit to the diagram, canvas settings, keyboard shortcuts — pinch or <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+scroll zoom the canvas wherever the pointer is, never the page |
| **Command palette** (<kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>K</kbd>) | type what you want to do: every action of the app, every icon and diagram |
| **Right-click** | quick actions: duplicate mirrored, align and distribute, layers, mirror a pattern, paste here, copy as image, export… |

Prefer the side panels of earlier versions? *Appearance → Layout → Classic* brings them back, with every feature.

<br>

## Drawing

### Vertices

- **40 shapes** in eight families — circles, squares, triangles up and down, diamonds, hexagons, stars and crosses — each filled, outlined, concentric or in two colours (black half on the left or on the right). The shape button of the selection bar shows them all with a preview.
- **Four labels** per vertex (top, bottom, left, right), each one draggable to any position; label colour follows the vertex unless you choose another one.
- **External vertices** (<kbd>E</kbd>) are transparent points where a line just ends.
- **Auto-numbering** of new vertices, or *Number vertices* from the command palette (1, 2, 3… or 1, 2, 3̄, 4̄).
- Size, rotation and two colours for every shape.

### Lines

- **Ten styles:** solid (fermion), dashed, dotted, dash-dot, sine (photon, interaction), square wave, zig-zag, coil, gluon and phonon. Keys <kbd>1</kbd> … <kbd>9</kbd>, <kbd>0</kbd> pick the style of the selection or of the next lines you draw.
- **Arrows** halfway along the line (by length, also on lopsided arcs, exactly as in TikZ), with their size and direction; **double lines** for dressed propagators, with their distance; the **line width** of each line (in TikZ too).
- **Curves and loops:** drag the handle in the middle of a line to bend it into an arc, as little or as much as you like; a line from a vertex to itself is a self-loop (tadpoles, Hartree, Debye–Waller).
- **Waves that fit:** the number of waves and curls adapts to the length of the line; wave height and wave length can be set per line, and asymmetric patterns mirrored with <kbd>M</kbd>.
- **Reconnect** a line by dragging one of its ends onto another vertex. Lines always start and end exactly on their vertices.
- **One LaTeX label** per line, on either side.
- **A vertex inside a line:** select it and press <kbd>X</kbd> (or *Add a vertex* in its selection bar): the line is cut in two at its middle, and the new vertex can be dragged anywhere — a self-energy insertion or a vertex correction in two seconds.

<p align="center">
  <img src="docs/line-styles.png" width="100%" alt="The ten line styles">
</p>

### Kernels

Vertex functions, self-energy blobs and two-particle kernels are **single blocks** with 2, 4 or 6 legs (3 for triangles):

- **Body:** box, circle, ellipse, triangle or right triangle; solid or gradient fill (left → right, top → bottom, two diagonals, radial); a pattern inside — **none, grid, horizontal lines or vertical lines** — with its density; border style, colour and width; a LaTeX label inside.
- **Every leg is independent:** its own line style, colour, arrow direction, length and position along the side. Set them in the Inspector, or drag the handle in the middle of a leg on the canvas.
- **Outer vertices** with any of the 40 shapes (or none) and their own labels.
- Lines attached to a block follow it when you move, rotate or mirror it.

<p align="center">
  <img src="docs/kernels.png" width="100%" alt="Kernels of every shape with every pattern; one is selected with the full Inspector open, and the Library shows the kernel shapes with the pattern choice">
</p>

### Text and LaTeX

Every label is LaTeX, typeset live: vertex labels, line labels, kernel labels and free text.

- **Double-click a label** to edit it in place on the canvas; <kbd>Enter</kbd> applies, <kbd>Esc</kbd> cancels.
- **Symbol palette** with search (*alpha*, *sum*, *hbar*…) and the symbols you use most under *Recent*.
- **Label presets** (*G*, *G*₀, *W*, *v*, Σ, Π, *D*…) under every line and kernel label, the one suited to the line style outlined; add your own with **+**.
- **Free text** anywhere, with size, colour, rotation and an optional highlighted background — for equations such as *Σ(1,2) =* next to a diagram.

### Curved arrows and icons

- **Curved arrows** with an optional text along them, dashed or solid, with or without the line: to point at a part of a diagram or to show a flow.
- **36 icons**, in two groups. *Explain a diagram*: scissors where a diagram is cut (one- or two-particle reducible), included / excluded, caution, zoom into a block, self-consistency, static, quench, laser pulse, time evolution, temperature, counterterm, probe, key idea, leads to, approximation, open question, note. *Physics*: honeycomb lattice, K / K′ valleys, exciton, circular polarization, photoemission, optical cavity, lattice vibrations, coherent phonons, atom, conserving approximation, memory, detailed balance, spectral function, lifetime, collision integral, resummation, ab initio, band structure. Icons move, rotate, resize and take a colour like any text, and are exported to every format, TikZ included.

<p align="center">
  <img src="docs/icons.png" width="100%" alt="The Icons tab: Explain a diagram and Physics">
</p>

<br>

## Physics notation

### Keldysh contour

- **Keldysh component of a line**: <, >, R, A, M, T, T̄, ⌉, ⌈, written as a superscript of its label (*G* → *G*<sup><</sup>). In Customize or in the Inspector.
- **Keldysh branch of a vertex**: forward (−), backward (+) or Matsubara (M), shown as a small mark in the free corner next to the vertex. <kbd>K</kbd> cycles it on the selected vertices (<kbd>Shift</kbd>+<kbd>K</kbd> backwards); also in Customize.

### A physics check

*Check diagram* (in Export, and optionally before every export) flags overlapping labels, duplicated or stray elements, LaTeX errors — and **fermion arrows that do not balance at a vertex** (as many arrows must come in as go out).

### Electron–phonon diagrams

In the notation of Stefanucci and Perfetto: the phonon propagator *D* as a **spring**, the electron–phonon coupling *g* as a **rhombus** whose black half holds the electron vertex (four orientations), Π as a block. The Library has the phonon Dyson equation, the lowest-order phonon self-energy, the Fan self-energy with *g* vertices and the Ehrenfest self-energy ready to use.

<p align="center">
  <img src="docs/eph.png" width="88%" alt="Phonon Dyson equation, lowest-order phonon self-energy, Fan self-energy with rhombus vertices, Ehrenfest self-energy and screened interaction W, exported from Feynman Studio">
</p>

<br>

## Editing

<p align="center">
  <img src="docs/selection-bar.png" width="100%" alt="A selected kernel with its selection bar and the ready-made leg lengths">
</p>

### Selection bar

Right above whatever you select: colour, shape or style, size, label, arrow, double line, rotation, pattern, legs… Every change is **one undo step**. The bar glides to the next selection and never sits on top of the diagram you are working on. Its menus open right below or above it, on the side away from the diagram, always inside the canvas and never under the Inspector.

- **Select** with a double-click, add or remove with <kbd>Shift</kbd>+click (e.g. two blocks to rotate together), drag a box on the empty canvas to catch several elements (<kbd>Shift</kbd>+drag adds them to the selection), <kbd>Alt</kbd>+click to select a whole connected diagram, <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>A</kbd> for everything.
- With several elements selected: one colour for all, line style, rotate, flip, group, uniform style, save as template, export only the selection.

### Customize

The sliders button of the bar opens the finer settings of what is selected:

| Element | Settings |
|---|---|
| **Line** | line width, double-line distance, arrow size, reverse arrow, wave height and length, label size and side, Keldysh component |
| **Vertex** | second colour, Keldysh branch, label size and colour |
| **Kernel** | leg arrows (size, position), mirrored leg pattern, leg colour, gradient, pattern density, border style / colour / width, outer vertex shape / size / colour, label sizes and colours |
| **Text** | highlighted background and its colour |
| **Curved arrow** | line on / off, arrow size, text size and offset |

The panel opens beside the bar, **never on top of the diagram being edited**, and inside the canvas. **Pin** it to keep it open while you select other elements; **drag it by its title** to put it anywhere, and it stays there until you close it.

<p align="center">
  <img src="docs/customize.png" width="100%" alt="The Customize panel of a selected interaction line: double-line distance, arrow size, reverse arrow, wave height and length, label size and side">
</p>

### Copy & paste style

<kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>Alt</kbd>+<kbd>C</kbd> on one element, <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>Alt</kbd>+<kbd>V</kbd> on others — or the brush in the selection bar. It copies **how an element looks** (colours, line style, double line, arrows, waves, shapes, fills, borders, text size), never what it is or where it is (positions, connections, labels, LaTeX, rotation). The style of a line also goes onto the legs of kernels, and back.

### Uniform style

*Uniform style* (logo menu → Diagrams, the button of a multiple selection, or the command palette) gives the whole diagram — or the selection — one **label size, line width, arrow size and vertex size** in a single undoable step: the quickest way to make every figure of a thesis look alike.

### Groups and lock

- **Groups:** <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>G</kbd> joins the selection — for instance *Σ(1,2) =* and its diagram. A press on any member selects and moves the whole group; double-click a member to edit just that one; <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>G</kbd> ungroups. Copies of a group are groups of their own.
- **Lock:** <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>L</kbd> (or the padlock in the selection bar) keeps elements in place: they cannot be moved, rotated, flipped, resized or deleted until you unlock them — useful for a finished diagram while you work next to it.

### Sizes, guides and transformations

- **Ready-made sizes:** the small ▾ next to every size or angle opens a grid of values. Leg lengths and body sizes go in quarter-grid steps; the values marked with a dot keep the leg ends on grid points.
- **Snap to grid** for everything, with soft gliding from one grid point to the next; a diagram that is off the grid is brought onto it when you drag it; hold <kbd>Alt</kbd> to place freely. Grid spacing from 6 to 120 px.
- **Arrow keys** move the selection to the next grid node, <kbd>Shift</kbd>+arrows by one pixel.
- **Smart guides** (amber) show alignments and equal spacing while you drag vertices, kernels and texts.
- **Resize from the selection frame:** a corner scales anything proportionally (sizes, labels and arrows too; hold <kbd>Alt</kbd> to move positions only), a side handle stretches a multiple selection in one direction, <kbd>Shift</kbd> scales around the centre.
- **Flip and rotate:** <kbd>Shift</kbd>+<kbd>H</kbd> / <kbd>Shift</kbd>+<kbd>V</kbd>, <kbd>R</kbd> / <kbd>Shift</kbd>+<kbd>R</kbd> — exact for kernels and wavy lines too. Right-click → *Duplicate Mirrored* for symmetric diagrams.
- **Align and distribute** a multiple selection (left, centre, right, top, middle, bottom; evenly in either direction) from the right-click menu.
- **Layers:** bring forward / send backward with <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>]</kbd> / <kbd>[</kbd>, or from the right-click menu.
- **Full Inspector** with **More** or <kbd>I</kbd>: every property of the selection; it stays open for the next selections until you close it.
- **Undo** for every drag and every edit; a click on the empty canvas while something is selected only deselects, and a click that only closes a menu never places a vertex.

<br>

## The Library and your templates

<p align="center">
  <img src="docs/library.png" width="100%" alt="The Library open on the Diagrams tab">
</p>

Press <kbd>L</kbd> or click *Library* at the bottom, and **search** it by name (*fock*, *phonon*…). Click a tile to put it in the middle of the view, or drag it exactly where you want it. Every tab has the same size and its tiles fill it, so nothing hides behind a scroll bar.

- **Diagrams** — twelve ready-made diagrams, **without labels or numbers**, so you can write them in your own notation: Hartree, Fock, polarization bubble, *GW*, Fan–Migdal, Debye–Waller, Dyson equation, phonon Dyson equation, phonon self-energy, Fan with rhombus vertices, Ehrenfest self-energy, screened interaction *W*.
- **Kernels** — box, circle, ellipse, triangle and right triangle, with the number of legs and the pattern chosen at the top.
- **Icons** — *Explain a diagram* and *Physics*.
- **My templates** — select part of a diagram and click the star (*Save as template*) in the selection bar. Rename and delete them right on their tiles. They are kept in your browser; **Export…** saves them all in a `.json` file (a backup, or to share them with colleagues) and **Import…** adds templates from such a file.

<br>

## Export

<p align="center">
  <img src="docs/export.png" width="100%" alt="The Export panel with the live preview">
</p>

| Format | Use it for |
|---|---|
| **TikZ** | pasting into a LaTeX document: lines, curves, loops, waves, kernels, every vertex shape, line widths and icons come out as on the canvas; your LaTeX labels are kept as you wrote them |
| **SVG** | vector figures, with labels converted to paths |
| **PDF / PNG** | from 1× to 8×, cropped to the diagram plus your margin, optional transparent background |
| **Clipboard** | <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd> copies the diagram (or the selection) as an image, straight into slides or notes |
| **Share link** | the whole diagram inside a link, nothing uploaded |
| **Project (.json)** | the editable diagram, to reopen later |

Options:

- **Export all diagrams** — every tab at once: a **PDF with one page per diagram**, or a **.zip of PNG, SVG or TikZ** files named after the tabs.
- **Canvas colours** — export in the colours of the canvas: light lines on the dark background of a night, slate or blueprint canvas, for dark slides (PNG, PDF and SVG).
- **Selection only** — export just what is selected (lines bring the vertices they join); also from the export button of a multiple selection.
- **Figure width** — APS one column (8.6 cm), two columns (17.8 cm), thesis (15 cm) or custom: PNG, PDF and SVG get the real size of your document, the TikZ code is scaled, and a dashed box on the canvas shows the page width — fill it and the labels print at their true size.
- **TikZ for equations** — the drawing centred on the maths axis, to sit inside an equation, labels in the font size of your document.
- **Check diagram** — flags overlapping labels, duplicated elements and LaTeX errors before you export.
- A **live preview** shows exactly what you will get. Unless you choose *Canvas colours*, dark canvases only change the screen and exports stay black on white.

Using the TikZ code: the first lines list what to put in your preamble —

```latex
\usepackage{tikz}
\usetikzlibrary{arrows.meta, decorations.pathmorphing, decorations.markings, calc, shadings}
% plus svg.path when the diagram contains icons
```

— then paste the `tikzpicture` (or `\input` the exported file) where the figure goes.

<br>

## Projects, tabs, versions and sharing

- **Tabs:** several diagrams open at once; each tab keeps its own undo history. Double-click a tab to rename it, hover it for a preview, right-click it to **duplicate** it (to try a variant) or see its versions.
- **Versions:** save named snapshots of a diagram (logo menu → *Versions*) and go back to any of them; they are kept in the project file.
- **Find and replace in labels**, in one diagram or in all of them — e.g. *G*₀ → 𝒢₀ when you change notation.
- **Present:** the tabs become full-screen slides; ← and → (or Space) move between them, <kbd>Esc</kbd> leaves.
- **Save** with <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>S</kbd> (a `.json` file), **open** with <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>O</kbd> or by dropping the file on the canvas (it opens in a new tab).
- **Recovery:** the browser keeps a copy of the open diagrams, so a closed window does not lose your work.
- **Share link:** the whole diagram travels inside the link; whoever opens it sees it in Feynman Studio. Nothing is uploaded anywhere.
- Projects saved by earlier versions open unchanged.

<br>

## Install it as an app · iPad

- **Install:** open the [website](https://alessandromoreci.github.io/Feynman-Studio/) and use *Install* in Chrome or Edge (the icon in the address bar), *File → Add to Dock* in Safari on the Mac, or *Share → Add to Home Screen* on an iPad. Feynman Studio then opens in its own window with its own icon.
- **Offline:** after the first visit the website keeps a copy of the app and of its LaTeX libraries, so it also works without a connection, exports included.
- **iPad and touch screens:** tap to place vertices and join them, double-tap to select, drag with one finger, pinch to zoom, two fingers to pan, long press for quick actions. An Apple Pencil works like a finger.

<br>

## Appearance

<p align="center">
  <img src="docs/canvas.png" width="49%" alt="The canvas menu on the Blueprint canvas">
  <img src="docs/appearance.png" width="49%" alt="The Appearance panel">
</p>

- **16 canvases:** dots, grid, graph paper, paper, plain, crosses, ruled, engineering, and the dark ones — night, night grid, slate, blueprint, chalkboard, night crosses, graphite, black. On a dark canvas black lines and labels turn light and white fills take the background colour (on screen only).
- **Light or dark interface** and **12 accent colours**.
- **Six bar styles:** glass, classic, dark, translucent (the canvas runs under clear glass), tinted (glass with the accent colour) and floating (bars detached from the edges).
- **Studio or Classic layout**, how much glass, smooth motion on or off. With *reduce motion* set in your system, animations stay still.
- **Narrow windows** (split view, small laptops, iPad in portrait) rearrange the bars; every control can be reached with the keyboard and every icon button has a name for VoiceOver and other screen readers.
- **Focus mode** (<kbd>F</kbd>) hides everything but the canvas; the **bottom bar** can also be switched off for good (logo menu → *Bottom bar*).

<p align="center">
  <img src="docs/dark.png" width="100%" alt="Dark interface with the Violet accent on the Night canvas">
</p>

<br>

## Keyboard shortcuts

On macOS, use <kbd>⌘</kbd> instead of <kbd>Ctrl</kbd> and <kbd>⌥</kbd> instead of <kbd>Alt</kbd>. The full list is also under the keyboard button of the zoom bar.

| Action | Shortcut |
|---|---|
| Undo / redo | <kbd>Ctrl</kbd>+<kbd>Z</kbd> · <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Z</kbd> |
| Copy / paste / duplicate | <kbd>Ctrl</kbd>+<kbd>C</kbd> · <kbd>Ctrl</kbd>+<kbd>V</kbd> · <kbd>Ctrl</kbd>+<kbd>D</kbd> |
| Copy / paste style | <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>C</kbd> · <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>V</kbd> |
| Group / ungroup | <kbd>Ctrl</kbd>+<kbd>G</kbd> · <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>G</kbd> |
| Lock / unlock in place | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>L</kbd> |
| Select all | <kbd>Ctrl</kbd>+<kbd>A</kbd> |
| Save / open project | <kbd>Ctrl</kbd>+<kbd>S</kbd> · <kbd>Ctrl</kbd>+<kbd>O</kbd> |
| Export panel | <kbd>Ctrl</kbd>+<kbd>E</kbd> |
| Copy as image | <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd> |
| Command palette | <kbd>Ctrl</kbd>+<kbd>K</kbd> |
| Library | <kbd>L</kbd> |
| Full Inspector | <kbd>I</kbd> |
| Line style | <kbd>1</kbd> … <kbd>9</kbd>, <kbd>0</kbd> |
| Keldysh branch of the selected vertices | <kbd>K</kbd> · <kbd>Shift</kbd>+<kbd>K</kbd> |
| Mirror a line's pattern | <kbd>M</kbd> |
| External (transparent) vertex | <kbd>E</kbd> |
| Flip horizontally / vertically | <kbd>Shift</kbd>+<kbd>H</kbd> · <kbd>Shift</kbd>+<kbd>V</kbd> |
| Rotate 90° | <kbd>R</kbd> · <kbd>Shift</kbd>+<kbd>R</kbd> |
| Select the whole connected diagram | <kbd>Alt</kbd>+click |
| Add to / remove from the selection | <kbd>Shift</kbd>+click · <kbd>Shift</kbd>+drag a box on empty canvas |
| Place off the grid | hold <kbd>Alt</kbd> while dragging |
| Move the selection | arrow keys (next grid node) · <kbd>Shift</kbd>+arrows (1 px) |
| Add a vertex in the middle of the selected line | <kbd>X</kbd> |
| Bring forward / send backward | <kbd>Ctrl</kbd>+<kbd>]</kbd> · <kbd>Ctrl</kbd>+<kbd>[</kbd> (add <kbd>Shift</kbd> for front / back) |
| Focus mode | <kbd>F</kbd> |
| Close / deselect | <kbd>Esc</kbd> |
| Zoom in / out / 100 % | <kbd>Ctrl</kbd>+<kbd>=</kbd> · <kbd>Ctrl</kbd>+<kbd>−</kbd> · <kbd>Ctrl</kbd>+<kbd>0</kbd> |
| Zoom / pan | pinch or <kbd>Ctrl</kbd>+scroll · <kbd>Space</kbd>+drag |

<br>

## Tips

- **Same look everywhere in a thesis:** run *Uniform style* on every diagram, style one propagator of each kind and copy its style onto the others with <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>Alt</kbd>+<kbd>C</kbd> / <kbd>V</kbd>, save your recurring diagrams as templates, and export them all at once.
- **An equation and its diagram that move together:** select both and press <kbd>Ctrl</kbd>/<kbd>⌘</kbd>+<kbd>G</kbd>.
- **Before trying something new:** save a version (logo menu → *Versions*) or duplicate the tab.
- **Labels at the right size in the paper:** set the *Figure width* first, then fill the dashed box on the canvas.
- **An equation of diagrams:** put diagrams side by side and use free text for *=*, *+* and the symbols; *Alt*+click selects one diagram at a time to move it.
- **Symmetric diagrams:** draw half, then right-click → *Duplicate Mirrored*.
- **Only one diagram of a busy canvas:** select it and turn on *Selection only* in Export.
- **Internet connection:** the LaTeX libraries load from the internet the first time the page opens; the website (and the installed app) then keeps them for offline use. A copy of `index.html` opened from the disk without a connection still works, but exported labels fall back to a simple Unicode approximation.

<br>

## How it works

- The whole application is a single file, `index.html`, written in plain HTML, CSS and JavaScript with no build step and no server: it runs from GitHub Pages or from your disk. `manifest.webmanifest`, `sw.js` and `icons/` make the website installable and usable offline.
- Labels are typeset with [KaTeX](https://katex.org) on the canvas and with [MathJax](https://www.mathjax.org) for the exported figures. PDFs are written with [jsPDF](https://github.com/parallax/jsPDF). These libraries load from a CDN the first time the page opens.
- Nothing is uploaded anywhere. Your browser keeps only your interface preferences, your templates and a recovery copy of the open diagrams.
- Only what changes is redrawn, so a canvas with dozens of diagrams stays fluid while you drag.
- Developed and tested in Chromium-based browsers; any recent desktop browser should work.

<br>

## Support and files

Bug reports, ideas and diagrams for the library are very welcome: [open an issue](https://github.com/alessandromoreci/Feynman-Studio/issues), and attach the `.json` project that shows the problem if you can.

| File | What it is |
|---|---|
| `index.html` | the whole application |
| `manifest.webmanifest`, `sw.js`, `icons/` | installable, offline website |
| `examples/` | an example project (`.json`) |
| `docs/` | the pictures of this page and of the wiki |
| `LICENSE` | MIT licence |

<br>

## What's new

**3.1** — fluid on big canvases (only what changes is redrawn) and in Safari; <kbd>Shift</kbd>+click selection; a vertex inside any line (<kbd>X</kbd>); arrows and labels halfway along lopsided arcs; any bend; grid from 6 px, drags and arrow keys that land on the grid; menus of the selection bar placed next to it and always inside the canvas; the page never scrolls or zooms; the bottom bar can be hidden; calmer edge scrolling.
**3.0** — installable app that works offline; iPad and touch; groups and lock; line width and uniform style; export of every diagram at once and in the canvas colours; versions, duplicate tab, find & replace in labels; library search and template import / export; presentation mode; fermion-arrow check; narrow windows and accessibility.
**2.9** — copy & paste of styles; export of the selection only; alignment guides for texts and kernels; Keldysh branch with <kbd>K</kbd> and Keldysh options in Customize; Customize can be pinned and moved; the selection bar glides; templates renamed and deleted in the Library; the ready-made diagrams come without labels or numbers.
**2.8.1** — panels and menus keep clear of the diagram being edited; vertex shapes with previews.
**2.8** — the Customize panel; translucent, tinted and floating bars; a Library without gaps.

The full history is in the app: click the version number at the bottom left, or *What's new* in the logo menu.

<br>

## Citing Feynman Studio

If the app helped with the figures of a paper or thesis, a mention is appreciated, for instance in BibTeX:

```bibtex
@misc{FeynmanStudio,
  author       = {Moreci, Alessandro},
  title        = {{Feynman Studio}: a web editor for many-body {F}eynman diagrams},
  year         = {2026},
  version      = {3.1},
  howpublished = {\url{https://github.com/alessandromoreci/Feynman-Studio}}
}
```

## Feedback

Found a bug or have an idea? [Open an issue](https://github.com/alessandromoreci/Feynman-Studio/issues) and, if you can, attach the `.json` project that shows it.

<br>

<p align="center">
  Made by <a href="https://github.com/alessandromoreci"><b>Alessandro Moreci</b></a>, PhD student in theoretical condensed-matter physics at the University of Rome Tor Vergata<br>
  <a href="https://www.linkedin.com/in/alessandro-moreci-a35bbb247/">LinkedIn</a> · <a href="mailto:alessandromoreci27@gmail.com">Email</a>
</p>
