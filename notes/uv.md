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

# uv

## 安装

外网直接安装

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 镜像源

https://github.com/astral-sh/uv/issues/6925

https://github.com/astral-sh/uv/issues/9053

pyproject.toml

```toml
[tool.uv]
index-url = "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple"

[tool.uv]
index-url = "https://mirrors.aliyun.com/pypi/simple"
```

```bash
mkdir ~/.config/uv && vim ~/.config/uv/uv.toml
```

```toml
index-url = "https://mirrors.aliyun.com/pypi/simple"
```
## python

```bash
UV_PYTHON_INSTALL_MIRROR="https://mirror.nju.edu.cn/github-release/indygreg/python-build-standalone/" uv python install 3.12
UV_PYTHON_INSTALL_MIRROR="https://gh-proxy.com/github.com/indygreg/python-build-standalone/releases/download" uv python install 3.12
```

## pyproject.toml

如何使用 poetry 的 pyproject.toml 来跑

```bash
uv pip install poetry-plugin-export --index-url "https://mirrors.aliyun.com/pypi/simple"
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

## ref

[Python 包管理工具 uv 使用教程](https://zhuanlan.zhihu.com/p/1888904532131575259)

