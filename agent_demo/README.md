# LangChain Agent Demo

这是一个简单的 AI Agent 演示项目，展示了如何使用 LangChain 构建智能代理。

## 项目结构

```
agent_demo/
├── requirements.txt          # Python 依赖
├── .env.example             # 环境变量示例
├── simple_agent.py          # 完整的 Agent 实现（需要 API Key）
├── simple_agent_demo.py     # 演示版本（无需 API Key）
└── README.md                # 本文件
```

## 快速开始

### 方式一：运行演示版本（无需 API Key）

```bash
cd agent_demo
python simple_agent_demo.py
```

这个版本会模拟 Agent 的工作流程，展示 Agent 如何思考和使用工具。

### 方式二：运行完整版本

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 配置环境变量：
```bash
copy .env.example .env
# 编辑 .env 文件，填入你的 OpenAI API Key
```

3. 运行 Agent：
```bash
python simple_agent.py
```

## Agent 功能

### 内置工具

| 工具 | 描述 |
|------|------|
| WebSearch | 模拟网络搜索（获取天气、新闻、时间等） |
| Calculator | 数学计算器 |

### 特性

- 对话记忆功能
- 自动工具选择
- 链式推理（ReAct 模式）
- 友好的命令行界面

## 工作原理

```
用户输入
    ↓
[LLM 推理] 理解问题 → 选择工具
    ↓
[工具执行] 调用相应工具
    ↓
[结果处理] 工具返回结果
    ↓
[最终回答] 生成用户友好的回复
```

## 使用示例

### 示例对话

```
你: 今天天气怎么样？
Agent 正在思考...
[使用 WebSearch 工具]
Agent: 今天天气晴朗，温度 25°C

你: 123 * 456 等于多少？
Agent 正在思考...
[使用 Calculator 工具]
Agent: 计算结果: 123 * 456 = 56088

你: 刚才问了什么问题？
Agent 正在思考...
Agent: 你刚才问了今天的天气怎么样
```

## 扩展开发

### 添加新工具

在 `simple_agent.py` 中添加新的工具函数：

```python
def my_custom_tool(input_str):
    """你的工具描述"""
    result = process(input_str)
    return result
```

然后在 tools 列表中注册：

```python
tools = [
    # ... 现有工具
    Tool(
        name="MyTool",
        func=my_custom_tool,
        description="什么时候使用这个工具"
    )
]
```

### 修改 Agent 类型

可以尝试不同的 Agent 类型：

```python
agent = initialize_agent(
    tools, llm,
    agent="zero-shot-react-description",  # 或其他类型
    # agent="conversational-react-description",
    # agent="react-docstore",
    verbose=True
)
```

## 学习资源

- [LangChain 官方文档](https://python.langchain.com/)
- [OpenAI API 文档](https://platform.openai.com/docs/)
- [Agent 设计模式](https://www.promptingguide.ai/techniques/react)

## 常见问题

### Q: 没有 OpenAI API Key 怎么办？
A: 使用 `simple_agent_demo.py` 演示版本，无需 API Key 即可体验 Agent 工作流程。

### Q: 如何使用其他 LLM？
A: 修改 `simple_agent.py` 中的 LLM 初始化代码，支持 Claude、Gemini 等多种模型。

### Q: 可以添加更多工具吗？
A: 当然！参考上述"扩展开发"部分，添加任意数量的工具。

## 许可证

MIT License