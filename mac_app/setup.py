"""
Build script for py2app.

Run on your Mac (NOT here — py2app must run on macOS):
    python3 setup.py py2app

The finished app appears in dist/Feynman Studio.app
"""
from setuptools import setup

APP = ["main.py"]
DATA_FILES = ["index.html"]
OPTIONS = {
    "argv_emulation": False,
    "iconfile": "Icon.icns",  # created by make_icon.sh before running this
    "plist": {
        "CFBundleName": "Feynman Studio",
        "CFBundleDisplayName": "Feynman Studio",
        "CFBundleIdentifier": "com.alessandromoreci.feynmanstudio",
        "CFBundleVersion": "1.1.0",
        "CFBundleShortVersionString": "1.1.0",
        "NSHighResolutionCapable": True,
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
