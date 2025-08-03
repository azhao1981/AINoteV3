# Node.js 与 pnpm 配置指南

## npm 配置

```bash
npm config get registry
npm config set registry=http://registry.npm.taobao.org
npm install -g pnpm
```

## pnpm 配置

```bash
# 设置存储目录
pnpm config set store-dir 'D:\dev\pnpm\store'

# 设置全局 bin 目录
pnpm config set global-bin-dir "D:\dev\pnpm-v22\bin"

# 设置 pnpm_home 目录
pnpm config set pnpm_home "D:\dev\pnpm-v22"

# 查看配置
pnpm config get global-bin-dir
pnpm config get pnpm_home
```

## 环境变量配置

```bash
sysdm.cpl
path
D:\dev\pnpm-v22\bin
$env:PATH
```

## Qwen Code 安装

在 Windows 下的体验好过 cc:

```bash
npm i -g @qwen-code/qwen-code

pnpm i -g @qwen-code/qwen-code
```

## 符号链接设置

```bash
# 删除旧链接
Remove-Item "D:\dev\nodejs" -Force -Recurse

# 创建 Node.js 符号链接
New-Item -ItemType SymbolicLink -Path "D:\dev\nodejs" -Target "D:\dev\node-v24.4.1-win-x64"
New-Item -ItemType SymbolicLink -Path "D:\dev\nodejs" -Target "D:\dev\node-v22.18.0-win-x64"

# 创建 pnpm 目录和符号链接
mkdir 'd:\dev\pnpm-v22'
mkdir 'd:\dev\pnpm-v22\bin'
New-Item -ItemType SymbolicLink -Path "D:\dev\pnpm" -Target "D:\dev\pnpm-v22"
```