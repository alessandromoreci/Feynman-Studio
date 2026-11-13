#!/usr/bin/env python3
"""
Trasforma la pagina di Feynman Studio (feynman_studio.html) in una vera applicazione, con la sua icona.

    python3 build_app.py              costruisce l'app nella cartella "dist"
    python3 build_app.py --install    su Mac la copia anche in Applicazioni e la apre

Un'app vale per il sistema su cui e' stata costruita: lo script va lanciato su ogni tipo di computer.
  - Mac:      finestra nativa scritta in Swift (app/main.swift). Servono i "Command Line Tools" di Apple
              (lo script dice come installarli). Il risultato gira sia sui Mac Apple Silicon sia sugli Intel.
  - Windows:  un solo file "Feynman Studio.exe".
  - Linux:    un solo file eseguibile "feynman-studio".
Su Windows e Linux (o su Mac con --engine web) lo script scarica da solo, in una cartella temporanea,
gli strumenti che gli servono (pywebview, PyInstaller, Pillow): serve la rete la prima volta.

Accanto a questo script devono esserci:  app/icon.png  (il logo, quadrato, 1024 px)  e  app/main.swift.
"""
import argparse
import os
import platform
import plistlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
NAME = "Feynman Studio"
BUNDLE_ID = "io.github.alessandromoreci.feynmanstudio"


def say(msg):
    print("→ " + msg, flush=True)


def stop(msg):
    print("\n✗ " + msg, file=sys.stderr)
    sys.exit(1)


def run(cmd, **kw):
    """Esegue un comando; se fallisce mostra il suo messaggio e si ferma."""
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, **kw)
    if r.returncode != 0:
        out = (r.stdout or "") + (r.stderr or "")
        stop("Comando non riuscito: " + " ".join(str(c) for c in cmd[:4]) + " …\n" + out[-3000:])
    return r.stdout


def app_version(html_text):
    """La versione scritta nella pagina ("Feynman Studio 3.2"), altrimenti 1.0."""
    m = re.search(r"APP_VERSION\s*=\s*['\"](\d+(?:\.\d+){0,2})['\"]", html_text)
    return m.group(1) if m else "1.0"


# --------------------------------------------------------------------------- Mac: app nativa (Swift)
def make_icns(icon_png, out_icns, tmp):
    iconset = tmp / "AppIcon.iconset"
    iconset.mkdir()
    for size in (16, 32, 128, 256, 512):
        for scale in (1, 2):
            px = size * scale
            name = f"icon_{size}x{size}{'@2x' if scale == 2 else ''}.png"
            run(["sips", "-z", px, px, icon_png, "--out", iconset / name])
    run(["iconutil", "-c", "icns", iconset, "-o", out_icns])


def build_mac_native(html, icon_png, version, dist, tmp):
    swift = HERE / "app" / "main.swift"
    if not swift.exists():
        stop(f"Manca {swift}: e' il sorgente della finestra nativa.")
    if subprocess.run(["xcrun", "--find", "swiftc"], capture_output=True).returncode != 0:
        subprocess.run(["xcode-select", "--install"], capture_output=True)
        stop("Mancano i Command Line Tools di Apple (servono solo per compilare).\n"
             "  Si e' aperta la finestra di installazione: installa, poi rilancia questo script.\n"
             "  In alternativa: python3 build_app.py --engine web")

    # l'app si monta e si firma nella cartella temporanea: dentro una cartella sincronizzata con iCloud il sistema
    # aggiunge ai file attributi suoi, e la firma li rifiuta
    app = tmp / "bundle" / f"{NAME}.app"
    macos, res = app / "Contents" / "MacOS", app / "Contents" / "Resources"
    (res / "web").mkdir(parents=True)
    macos.mkdir(parents=True)

    say("compilo la finestra nativa (Apple Silicon e Intel)…")
    slices, min_os = [], {}
    for arch in ("arm64", "x86_64"):
        out, err = tmp / f"FeynmanStudio-{arch}", ""
        for target in ("12.0", "13.0"):      # con gli strumenti recenti la parte Intel si collega solo da macOS 13
            r = subprocess.run(["xcrun", "swiftc", "-O", "-swift-version", "5", "-target", f"{arch}-apple-macos{target}",
                                str(swift), "-o", str(out), "-framework", "Cocoa", "-framework", "WebKit"],
                               capture_output=True, text=True)
            if r.returncode == 0:
                slices.append(out)
                min_os[arch] = target
                break
            err = r.stderr or r.stdout
        else:
            if arch == platform.machine():
                stop("La compilazione non e' riuscita:\n" + err[-3000:])
            say(f"  (la versione {arch} non si compila su questo Mac: l'app girera' solo su Mac come questo)")
    exe = macos / "FeynmanStudio"
    if len(slices) == 2:
        run(["lipo", "-create", *slices, "-output", exe])
    else:
        shutil.copy2(slices[0], exe)
    exe.chmod(0o755)

    say("aggiungo pagina e icona…")
    shutil.copy2(html, res / "web" / "index.html")       # la finestra apre sempre web/index.html
    make_icns(icon_png, res / "AppIcon.icns", tmp)
    info = {
        "CFBundleName": NAME, "CFBundleDisplayName": NAME, "CFBundleIdentifier": BUNDLE_ID,
        "CFBundleExecutable": "FeynmanStudio", "CFBundleIconFile": "AppIcon", "CFBundlePackageType": "APPL",
        "CFBundleShortVersionString": version, "CFBundleVersion": version, "CFBundleInfoDictionaryVersion": "6.0",
        "CFBundleDevelopmentRegion": "en", "LSMinimumSystemVersion": min(min_os.values(), key=float),
        "LSMinimumSystemVersionByArchitecture": dict(min_os),
        "LSApplicationCategoryType": "public.app-category.education", "NSHighResolutionCapable": True,
        "NSPrincipalClass": "NSApplication", "NSHumanReadableCopyright": "Feynman Studio — Alessandro Moreci",
        "CFBundleDocumentTypes": [{
            "CFBundleTypeName": "Feynman Studio Project", "CFBundleTypeRole": "Editor", "LSHandlerRank": "Alternate",
            "LSItemContentTypes": ["public.json"], "CFBundleTypeExtensions": ["json"]}],
    }
    with open(app / "Contents" / "Info.plist", "wb") as f:
        plistlib.dump(info, f)
    (app / "Contents" / "PkgInfo").write_text("APPL????")

    say("firmo l'app (firma locale)…")
    subprocess.run(["xattr", "-cr", str(app)], capture_output=True)
    run(["codesign", "--force", "--deep", "--sign", "-", app])
    run(["codesign", "--verify", "--deep", app])
    final = dist / app.name
    if final.exists():
        shutil.rmtree(final)
    run(["ditto", "--norsrc", "--noextattr", app, final])
    return final


def install_mac(app):
    dest = Path("/Applications") / app.name
    say(f"installo in {dest}…")
    if dest.exists():
        subprocess.run(["osascript", "-e", f'tell application "{NAME}" to quit'], capture_output=True)
        shutil.rmtree(dest)
    run(["ditto", "--norsrc", "--noextattr", app, dest])
    subprocess.run(["xattr", "-cr", str(dest)], capture_output=True)
    run(["codesign", "--force", "--deep", "--sign", "-", dest])
    run(["codesign", "--verify", "--deep", dest])
    lsregister = ("/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework"
                  "/Support/lsregister")
    subprocess.run([lsregister, "-f", str(dest)], capture_output=True)
    subprocess.run(["open", str(dest)])
    return dest


# --------------------------------------------------------------------------- ogni sistema: pywebview + PyInstaller
LAUNCHER = '''\
import os, sys
import webview

base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
page = os.path.join(base, "web", "index.html")
home = os.path.join(os.path.expanduser("~"), ".feynman-studio")      # preferenze dell'app (mai le chiavi API)
os.makedirs(home, exist_ok=True)
webview.settings["ALLOW_DOWNLOADS"] = True                           # esportazioni: PNG, PDF, SVG, progetto
webview.create_window("Feynman Studio", page, width=1320, height=860, min_size=(900, 600))
webview.start(private_mode=False, storage_path=home, debug=False)
'''


def build_web_engine(html, icon_png, version, dist, tmp):
    system = platform.system()
    say("preparo gli strumenti in una cartella temporanea (la prima volta serve la rete)…")
    venv = tmp / "venv"
    run([sys.executable, "-m", "venv", venv])
    py = venv / ("Scripts/python.exe" if system == "Windows" else "bin/python")
    wanted = ["pyinstaller", "pillow", "pywebview[qt]" if system == "Linux" else "pywebview"]
    run([py, "-m", "pip", "install", "--quiet", "--upgrade", "pip"])
    run([py, "-m", "pip", "install", "--quiet", *wanted])

    work = tmp / "work"
    (work / "web").mkdir(parents=True)
    shutil.copy2(html, work / "web" / "index.html")
    (work / "launcher.py").write_text(LAUNCHER, encoding="utf-8")

    # l'icona nel formato del sistema
    if system == "Windows":
        icon = work / "icon.ico"
        run([py, "-c", "import sys; from PIL import Image; Image.open(sys.argv[1]).save(sys.argv[2], "
                       "sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])", icon_png, icon])
    elif system == "Darwin":
        icon = work / "AppIcon.icns"
        make_icns(icon_png, icon, tmp)
    else:
        icon = work / "icon.png"
        shutil.copy2(icon_png, icon)

    exe_name = NAME if system != "Linux" else "feynman-studio"
    cmd = [py, "-m", "PyInstaller", "--noconfirm", "--clean", "--windowed", "--name", exe_name,
           "--icon", icon, "--add-data", f"{work / 'web'}{os.pathsep}web",
           "--distpath", dist, "--workpath", tmp / "pyi", "--specpath", tmp / "pyi"]
    if system == "Darwin":
        cmd += ["--osx-bundle-identifier", BUNDLE_ID]
    else:
        cmd += ["--onefile"]
    say("costruisco l'app (qualche minuto)…")
    run(cmd + [work / "launcher.py"], cwd=work)

    if system == "Darwin":
        app = dist / f"{NAME}.app"
        leftover = dist / NAME                       # PyInstaller lascia anche la cartella non impacchettata
        if leftover.is_dir():
            shutil.rmtree(leftover)
        plist = app / "Contents" / "Info.plist"
        with open(plist, "rb") as f:
            info = plistlib.load(f)
        info.update({"CFBundleShortVersionString": version, "CFBundleVersion": version, "NSHighResolutionCapable": True})
        with open(plist, "wb") as f:
            plistlib.dump(info, f)
        subprocess.run(["xattr", "-cr", str(app)], capture_output=True)
        run(["codesign", "--force", "--deep", "--sign", "-", app])
        return app
    if system == "Windows":
        return dist / f"{exe_name}.exe"
    out = dist / exe_name
    shutil.copy2(icon_png, dist / "feynman-studio.png")
    (dist / "feynman-studio.desktop").write_text(
        "[Desktop Entry]\nType=Application\nName=Feynman Studio\nComment=Draw Feynman diagrams\n"
        f"Exec={out}\nIcon={dist / 'feynman-studio.png'}\nCategories=Education;Science;\nTerminal=false\n")
    return out


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description="Trasforma la pagina di Feynman Studio in un'applicazione.")
    ap.add_argument("--html", default=str(HERE / "feynman_studio.html"), help="la pagina da impacchettare (default: feynman_studio.html)")
    ap.add_argument("--icon", default=str(HERE / "app" / "icon.png"), help="il logo, PNG quadrato (default: app/icon.png)")
    ap.add_argument("--out", default=str(HERE / "dist"), help="dove mettere l'app (default: dist)")
    ap.add_argument("--engine", choices=["auto", "native", "web"], default="auto",
                    help="native = finestra Swift (solo Mac); web = pywebview + PyInstaller (ogni sistema); auto = native su Mac")
    ap.add_argument("--install", action="store_true", help="su Mac: copia in Applicazioni e apre l'app")
    a = ap.parse_args()

    html, icon, dist = Path(a.html).resolve(), Path(a.icon).resolve(), Path(a.out).resolve()
    if not html.is_file():
        stop(f"Non trovo la pagina: {html}")
    if not icon.is_file():
        stop(f"Non trovo il logo: {icon}")
    text = html.read_text(encoding="utf-8", errors="replace")
    if "<html" not in text[:2000].lower():
        stop(f"{html.name} non sembra una pagina HTML.")
    # la pagina con l'AI lascia eseguire solo gli script di cui conosce l'impronta: se e' stata modificata
    # senza aggiornare le impronte, l'app si aprirebbe vuota
    csp = HERE / "csp-update.py"
    if "Content-Security-Policy" in text[:6000] and csp.exists() and html.parent == HERE and html.name == "feynman_studio.html":
        r = subprocess.run([sys.executable, str(csp), "--check"], capture_output=True, text=True, cwd=HERE)
        if r.returncode != 0:
            stop("Le impronte degli script nella pagina non sono aggiornate.\n  Esegui prima:  python3 csp-update.py")

    system = platform.system()
    engine = a.engine
    if engine == "auto":
        engine = "native" if system == "Darwin" else "web"
    if engine == "native" and system != "Darwin":
        stop("La finestra nativa in Swift esiste solo per Mac: usa --engine web.")

    version = app_version(text)
    dist.mkdir(parents=True, exist_ok=True)
    say(f"{NAME} {version} · {html.name} · {system} ({platform.machine()})")
    with tempfile.TemporaryDirectory(prefix="feynman-build-") as t:
        tmp = Path(t)
        result = build_mac_native(html, icon, version, dist, tmp) if engine == "native" else build_web_engine(html, icon, version, dist, tmp)

    if not result.exists():
        stop("La costruzione e' finita senza errori ma l'app non c'e': " + str(result))
    print(f"\n✓ Fatto: {result}")
    if a.install:
        if system == "Darwin":
            print(f"✓ Installata: {install_mac(result)}")
        else:
            print("  (--install vale solo su Mac: su questo sistema basta spostare il file dove vuoi)")
    elif system == "Darwin":
        print("  Per metterla in Applicazioni:  python3 build_app.py --install")


if __name__ == "__main__":
    main()
