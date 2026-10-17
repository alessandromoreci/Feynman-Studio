---
title: 'Feynman Studio: a web editor for the diagrams of many-body physics'
tags:
  - JavaScript
  - Feynman diagrams
  - many-body perturbation theory
  - nonequilibrium Green's functions
  - electron-phonon interaction
  - TikZ
authors:
  - given-names: Alessandro
    surname: Moreci
    orcid: 0000-0000-0000-0000   # TODO: replace with your ORCID
    affiliation: 1
affiliations:
  - index: 1
    name: Department of Physics, University of Rome Tor Vergata, Italy
    ror: 02p77k626
date: 17 October 2026          # TODO: the date of submission
bibliography: paper.bib
---

# Summary

Diagrams are the working language of many-body theory. Since Feynman introduced them for quantum electrodynamics [@feynman1949], they have become the standard way to write, organise and communicate perturbative expansions: Dyson equations, self-energies, polarizations, vertex functions and kernels. In condensed-matter physics they encode, for example, the *GW* approximation [@hedin1965], the theory of electron–phonon coupling [@giustino2017] and the nonequilibrium Green's function formalism on the Keldysh contour [@stefanucci2013; @stefanucci2023].

Feynman Studio is an open-source editor for these diagrams that runs entirely in a web browser. Users place vertices, join them with propagators (fermion lines, interactions, photons, phonons and gluons, single or doubled), bend lines into arcs and loops, and insert self-energy blobs and multi-leg kernels as single blocks. Every label is LaTeX, typeset live. Diagrams are exported to TikZ code that compiles with a standard LaTeX installation, to vector SVG, and to PDF or PNG at the column width of a journal or a thesis. The application is a single HTML file with no build step and no server: nothing is uploaded, and the same file works online, offline and installed as an application.

![The Feynman Studio editor with the Dyson equation, the *GW* and Fan–Migdal self-energies, a four-point kernel and a Hartree-type diagram. The selected interaction line shows its properties right above it.](figure.png)

# Statement of need

Drawing a many-body diagram for a paper or a thesis is still surprisingly laborious. The diagrams of condensed-matter theory differ from those of particle physics in several ways that general tools handle poorly: dressed (double) propagators next to bare ones, self-energy and polarization blobs, two-particle kernels with four or six legs whose order matters, labels that carry the space–time or contour arguments of the Green's function, Keldysh components and contour branches, and — in electron–phonon theory — dedicated symbols such as the coupling vertex drawn as a half-filled rhombus [@stefanucci2023]. Researchers typically either write TikZ code by hand, adjusting coordinates by trial and error, or draw in a generic vector-graphics program and lose both the LaTeX labels and the ability to edit the diagram later.

Feynman Studio targets graduate students and researchers in many-body and condensed-matter theory who need publication-quality diagrams quickly and want to keep them editable. Its design goals are: (i) the notation of the field as first-class objects (propagator styles, kernels, Keldysh labels, momentum arrows, electron–phonon vertices); (ii) direct manipulation, with a contextual bar of properties next to the selected element and every edit undoable; (iii) exports that are faithful to the canvas, in particular TikZ code that a LaTeX user can read, edit and compile; and (iv) zero installation, so that the tool can be used on any computer, in a lecture or during a discussion.

# State of the field

Several tools exist for drawing Feynman diagrams, most of them developed for high-energy physics. Axodraw [@vermaseren1994], feynMF [@ohl1995] and TikZ-Feynman [@ellis2017] are LaTeX packages: diagrams are written as code, which gives precise control but no visual editing. JaxoDraw [@binosi2004; @binosi2009] is a Java graphical editor that produces Axodraw code. FeynGame [@harlander2020] is a Java application built around particle-physics models, aimed largely at teaching, with its own export formats.

None of these targets the specific notation of many-body and nonequilibrium theory, and the graphical ones require a Java runtime. Feynman Studio was therefore built as a new tool rather than as an extension of an existing one: its data model (lines between vertices or kernel legs, multi-leg kernel blocks, labels attached to elements, Keldysh attributes) and its target platform (the browser, with no installation) are different from those of the existing editors. Its TikZ output uses only the standard TikZ libraries [@tantau_pgf], so it does not depend on a diagram package and can be edited by hand.

# Software design

The application is a single `index.html` file written in plain JavaScript, HTML and CSS. This choice favours longevity and portability over the convenience of a framework: the file can be archived, e-mailed or opened from a disk years later without a toolchain.

A diagram is a plain JSON object holding five lists — vertices, lines, free texts, curved arrows and kernel blocks. Lines are quadratic Bézier curves between two endpoints, which can be vertices or the legs of a kernel block; a kernel block is a single element whose legs are computed from its shape, so that attached lines follow it when it is moved, rotated or mirrored. Wavy, coiled and zig-zag propagators are generated along the curve with a number of periods adapted to its length. Elements such as momentum arrows store their position in the local frame of their line (midpoint, tangent and normal of the curve), so they follow the line when it moves or bends while keeping the place chosen by the user.

Every modification goes through a single rendering function, and the state before each edit is kept for undo. Exports are built from the state rather than from the screen: the SVG export typesets labels with MathJax [@cervone2012] and converts them to paths, and PNG and PDF are rasterised from that SVG; the TikZ export translates each element into TikZ paths and decorations, keeping the user's LaTeX source of every label. Labels on the canvas are rendered with KaTeX [@katex] for speed.

The repository contains end-to-end tests that open the application in a browser, draw and edit diagrams as a user would, and check every export; the TikZ output is also compiled with `pdflatex`. The tests run on every change through continuous integration.

# Research impact statement

<!-- TODO (author): replace this paragraph with concrete, verifiable evidence. For example:
     - the thesis chapters / papers / preprints whose figures were made with Feynman Studio (with references);
     - talks, lectures or journal clubs where it was used;
     - other people or groups using it (issues, messages, stars), with permission;
     - usage numbers of the website if available.
     JOSS asks for "specific, realized or credible near-term" impact: only list what can be checked. -->

Feynman Studio was developed during the author's doctoral work on nonequilibrium many-body theory of electrons and phonons at the University of Rome Tor Vergata, where it is used to prepare the diagrams of the theory in the notation of @stefanucci2023. [TODO: add the concrete evidence listed in the comment above.]

# AI usage disclosure

<!-- TODO (author): check that every statement below is true, complete it, and adapt it. JOSS requires the tools and
     versions, where they were used, the kind of assistance, and a confirmation that you reviewed the output and made
     the core design decisions. -->

Generative AI was used in the development of this software and in the preparation of this paper. Anthropic's Claude models [TODO: list the exact models and versions, e.g. the Claude Opus family, and the period of use] were used, through [TODO: claude.ai / Claude Code], to write and refactor large parts of the JavaScript code, the automated tests and the documentation, and to draft this paper. The author defined the features, the physical notation and the design of the application, reviewed and tested the generated code and text, checked the exported figures and the compiled TikZ code, verified every bibliographic reference against its publisher's record, and takes full responsibility for the content.

# Acknowledgements

<!-- TODO (author): funding (e.g. the doctoral fellowship), colleagues who tested the app or suggested features, and any conflict of interest (or "The author declares no conflict of interest"). -->

[TODO]

# References
