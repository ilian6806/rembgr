from launch import is_installed, run_pip

if not is_installed("rembg"):
    run_pip("install rembg", "requirements for rembgr")
