"""
Feynman Studio — native macOS launcher.

Opens index.html in a real native window (via pywebview) instead of a browser tab.
Works both when run directly with `python3 main.py` and when bundled into a
.app by py2app (see setup.py).
"""
import os
import sys
import webview


def resource_path(relative_path):
    """Resolve a path that works both in dev and inside the packaged .app bundle.

    py2app puts data_files (like index.html) into Contents/Resources and sets
    the RESOURCEPATH environment variable to that folder at runtime.
    """
    if getattr(sys, "frozen", False):
        base_path = os.environ.get("RESOURCEPATH", os.path.dirname(sys.executable))
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


def main():
    html_path = resource_path("index.html")
    webview.create_window(
        "Feynman Studio",
        html_path,
        width=1440,
        height=900,
        min_size=(900, 600),
    )
    webview.start()


if __name__ == "__main__":
    main()
