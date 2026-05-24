# 安装skills

## 安装 claude-hud
``` bash
/plugin marketplace add jarrodwatts/claude-hud

/plugin install claude-hud

/reload-plugins

/claude-hud:setup
```

### 1 报错（SSH Host Key 验证失败）
```
Error: Failed to clone marketplace repository: SSH host key is not in your known_hosts file.
```

**解决方案：**

#### 方案 A：配置 Git 使用 HTTPS 替代 SSH（推荐）
```powershell
git config --global url."https://github.com/".insteadOf "git@github.com:"
```
这会自动将所有 `git@github.com:` 的仓库地址转换为 `https://github.com/`，避免 SSH 密钥验证问题。

#### 方案 B：添加 GitHub SSH Host Key
```powershell
# 创建 known_hosts 文件（如果不存在）
if (-not (Test-Path "~\.ssh\known_hosts")) {
    New-Item -ItemType File -Path "~/.ssh/known_hosts"
}
# 添加 GitHub host key
ssh-keyscan github.com >> ~/.ssh/known_hosts 2>$null
```

---

### 2 报错（HTTPS 连接超时）
```
Error: Failed to clone marketplace repository:
fatal: unable to access 'https://github.com/jarrodwatts/claude-hud.git/':
Failed to connect to github.com port 443: Timed out
```

**问题诊断：**
| 测试项 | 结果 |
|--------|------|
| DNS 解析 | ✅ 正常 |
| TCP 443 端口 | ❌ 连接超时/被阻断 |
| 代理设置 | 未配置 |

**解决方案：**

#### 方案 A：配置代理（如果你有代理）
```powershell
# 设置 HTTP 代理
git config --global http.proxy http://127.0.0.1:7890
# 设置 HTTPS 代理
git config --global https.proxy http://127.0.0.1:7890
```
将 `http://127.0.0.1:7890` 替换为你的实际代理地址。

#### 方案 B：使用 GitHub 镜像源
```powershell
# 配置镜像源
git config --global url."https://hub.fastgit.xyz/".insteadOf "https://github.com/"
```
或使用 `gitclone.com` 镜像：
```powershell
git config --global url."https://gitclone.com/github.com/".insteadOf "https://github.com/"
```

#### 方案 C：手动下载安装
1. 在有网络的设备上访问：`https://github.com/jarrodwatts/claude-hud`
2. 点击 "Code" -> "Download ZIP"
3. 解压到 `C:\Users\fanchengdong\.claude\plugins\marketplaces\jarrodwatts-claude-hud`


## 安装方式

### 1 手动安装
‌手动复制文件夹‌
下载 Skill 文件夹（需包含 SKILL.md 文件）。
1. 全局 Skill 放 ~/.claude/skills/（所有项目可用）
`C:\Users\fanchengdong\.claude\plugins\marketplaces\jarrodwatts-claude-hud`
`C:\Users\fanchengdong\.claude\skills\claude-hud`
2. 项目 Skill 放项目目录下的 skills/（仅项目内可用）
`<current_pro_dir>\.claude\skills\claude-hud`

``` bash
/plugin marketplace add jarrodwatts/claude-hud

/claude-hud:setup
```

### 2 完整插件安装 plugin
1. 官方市场，直接安装
``` bash
/plugin install xxx
```
2. 第三方市场，需要添加市场源 再安装

添加市场源：/plugin marketplace add <市场地址>
安装插件：/plugin install <插件名>@<市场名>
例如：/plugin install superpowers@superpowers-marketplace‌‌‌
‌手动复制文件夹‌
下载 Skill 文件夹（需包含 SKILL.md 文件）。
``` bash
/plugin marketplace add xxx
/plugin install xxx
```

### 3 自动安装（推荐）
‌npx 命令行安装‌
执行命令：npx skills add <github 仓库地址> -g -y
-g 参数表示全局安装到用户目录。‌‌‌
