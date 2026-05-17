
# 安装
``` bash
winget install Anthropic.Claudecode
```

# 启动claude_code
``` bash
 claude
```

启动报错
Unable to connect to Anthropic services Failed to connect to api.anthropic.claude.ai
解决方法：
    编辑或新增 ~/.claude.json（Windows 路径：C:\Users\<用户名>\.claude.json），将 hasCompletedOnboarding 设置为 true，跳过 Anthropic 官方登录验证。

``` json
{
  "firstStartTime": "2026-05-17T09:08:44.192Z",
  "opusProMigrationComplete": true,
  "sonnet1m45MigrationComplete": true,
  "seenNotifications": {},
  "migrationVersion": 13,
  "userID": "5ebbd31ce97922e46c9f5d31ab9c8c8201ac44bb047f61857a03b4bd8e45db72",
  "changelogLastFetched": 1779008925329,
  "hasCompletedOnboarding": true
}
```
# 模型配置

``` bash
setx ANTHROPIC_API_KEY "sk-578ed81f82b2487eb6a9fe8e56ac82a8"

setx ANTHROPIC_BASE_URL "https://dashscope.aliyuncs.com/apps/anthropic"

setx ANTHROPIC_MODEL "glm-5"
```
阿里百炼配置
https://bailian.console.aliyun.com/cn-beijing/?spm=5176.29619931.J_SEsSjsNv72yRuRFS2VknO.2.100f10d7IWAIBY&tab=model#/api-key

配置路径：
C:\Users\<用户名>\.claude\settings.json

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "sk-578ed81f82b2487eb6a9fe8e56ac82a8",
    "ANTHROPIC_BASE_URL": "https://dashscope.aliyuncs.com/apps/anthropic",
    "CLAUDE_MODEL": "glm-5"
  },
  "permissions": {
    "allow": [],
    "deny": []
  },
  "version": 1,
  "profile": "deepseek",
  "effortLevel": "medium"
}
```
