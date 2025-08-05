# 桌面UI


## wails

## pakeplus

将网页秒变桌面应用的打包工具。这是一款基于 Rust 和 Tauri 构建的开源工具，能够将任意网页或前端项目（如 Vue、React 等）快速转换为轻量级的桌面应用和移动应用。它体积仅 5 MB，可通过 GitHub Actions 实现云端自动打包，无需复杂依赖，支持 macOS、Windows 和 Linux 平台。
https://github.com/Sjj1024/PakePlus

为什么这么小？晚上把这个demo 也做一下

先不搞这种，还要上传 github key..这不是送吗？

需要可以先走：
https://github.com/tw93/Pake/blob/main/README_CN.md

## tauri v2

https://v2.tauri.app/start/
```bash
pnpm create tauri-app
cd tauri-v2-demo
pnpm install
vi tauri-v2-demo\vite.config.ts
vi tauri-v2-demo\src-tauri\tauri.conf.json
把 1420改成11420 
pnpm tauri dev

```