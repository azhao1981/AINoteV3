# uv : python 管理包

## windows 下
```shell
pip install uv -U
$env:UV_PYTHON_INSTALL_MIRROR = "https://gh-proxy.com/github.com/indygreg/python-build-standalone/releases/download"
uv python install 3.12
# Installed Python 3.12.11 in 34.52s
 + cpython-3.12.11-windows-x86_64-none (python3.12.exe)
# warning: `C:\Users\azhao\.local\bin` is not on your PATH. To use installed Python executables, run `$env:PATH = "C:`\Users`\azhao`\.local`\bin;$env:PATH"` or `uv python update-shell`.
uv python update-shell
# C:\Users\azhao\.local\bin
```

```bash
pip install uv -U
UV_PYTHON_INSTALL_MIRROR="https://gh-proxy.com/github.com/indygreg/python-build-standalone/releases/download" uv python install 3.12
```