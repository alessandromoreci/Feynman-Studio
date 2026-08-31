# Building Feynman Studio as a native macOS app

This turns `index.html` into a real `Feynman Studio.app` you can drop into
your Applications folder, with its own icon and Dock presence — using
[pywebview](https://pywebview.flowrl.com/) (native window) and
[py2app](https://py2app.readthedocs.io/) (packaging).

Run all of this **on your Mac**, from a Terminal, inside this folder (the
one containing `main.py`, `setup.py`, `index.html`, `logo.png`,
`make_icon.sh`).

## 1. Create a virtual environment

Modern Homebrew Python refuses system-wide `pip install`
(`externally-managed-environment` error) — a virtual environment sidesteps
that entirely and keeps dependencies isolated from the rest of your system:

```bash
python3 -m venv venv
source venv/bin/activate
```

Your prompt should now show `(venv)` at the start of the line. **You need to
re-run `source venv/bin/activate` every time you open a new Terminal window**
before running any command below — it doesn't stay active across sessions.

## 2. Install the dependencies

```bash
python3 -m pip install pywebview py2app pyobjc-framework-Cocoa pyobjc-framework-WebKit pyobjc-framework-Quartz
```

## 3. (Optional) sanity-check before packaging

```bash
python3 main.py
```

A native window with Feynman Studio should open. This only runs the app
in place — it does **not** create an installable `.app` yet. Close the
window and move on once this works.

## 4. Build the icon

```bash
chmod +x make_icon.sh
./make_icon.sh
```

Converts `logo.png` into `Icon.icns` using macOS's built-in `sips`/
`iconutil` — no extra install needed. `logo.png` is only 128×128, so the
larger icon sizes are upscaled and a bit soft, but perfectly usable for a
Dock/Finder icon.

## 5. Build the app

```bash
python3 setup.py py2app
```

This can take a minute. When it finishes, `dist/Feynman Studio.app` is
your finished, double-clickable app.

## 6. Install it

Drag `dist/Feynman Studio.app` into **Applications**. From there it behaves
like any other Mac app — Dock, Spotlight, Launchpad, all included.

## Updating the app later

If you change `index.html`, replace it in this folder and repeat only
step 5 (`python3 setup.py py2app`) — no need to rebuild the icon or the
venv.

## Troubleshooting

- **`externally-managed-environment` error** → you skipped the venv (step 1)
  or aren't inside it. Run `source venv/bin/activate` again and retry.
- **`ModuleNotFoundError: No module named 'webview'`** even after installing
  → almost always means step 2 was run outside the activated venv. Check
  your prompt shows `(venv)`, then reinstall.
- **`python3 main.py` opens a window fine, but there's no app in
  Applications** → that step alone never creates an `.app` — you still need
  steps 4 and 5.
- **Gatekeeper blocks the app ("unidentified developer")** → right-click the
  app → Open, then confirm. Expected for an app that isn't signed with an
  Apple Developer certificate.
