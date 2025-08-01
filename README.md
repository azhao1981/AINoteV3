


## 安装使用uv

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

## node pnpm


```bash
npm config get registry
npm config set registry=http://registry.npm.taobao.org
npm install -g pnpm

pnpm config set store-dir 'D:\dev\pnpm\store'

# 设置全局 bin 目录
pnpm config set global-bin-dir "D:\dev\pnpm-v22\bin"

# 设置 pnpm_home 目录
pnpm config set pnpm_home "D:\dev\pnpm-v22"
pnpm config get global-bin-dir
pnpm config get pnpm_home
```

```bash
sysdm.cpl
path
D:\dev\pnpm-v22\bin
$env:PATH
```

## qwen

在 windows 下的体验好过 cc

```bash
npm i -g @qwen-code/qwen-code

pnpm i -g @qwen-code/qwen-code
```

## link

```bash
Remove-Item "D:\dev\nodejs" -Force -Recurse
New-Item -ItemType SymbolicLink -Path "D:\dev\nodejs" -Target "D:\dev\node-v24.4.1-win-x64"

New-Item -ItemType SymbolicLink -Path "D:\dev\nodejs" -Target "D:\dev\node-v22.18.0-win-x64"

mkdir 'd:\dev\pnpm-v22'
mkdir 'd:\dev\pnpm-v22\bin'
New-Item -ItemType SymbolicLink -Path "D:\dev\pnpm" -Target "D:\dev\pnpm-v22"
```