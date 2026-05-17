# OpenClaw 配置过程记录

本文档用于记录 OpenClaw 项目的配置过程。

## 环境准备

- 操作系统：Linux/Windows/macOS
- 依赖工具：CMake, GCC/Clang/MSVC

## 配置步骤

### 1. 安装并启动服务

执行以下命令完成安装并启动守护进程：
openclaw onboard --install-daemon

```bash
C:\WINDOWS\system32>openclaw onboard --install-daemon

🦞 OpenClaw  2026.5.12 (f066dd2) — I keep secrets like a vault... unless you print them in debug logs again.

Windows detected - OpenClaw runs great on WSL2!
Native Windows might be trickier.
Quick setup: wsl --install (one command, one reboot)
Guide: https://docs.openclaw.ai/windows
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄░██░▄▄░██░▄▄▄██░▀██░██░▄▄▀██░████░▄▄▀██░███░██
██░███░██░▀▀░██░▄▄▄██░█░█░██░█████░████░▀▀░██░█░█░██
██░▀▀▀░██░█████░▀▀▀██░██▄░██░▀▀▄██░▀▀░█░██░██▄▀▄▀▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                  🦞 OPENCLAW 🦞

T  OpenClaw setup
|
o  Security disclaimer ----------------------------------------------------------------------+
|                                                                                            |
|  OpenClaw is a hobby project and still in beta. Expect sharp edges.                        |
|  By default, OpenClaw is a personal agent: one trusted operator boundary.                  |
|  This bot can read files and run actions if tools are enabled.                             |
|  A bad prompt can trick it into doing unsafe things.                                       |
|                                                                                            |
|  OpenClaw is not a hostile multi-tenant boundary by default.                               |
|  If multiple users can message one tool-enabled agent, they share that delegated tool      |
|  authority.                                                                                |
|                                                                                            |
|  If you’re not comfortable with security hardening and access control, don’t run           |
|  OpenClaw.                                                                                 |
|  Ask someone experienced to help before enabling tools or exposing it to the internet.     |
|                                                                                            |
|  Recommended baseline                                                                      |
|  - Pairing/allowlists + mention gating.                                                    |
|  - Multi-user/shared inbox: split trust boundaries (separate gateway/credentials, ideally  |
|    separate OS users/hosts).                                                               |
|  - Sandbox + least-privilege tools.                                                        |
|  - Shared inboxes: isolate DM sessions (session.dmScope: per-channel-peer) and keep tool   |
|    access minimal.                                                                         |
|  - Keep secrets out of the agent’s reachable filesystem.                                   |
|  - Use the strongest available model for any bot with tools or untrusted inboxes.          |
|                                                                                            |
|  Run regularly                                                                             |
|  openclaw security audit --deep                                                            |
|  openclaw security audit --fix                                                             |
|                                                                                            |
|  Learn more                                                                                |
|  - https://docs.openclaw.ai/gateway/security                                               |
|                                                                                            |
+--------------------------------------------------------------------------------------------+
|
o  I understand this is personal-by-default and shared/multi-user use requires lock-down. Continue?
|  Yes
|
o  Setup mode
|  QuickStart (recommended)
|
o  QuickStart -------------------------+
|                                      |
|  Gateway port: 18789                 |
|  Gateway bind: Loopback (127.0.0.1)  |
|  Gateway auth: Token (default)       |
|  Tailscale exposure: Off             |
|  Direct to chat channels.            |
|                                      |
+--------------------------------------+
|
*  Model/auth provider
|    Anthropic
|    Google
|    OpenAI
|    xAI (Grok)
|  > More…
|    Skip for now
```

选择模型
```bash
o  Model/auth provider
|  Qwen Cloud
|
o  Qwen Cloud auth method
|  Coding Plan API Key for China (subscription)
|
o  Qwen Cloud Coding Plan (China) -----------------------------+
|                                                              |
|  Manage API keys: https://home.qwencloud.com/api-keys        |
|  Docs: https://docs.qwencloud.com/                           |
|  Endpoint: coding.dashscope.aliyuncs.com                     |
|  Models: qwen3.5-plus, glm-5, kimi-k2.5, MiniMax-M2.5, etc.  |
|                                                              |
+--------------------------------------------------------------+
|
*  Enter Qwen Cloud Coding Plan API key (China)

```

qiwen3.5-plus
https://home.qwencloud.com/api-keys?accounttraceid=57b7079079ad4531ae54cd2f0e497797sklc&cspNonce=wgmC1CBnlq

```bash
o  Model configured -----------------------+
|                                          |
|  Default model set to qwen/qwen3.5-plus  |
|                                          |
+------------------------------------------+
|
o  Default model
|  Keep current (qwen/qwen3.5-plus)
|
o  How channels work -----------------------------------------------------------------------+
|                                                                                           |
|  Inbound DM safety defaults to pairing: unknown senders get a pairing code first.         |
|  Approve with: openclaw pairing approve <channel> <code>                                  |
|  Open/public DMs require dmPolicy="open" plus allowFrom=["*"].                            |
|  For multi-user DMs, isolate sessions with: openclaw config set session.dmScope           |
|  "per-channel-peer" (or "per-account-channel-peer" for multi-account channels).           |
|  Docs: channels/pairing                                                                   |
|                                                                                           |
|  Feishu: 飞书/Lark enterprise messaging with doc/wiki/drive tools.                        |
|  WeCom: Enterprise messaging and documents, scheduling, task tools.                       |
|  Google Chat: Google Workspace Chat app with HTTP webhook.                                |
|  Nostr: Decentralized protocol; encrypted DMs via NIP-04.                                 |
|  Microsoft Teams: Teams SDK; enterprise support.                                          |
|  Mattermost: self-hosted Slack-style chat; install the plugin to enable.                  |
|  Nextcloud Talk: Self-hosted chat via Nextcloud Talk webhook bots.                        |
|  Matrix: open protocol; install the plugin to enable.                                     |
|  LINE: LINE Messaging API webhook bot.                                                    |
|  Weixin: Personal WeChat messaging via QR-code login.                                     |
|  Zalo: Vietnam-focused messaging platform with Bot API.                                   |
|  ClickClack: self-hosted chat via first-class ClickClack bot tokens.                      |
|  Yuanbao: Tencent Yuanbao AI assistant conversation channel.                              |
|  Zalo Personal: Zalo personal account via QR code login.                                  |
|  Synology Chat: Connect your Synology NAS Chat to OpenClaw with full agent capabilities.  |
|  Tlon: decentralized messaging on Urbit; install the plugin to enable.                    |
|  Discord: very well supported right now.                                                  |
|  iMessage: Local iMessage/SMS through the imsg bridge, including private API message      |
|  actions when enabled.                                                                    |
|  IRC: classic IRC networks with DM/channel routing and pairing controls.                  |
|  QQ Bot: connect to QQ via official QQ Bot API with group chat and direct message         |
|  support.                                                                                 |
|  Signal: signal-cli linked device; more setup (David Reagans: "Hop on Discord.").         |
|  Slack: supported (Socket Mode).                                                          |
|  Telegram: simplest way to get started — register a bot with @BotFather and get going.    |
|  Twitch: Twitch chat integration                                                          |
|  WhatsApp: works with your own number; recommend a separate phone + eSIM.                 |
|                                                                                           |
+-------------------------------------------------------------------------------------------+



```

安装clawhub

```bash
o  Search provider
|  Skip for now
|
o  Skills status -------------+
|                             |
|  Eligible: 7                |
|  Missing requirements: 37   |
|  Unsupported on this OS: 8  |
|  Blocked by allowlist: 0    |
|                             |
+-----------------------------+
|
o  Configure skills now? (recommended)
|  Yes
|
*  Install missing skill dependencies
|  [ ] Skip for now
|  [ ] 🔐 1password
|  [ ] 📰 blogwatcher
|  [ ] 🫐 blucli
|  [ ] 📸 camsnap
|  [+] 🧩 clawhub  (Search, install, update, sync, or publish agent skills with the ClawHub CLI and registry.…)
|  [ ] 🛌 eightctl
|  [ ] ✨ gemini
|  [ ] 🧩 gh-issues
|  [ ] 🧲 gifgrep
|  [ ] 🐙 github
|  [ ] 🎮 gog
|  [ ] 📍 goplaces
|  [ ] 📧 himalaya
|  [ ] 📦 mcporter
|  [ ] 📄 nano-pdf
|  [ ] 💎 obsidian
|  [ ] 🎤 openai-whisper
|  [ ] 💡 openhue
|  [ ] 🧿 oracle
|  [ ] 🛵 ordercli
|  [ ] 🔊 sag
|  [ ] 📜 session-logs
|  [ ] 🌊 songsee
|  [ ] 🔊 sonoscli
|  [ ] 🧾 summarize
|  [ ] 📋 trello
|  [ ] 🎬 video-frames
|  [ ] 📱 wacli
|  [ ] 🐦 xurl
```

```bash
o  Configure skills now? (recommended)
|  Yes
|
o  Install missing skill dependencies
|  🧩 clawhub
|
o  Preferred node manager for skill installs
|  npm
```

` npm install -g clawhub ` 


安装gateway
```bash
Enable hooks?
|  Skip for now
Config overwrite: C:\Users\fanchengdong\.openclaw\openclaw.json (sha256 9277fa5c889f2cb0a536d57e9caf9518cf156369c4d4ee400603703b34295bcd -> e9cd94620f8d1966df4641780f44d10b20430764c6f9a92c168829e05b4429a4, backup=C:\Users\fanchengdong\.openclaw\openclaw.json.bak)
|
o  Gateway service runtime --------------------------------------------+
|                                                                      |
|  QuickStart uses Node for the Gateway service (stable + supported).  |
|                                                                      |
+----------------------------------------------------------------------+
|
o  Installing Gateway service….
Installed Scheduled Task: OpenClaw Gateway
Task script: C:\Users\fanchengdong\.openclaw\gateway.cmd
o  Gateway service installed.
Health check failed: connect ECONNREFUSED 127.0.0.1:18789
|
o  Health check help --------------------------------+
|                                                    |
|  Docs:                                             |
|  https://docs.openclaw.ai/gateway/health           |
|  https://docs.openclaw.ai/gateway/troubleshooting  |
|                                                    |
+----------------------------------------------------+
|
o  Optional apps ------------------------+
|                                        |
|  Add nodes for extra features:         |
|  - macOS app (system + notifications)  |
|  - iOS app (camera/canvas)             |
|  - Android app (camera/canvas)         |
|                                        |
+----------------------------------------+
|
o  Control UI ---------------------------------------------------------------------+
|                                                                                  |
|  Web UI: http://127.0.0.1:18789/                                                 |
|  Web UI (with token):                                                            |
|  http://127.0.0.1:18789/#token=dde3a44f68ef00a12678096e3f36cc64e2aa4e051e253de2  |
|  Gateway WS: ws://127.0.0.1:18789                                                |
|  Gateway: not detected (connect ECONNREFUSED 127.0.0.1:18789)                    |
|  Docs: https://docs.openclaw.ai/web/control-ui                                   |
|                                                                                  |
+----------------------------------------------------------------------------------+
|
o  Hatch your agent ---------------------------------------------------+
|                                                                      |
|  Your workspace is ready.                                            |
|  The first Terminal chat run will send: "Wake up, my friend!"        |
|  Edit BOOTSTRAP.md later to change how the agent introduces itself.  |
|                                                                      |
+----------------------------------------------------------------------+
|
*  How do you want to hatch your agent?
|  > Hatch in Terminal (recommended)
|    Hatch later
```

http://127.0.0.1:18789/#token=dde3a44f68ef00a12678096e3f36cc64e2aa4e051e253de2

阿里
https://bailian.console.aliyun.com/cn-beijing?spm=a2c4g.11186623.0.0.6095785bV0PWpW&tab=model&accounttraceid=0f67d0a62a2e4a71acdf3fef48c16556vsvv#/api-key

minMax：
sk-api-cia_Q6rqVji6FyLHuj3A_z8IKMWMk5OgpQIp_t_Wpn6lUxxqwerTXqN8Xdj3OpXO4Ms_sEfW3p3CXZl06i3ZpdogOYPy-NZfOOaEAAFcFVr7BnpaUH_QO0E


## 启动命令
1、重新配置openclaw
`openclaw onboard --install-daemon`

2、启动gateway
`openclaw gateway run`
3、启动dashboard webui
`openclaw dashboard`
4、启动tui
`openclaw tui`


sk-efc4565804754ee5abfcf3bb3e09f3a6