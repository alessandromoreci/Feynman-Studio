# Changelog

All notable changes to Feynman Studio. The same list is in the app: click the version number at the bottom left.

## 3.0 — 2026-10-17

- **Install it as an app**: from the website, your browser can install Feynman Studio (an icon in the Dock or on the iPad home screen, its own window). After the first visit it works offline too, LaTeX exports included.
- **Groups**: `Ctrl+G` joins the selection (e.g. “Σ(1,2) =” and its diagram) — a press on any member selects and moves all of it; double-click to edit one member; `Ctrl+Shift+G` ungroups.
- **Lock**: `Ctrl+Shift+L` (or the padlock of the selection bar) keeps elements in place — they cannot be moved, rotated, resized or deleted until unlocked.
- **Line width** for every line (Customize, and in TikZ), and **Uniform style**: one label size, line width, arrow size and vertex size for the whole diagram or the selection, in one step.
- **Export all diagrams**: a PDF with one page per tab, or a .zip of PNG, SVG or TikZ files named after the tabs. **Canvas colours**: export with light lines on the dark canvas, for dark slides.
- **Versions**: save snapshots of a diagram and go back to any of them; they travel in the project file. **Duplicate** a tab to try a variant. Right-click a tab for rename, duplicate, versions, close.
- **Find and replace in labels**, in one diagram or all of them (e.g. *G*₀ → 𝒢₀). **Library search**, and your templates can be exported and imported as a file — to back them up or share them.
- **Present**: the tabs become full-screen slides (← →, Esc). **Check diagram** now also flags fermion arrows that do not balance at a vertex.
- **iPad and touch**: tap to place and join, drag with one finger, pinch to zoom, two fingers to pan, long press for quick actions. Narrow windows and keyboard navigation work better, and every icon button has a spoken name for VoiceOver.

## 2.9

- **Momentum arrows**: `P` (or the arrow button of the selection bar) puts a small arrow with its label next to the selected lines — *k* on fermion lines, *q* on bosons — on the freer side. They follow the line when it moves, turns or bends; drag them to place them, edit the label, side and direction in Customize. They are copied, exported (PNG, PDF, SVG, TikZ) and deleted together with their line.
- **Copy & paste style**: `Ctrl+Alt+C` on an element, `Ctrl+Alt+V` on others (or the brush in the selection bar) — colours, line style, double line, arrows, waves, shapes, fills and borders, never positions, connections or labels. A line style also goes onto the legs of blocks.
- **Export only the selection**: the new *Selection Only* switch in Export (or the export button of a multiple selection) — PNG, PDF, SVG, TikZ and the preview; lines bring the vertices they join.
- **Alignment guides for texts and blocks**: labels and blocks you drag snap into line with vertices, blocks and other texts, and to equal spacing, with the amber guides.
- **Keldysh notation, quicker**: `K` cycles the branch of the selected vertices (none, −, +, M); branch and line component are also in Customize.
- **Customize, pinned and moved**: the pin keeps it open while you select other elements; drag it by its title to put it anywhere — it stays there until you close it.
- **Polish**: the selection bar glides to the next selection; your templates can be renamed and deleted right in the Library (*My templates*); the ready-made diagrams come without labels or numbers, ready for your notation; with “reduce motion” on, the new animations stay still.

## 2.8.1

- **Nothing covers what you are editing**: the selection bar, the Customize panel and every menu opened from them keep clear of the whole diagram you are working on (everything joined to the selection), stay inside the canvas and prefer empty space.
- **Vertex shapes with previews**: the shape button of the selection bar (and the shape of block vertices in Customize) opens a grid of all the shapes, with the name of the one under the pointer.

## 2.8

- **Customize**: the sliders button in the selection bar opens a small panel with the finer settings of what is selected — double-line distance, arrow size and direction, wave height and length (also in TikZ), label size and side for lines; leg arrows, border, gradient, pattern density, vertices and labels for blocks; label size and colours for vertices; background for texts; arrow and text of curved arrows. Every change is one undo step.
- **Three new bar styles**: *Translucent* (the canvas runs under clear glass bars), *Tinted* (glass with the accent colour) and *Floating* (bars detached from the edges). Appearance → Top and bottom bars.
- **Library**: every tab has the same size and its tiles fill it, without gaps — diagrams in two full rows, kernels at full height, icons in two blocks of 6 × 3. New icons: open question, note. The Keldysh contour is no longer in the Library.
- Double lines are a little closer by default (distance 3 instead of 4); lines already drawn keep theirs.

## 2.7

- **Kernel patterns for every shape**: box, circle, ellipse and triangles with no pattern, grid, horizontal or vertical lines — pick the pattern next to the number of legs (Library → Kernels, or the Blocks tab), or change it later from the selection bar.
- **One phonon line**: the propagator *D* is a single style, *Phonon* (key `0`); the older tight-curl lines of saved files become it.
- **Electron–phonon diagrams** made of fewer pieces: the rhombus *g* is itself the vertex where the electron and phonon lines meet, nothing sits on top of anything else.
- **Library**: larger, with diagrams and icons all in view, no sideways scrolling. The Keldysh contour now lives with the *Physics* pictures; new icons: approximation (≈) and band structure.
- **Appearance** laid out like the canvas menu: Interface, Accent colour, Bars, Behaviour.
- **Help**: a new first page, *The Studio at a glance*, and every page updated.

## 2.6

- **Electron–phonon diagrams** in the library, in the notation of Stefanucci–Perfetto (phonon propagator as a spring, coupling *g* as a rhombus whose black half holds the electron vertex): phonon Dyson equation *D = D₀ + D₀ΠD*, lowest-order phonon self-energy Π, Fan self-energy with *g* vertices, Ehrenfest self-energy, screened interaction *W = v + vPW*.
- **Export** has its own icon at the top right, next to the light / dark switch, and its own panel (or `Ctrl+E`): PNG, PDF, SVG, TikZ, figure width, project file and share link. The Inspector is only for editing.
- **TikZ for every vertex shape**: squares, triangles, diamonds, hexagons, stars and their two-colour versions now come out exactly as on the canvas (before, several became plain dots).
- **Six more accent colours**: Indigo, Teal, Amber, Pink, Olive, Crimson.
- **Library**: the tabs slide, the content follows the direction of the tab and the tiles come in one after the other; icons grouped under readable headings. Messages move above the open Library.
- **More in the selection bar**: rotation of vertices, fill of kernel blocks, highlighted background of texts; ready-made values for every rotation and for the pattern density.
- Line styles and menu entries start with a capital letter; the logo menu has more room.

## 2.5

- **Click the logo** (top left): canvas, grid spacing, snap to grid, minimap, and the links: Help, shortcuts, GitHub, report an issue, LinkedIn, contact. The links stay in the bottom bar too.
- **Sixteen canvases**, light and dark: new Crosses, Ruled, Engineering, Night crosses, Graphite and Black.
- **Ready-made sizes**: the small ▾ next to every size field (vertices, texts, labels, arrows, line distance, widths, leg length, body size, in the bar and in the Inspector) opens a grid of values; one click applies it and one undo takes it back. Leg lengths and body sizes now go in quarter-grid steps; the values marked with a dot keep the leg ends on grid points.
- **Kernel blocks with horizontal or vertical lines** inside the box (Library → Kernels, or *Pattern* in the bar and in the Inspector), exported to TikZ too. New *Default Body Size* next to *Default Leg Length*.
- **A click that only closes**: after a menu, a popover, the selection bar or `Esc` on a selection, the first click on the empty canvas just closes and deselects, it no longer drops a vertex. After choosing a tool (vertex shape, line style, text) a click places as before.
- **Fixes**: dragging a block (or anything else) no longer leaves a copy behind at the old place; the diagram tabs live only in the top bar (with their preview on hover); the Keldysh component is no longer in the selection bar (write it in the label, or use the Inspector).

## 2.4

- **Selection bar**: the most used properties sit right above what you select: colour, shape and size of a vertex; style, arrow, double line, label and Keldysh component of a line; legs, body and colours of a block; text, size, colour and angle of labels and icons; style of arrows. Each change is one undo step.
- **All the other properties** with the **More** button at the end of the bar or the `I` key: the full Inspector opens and stays open for the next selections until you close it. To have it open on every selection: Appearance → *Open the full Inspector on every selection*.
- **Ten canvases**: dots, grid, graph paper, paper, plain, and the dark ones night, night grid, slate, blueprint, chalkboard. On a dark canvas black lines and labels turn light and white fills take the background colour, so everything stays readable; exports always stay black on white.
- **Less repetition**: icons and kernels live only in the Library drawer, the GitHub and profile links only in the bottom bar. Grid spacing can be set from Appearance.

## 2.3

- **Studio interface**: the canvas fills the window; the Inspector floats on the right; the selection's own tools sit right above it.
- **Library drawer**: press `L` or the Library tab at the bottom: diagrams, kernels, icons and your templates. Click to insert, or drag one exactly where you want it; the drawer closes by itself.
- **Appearance** (the coloured dot at the top right): interface Studio or Classic, light or dark, accent colour, canvas (dots, grid, plain, paper, night), style of the top and bottom bars (glass, classic, dark) and what they show, amount of glass.
- **Export** button in the top bar opens the export options directly.

## 2.2

- **Resize from the selection frame**: select anything, one icon or a whole diagram, and drag a corner to scale it proportionally (sizes, labels and arrows too; `` = positions only). Side handles stretch a multi-selection in one direction; `Shift` scales around the centre.
- **Smooth motion**: moving icons, texts, blocks or whole selections only shifts what is already drawn, so it stays fluid even on large diagrams. Elements glide from one grid point to the next, lift slightly while dragged and settle when dropped.
- **Pan inertia**: a quick flick with `Space`+drag or the hand tool keeps the view gliding. Dragging towards the edge of the canvas scrolls it, and the selection box lights up the elements it is catching. Switch it off in ⚙ → *Smooth motion*.
- **Physics icons**: honeycomb lattice, K / K′ valleys, exciton, circular polarization, photoemission, optical cavity, lattice vibrations, coherent phonons, atom, conserving approximation, memory, detailed balance, spectral function, lifetime, collision integral, resummation, ab initio.

## 2.1

- **Icons**: scissors to show where a diagram is cut (one- or two-particle reducible), check / cross, caution, zoom into a block, self-consistency, static (snowflake), quench, laser pulse, time evolution, temperature, counterterm, probe, key idea, arrow. In the tool bar and in the *Text* tab; exported to PNG, PDF, SVG and TikZ.
- **Figure width** (Export tab): APS one column 8.6 cm, two columns 17.8 cm, thesis 15 cm or custom. PNG / PDF / SVG come out at that size, TikZ is scaled to it, and a dashed box on the canvas shows the real width.
- **TikZ for equations**: the drawing sits on the maths axis and the labels take the font size of your text.
- **Label presets**: *G*, *G*₀, *W*, *v*, Σ, Π, *D*… in one click under the label field, with a suggestion for the line style; save your own.
- **Number Vertices** 1, 2, 3̄, 4̄: end points plain, internal (integrated) vertices barred.
- **Keldysh notation**: component of a line (<, >, R, A, M, T, T̄, ⌉, ⌈) added to its label, branch of a vertex (−, +, M) as a small mark, and the Keldysh contour in the library.
- **Share link**: the whole diagram inside a link, nothing uploaded.

## 2.0 and earlier

### Build diagrams faster

- **Select a whole diagram** with `Alt+click` on any of its vertices, lines or blocks.
- **Flip & rotate** any selection: `Shift+H` / `Shift+V` mirror, `R` / `Shift+R` rotate 90°. Mirrors are exact, kernel blocks and wavy lines included.
- **Duplicate** with `Ctrl+D`, or right-click → *Duplicate Mirrored* for symmetric diagrams.
- **Diagram library**: Hartree, Fock, bubble, GW, Fan–Migdal, Debye–Waller, Dyson equation (unlabelled, ready for your notation) — plus your own saved templates.
- **Command palette** `Ctrl+K`: type what you want to do. Number keys `1`…`0` switch line style.
- **Live previews**: the line follows the cursor while you draw it, the next vertex shows where it will land; drag a line end to reconnect it.
- **Align & distribute** buttons for multi-selections, and a floating toolbar on any multi-selection.
- **Right-click menu** with quick actions, line style, layers, paste-here.
- **New line styles**: phonon and phonon 2, with a mirror switch (`M`) for asymmetric patterns.
- **Kernel blocks with 2, 4 or 6 legs**, each leg with its own line style and arrow direction (box, grid box, circle, ellipse): pick the number of legs above the presets, or change it later in the Inspector — attached lines stay connected.
- **Color themes** — Ocean, Forest, Sunset, Violet, Rose, Graphite — from the dot next to the light/dark switch (diagrams and exports are never recoloured).
- **Kernel body styling**: shape, solid / gradient / no fill, gradient direction (incl. radial and diagonal), grid or hatching pattern, dashed or dotted border.

### Look & feel

- **New colour picker** on every colour field: hue / shade square, hex code, harmonised palette, your recent colours and an eyedropper.
- **Label colours**: vertex labels and kernel vertex labels can have their own colour (or stay linked to the vertex colour) — kept in PNG, PDF, SVG and TikZ.
- **Help** (bottom bar): an illustrated step-by-step guide; a welcome card on an empty canvas; refined icons and tooltips that show the shortcut.
- `Ctrl+S` saves the project, `Ctrl+O` opens one.
- **Tool dock** on top of the canvas (vertex shape, line style, text, kernel, library, undo / redo); when something is selected it also shows its tools (colour, style, arrow, rotate / flip, duplicate, delete).
- **Tidier side panels**: tabs on the left (Draw · Blocks · Text) and on the right (Edit · Export), and the Inspector shows one section at a time. Prefer the long panels? ⚙ → *Compact side panels*.
- **Kernel legs one by one**: own colour and position — shift a leg along the side of the block, or drag the round handle in the middle of a leg (up / down moves it, left / right changes its length).
- **Edit labels on the canvas**: double-click a vertex, line or kernel-vertex label and type the LaTeX right there.
- **Drag a field's name** (Size, Arrow Size, Rotation…) left / right to change its value; `Shift` = faster, `` = finer.
- **Visual panels**: line styles as an icon grid, vertex shapes grouped in families (click again for the variants), option chips, symbol search with recent symbols, export as format tiles, recent line styles in the dock.
- **Smart guides** like Keynote: amber alignment lines and equal-spacing marks with the distance, with a small pulse when they engage.
- **Focus mode** `F`: panels and footer slide away. Softer spring animations; restored sessions reopen every tab at its zoom and position.

### Precision

- **Arrow keys** move the selection by a grid step, `Shift+arrows` by one unit; hold `` while dragging to place off-grid.
- **Layers**: put any element above or below others (`Ctrl+]` / `Ctrl+[`).
- Click targets stay the same size at every zoom; live values (Δ, angle, bend) while dragging.

### Output & safety

- **Exports typeset LaTeX exactly as on the canvas** (PNG, PDF, SVG).
- **Copy as image** straight to the clipboard: `Ctrl+Shift+C`.
- **Tight exports** cropped to the real content with your margin, from 1× to 8×; an automatic **diagram check** flags overlaps, duplicates and LaTeX errors.
- Collapsible Inspector sections, minimap, optional dark canvas, smooth appear / disappear animations.
- **Session recovery** after an accidental close; drop a .json on the canvas to open it.
- **TikZ export fixed and improved**: compiles cleanly, arrows in the middle of the lines as on the canvas, exact curves, self-loops, kernel bodies with gradients and patterns, per-leg colours, labels on the same side as on the canvas.
- Reliable undo for every drag and Inspector edit; `Ctrl+Z` / `Ctrl+Shift+Z`.
