
# OpenClaw 模型及 API 配置指南

## 概述

本指南介绍如何手动修改 OpenClaw 的模型配置和 API 密钥，适用于需要自定义模型提供商或切换不同 AI 模型的场景。

---

## 📁 配置文件位置

OpenClaw 的主配置文件位于：

```
C:\Users\<你的用户名>\.openclaw\openclaw.json
```

替换 `<你的用户名>` 为你的 Windows 用户名。

---

## 📝 配置文件结构

配置文件包含两个核心部分：

### 1. 默认模型设置（agents 部分）

```json
"agents": {
  "defaults": {
    "workspace": "C:\\Users\\用户名\\.openclaw\\workspace",
    "models": {
      "提供商名/模型ID": {
        "alias": "显示名称"
      }
    },
    "model": {
      "primary": "提供商名/模型ID"
    }
  }
}
```

### 2. 提供商配置（models 部分）

```json
"models": {
  "mode": "merge",
  "providers": {
    "提供商名": {
      "baseUrl": "API端点地址",
      "api": "API类型",
      "apiKey": "你的API密钥",
      "models": [
        {
          "id": "模型ID",
          "name": "模型名称",
          "reasoning": false,
          "input": ["text", "image"],
          "cost": {
            "input": 0,
            "output": 0,
            "cacheRead": 0,
            "cacheWrite": 0
          },
          "contextWindow": 1000000,
          "maxTokens": 65536
        }
      ]
    }
  }
}
```

---

## 🔧 常见提供商配置示例

### 1. 阿里云 Qwen 模型

```json
"qwen": {
  "baseUrl": "https://dashscope.aliyuncs.com/compatible-mode/v1",
  "api": "openai-completions",
  "apiKey": "sk-xxxxxxxxxxxxxxxxxxxxxxxx",
  "models": [
    {
      "id": "qwen-plus",
      "name": "qwen-plus",
      "contextWindow": 1000000,
      "maxTokens": 65536
    }
  ]
}
```

**获取 API Key**: https://dashscope.console.aliyun.com/apiKey

### 2. Anthropic Claude 模型

```json
"anthropic": {
  "api": "anthropic-messages",
  "apiKey": "sk-ant-xxxxxxxxxxxxxxxxxxxxxxxx",
  "models": [
    {
      "id": "claude-3-5-sonnet-20240620",
      "name": "Claude 3.5 Sonnet",
      "contextWindow": 200000,
      "maxTokens": 8191
    }
  ]
}
```

**获取 API Key**: https://console.anthropic.com/settings/keys

### 3. OpenAI 模型

```json
"openai": {
  "api": "openai-completions",
  "apiKey": "sk-xxxxxxxxxxxxxxxxxxxxxxxx",
  "models": [
    {
      "id": "gpt-4o",
      "name": "GPT-4o",
      "contextWindow": 128000,
      "maxTokens": 4096
    }
  ]
}
```

**获取 API Key**: https://platform.openai.com/api-keys

### 4. 本地 Ollama 模型（无需 API Key）

```json
"ollama": {
  "api": "ollama",
  "baseUrl": "http://localhost:11434",
  "models": [
    {
      "id": "llama3",
      "name": "Llama 3",
      "contextWindow": 8192,
      "maxTokens": 2048
    }
  ]
}
```

**前提条件**: 需要先安装并运行 Ollama

---

## ✅ 配置修改步骤

### 步骤 1：关闭 OpenClaw

确保 OpenClaw 应用已完全关闭，避免配置文件被占用。

### 步骤 2：备份配置文件

```bash
copy "C:\Users\用户名\.openclaw\openclaw.json" "C:\Users\用户名\.openclaw\openclaw.json.bak"
```

### 步骤 3：编辑配置文件

使用文本编辑器（如 Notepad++、VS Code）打开配置文件。

### 步骤 4：修改配置

#### 修改默认模型
找到 `agents.defaults.models` 和 `agents.defaults.model.primary`：

```json
"models": {
  "qwen/qwen-plus": { "alias": "Qwen" }
},
"model": {
  "primary": "qwen/qwen-plus"
}
```

#### 添加提供商配置
在 `models.providers` 下添加新的提供商配置。

### 步骤 5：保存并重启

保存配置文件后，重新启动 OpenClaw 应用。

---

## ⚠️ 重要注意事项

### API 类型参考

| 提供商 | API 类型 | 说明 |
|--------|----------|------|
| OpenAI / Qwen | `openai-completions` | OpenAI 兼容接口 |
| Anthropic | `anthropic-messages` | Claude 专用接口 |
| Ollama | `ollama` | 本地模型接口 |

### 模型 ID 必须准确

- **Qwen**: `qwen-plus`, `qwen-max`
- **Claude**: `claude-3-5-sonnet-20240620`, `claude-3-opus-20240229`
- **OpenAI**: `gpt-4o`, `gpt-4-turbo`, `gpt-3.5-turbo`
- **Ollama**: `llama3`, `mistral`, `phi3`

### 配置模式说明

- **`mode: "merge"`**: 合并内置模型目录和用户自定义配置
- **`mode: "replace"`**: 仅使用用户自定义配置（推荐）

---

## 🐛 常见问题排查

### 问题 1：模型认证失败（401 错误）

**原因**: API Key 无效或未配置

**解决**:
1. 检查 `apiKey` 字段是否正确
2. 确认 API Key 未过期
3. 验证 API Key 已开通对应模型服务

### 问题 2：模型未找到（model_not_found）

**原因**: 模型 ID 不正确

**解决**:
1. 确认模型 ID 与提供商文档一致
2. 检查模型是否在提供商的可用模型列表中

### 问题 3：配置修改后未生效

**原因**: 未重启 OpenClaw 或配置文件格式错误

**解决**:
1. 确保完全关闭并重新启动 OpenClaw
2. 使用 `openclaw config validate` 检查配置格式

---

## 📌 推荐配置实践

1. **定期备份**：修改配置前先备份
2. **最小改动**：只修改必要的字段
3. **使用替换模式**：设置 `mode: "replace"` 避免内置模型干扰
4. **单一提供商**：一次只配置一个提供商，便于排查问题

---

## 📞 参考资源

- **OpenClaw 官方文档**: https://docs.openclaw.ai/
- **Dashscope API 文档**: https://help.aliyun.com/zh/dashscope/developer-reference/api-details
- **Anthropic API 文档**: https://docs.anthropic.com/claude/reference/getting-started-with-the-api

---

*文档版本: 1.0*
*最后更新: 2026年5月*
