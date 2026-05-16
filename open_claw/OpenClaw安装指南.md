# OpenClaw 安装指南（Windows E盘 Node.js 方式）

## 环境概述

- **操作系统**: Windows
- **安装路径**: `E:\nodejs_install\node-v22.17.0-win-x64`
- **Node.js 版本**: v22.17.0
- **npm 版本**: 10.9.2

---

## 第一部分：Node.js 安装（已完成）

### 1.1 下载 Node.js v22.17.0

从官网下载 Windows x64 版本：
- ZIP 包: https://nodejs.org/dist/v22.17.0/node-v22.17.0-win-x64.zip
- MSI 安装包: https://nodejs.org/dist/v22.17.0/node-v22.17.0-x64.msi

### 1.2 解压到 E 盘

```powershell
# 解压到 nodejs_install 目录
Expand-Archive -Path "node-v22.17.0-win-x64.zip" -DestinationPath "E:\nodejs_install"
```

### 1.3 目录结构

解压后可能存在嵌套目录，需整理：

```
原路径: E:\nodejs_install\node-v22.17.0-win-x64\node-v22.17.0-win-x64\node-v22.17.0-win-x64\
整理后: E:\nodejs_install\node-v22.17.0-win-x64\
```

正确目录应包含：
- `node.exe`
- `npm.cmd`
- `node_modules\`

---

## 第二部分：环境变量配置

### 2.1 配置用户环境变量

在 PowerShell 中运行：

```powershell
[Environment]::SetEnvironmentVariable(
    "Path",
    "E:\nodejs_install\node-v22.17.0-win-x64;E:\nodejs_install\node-v22.17.0-win-x64\node_modules\.bin;$([Environment]::GetEnvironmentVariable('Path', 'User'))",
    "User"
)
```

### 2.2 验证配置

打开新终端，运行：

```bash
node --version
# 应输出: v22.17.0

npm --version
# 应输出: 10.9.2
```

---

## 第三部分：OpenClaw 安装

### 3.1 安装命令

```bash
E:\nodejs_install\node-v22.17.0-win-x64\npm.cmd install -g openclaw
```

或先设置 PATH 后安装：

```powershell
$env:PATH = "E:\nodejs_install\node-v22.17.0-win-x64;$env:PATH"
npm.cmd install -g openclaw
```

### 3.2 跳过脚本安装（可选）

如果遇到预安装脚本错误，尝试：

```bash
npm.cmd install -g openclaw --ignore-scripts
```

### 3.3 验证安装

```bash
openclaw --version
# 或
npm.cmd list -g openclaw
```

---

## 第四部分：API Key 配置

### 4.1 设置 ANTHROPIC_API_KEY

OpenClaw 需要 Anthropic API Key 来运行。

在 PowerShell 中设置用户环境变量：

```powershell
[Environment]::SetEnvironmentVariable(
    "ANTHROPIC_API_KEY",
    "your-api-key-here",
    "User"
)
```

或使用 setx：

```bash
setx ANTHROPIC_API_KEY "your-api-key-here"
```

### 4.2 获取 API Key

1. 访问 [Anthropic Console](https://console.anthropic.com/)
2. 注册/登录账户
3. 在 API Keys 页面创建新密钥
4. 复制密钥并替换 `your-api-key-here`

---

## 第五部分：使用批处理文件安装（推荐）

### 5.1 创建安装脚本

在 `E:\nodejs_install\` 目录下创建 `install_openclaw.bat`：

```batch
@echo off
cd /d E:\nodejs_install\node-v22.17.0-win-x64

echo ========================================
echo    OpenClaw 安装脚本
echo ========================================
echo.

echo [1/3] 检查 Node.js 版本...
node --version

echo.
echo [2/3] 安装 OpenClaw...
call npm install -g openclaw

echo.
echo [3/3] 验证安装...
npm list -g openclaw --depth=0

echo.
echo ========================================
echo    安装完成！
echo ========================================
echo.
echo 请设置 ANTHROPIC_API_KEY 环境变量
echo.
pause
```

### 5.2 以管理员身份运行

1. 右键点击 `install_openclaw.bat`
2. 选择「以管理员身份运行」
3. 等待安装完成

---

## 第六部分：验证和使用

### 6.1 验证安装

在新终端窗口中运行：

```bash
openclaw --version
```

### 6.2 基本使用

```bash
# 启动 OpenClaw
openclaw

# 查看帮助
openclaw --help
```

### 6.3 首次配置

首次运行时，OpenClaw 会引导你完成配置：
1. 输入 Anthropic API Key
2. 选择主题和偏好设置
3. 开始使用

---

## 常见问题

### Q1: npm 命令找不到

**解决方案**：确保 PATH 环境变量已正确配置，或使用完整路径：

```bash
E:\nodejs_install\node-v22.17.0-win-x64\npm.cmd --version
```

### Q2: 安装时 EPERM 权限错误

**解决方案**：
1. 关闭杀毒软件
2. 以管理员身份运行终端
3. 清理后重试：

```powershell
Remove-Item -Path "E:\nodejs_install\node-v22.17.0-win-x64\node_modules\openclaw" -Recurse -Force
```

### Q3: node 不是内部命令

**解决方案**：重新配置 PATH 环境变量，并重启终端。

### Q4: OpenClaw 版本要求

OpenClaw 需要 **Node.js >= 22.12.0**，请确保使用的是 v22.17.0 或更高版本。

---

## 目录结构总览

```
E:\
└── nodejs_install\
    └── node-v22.17.0-win-x64\
        ├── node.exe
        ├── npm.cmd
        ├── node_modules\
        │   └── openclaw\
        │       ├── dist\
        │       │   ├── agents\
        │       │   ├── commands\
        │       │   ├── extensions\
        │       │   └── plugin-sdk\
        │       └── node_modules\
        └── install_openclaw.bat  (可选)
```

---

## 卸载步骤

如需卸载 OpenClaw：

```bash
npm uninstall -g openclaw
```

如需完全卸载 Node.js：

```powershell
Remove-Item -Path "E:\nodejs_install\node-v22.17.0-win-x64" -Recurse -Force
# 并从系统 PATH 中移除相关环境变量
```

---

*文档创建时间: 2025-05-16*
