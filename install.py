import sys

from launch import is_installed, run


if not is_installed("rembg"):
    python = sys.executable
    run(f'"{python}" -m pip install rembg', desc="Installing rembg", errdesc="Couldn't install rembg")
