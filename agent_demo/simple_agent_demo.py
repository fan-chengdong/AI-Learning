#!/usr/bin/env python3
import time

print("=" * 50)
print("       LangChain Agent Demo (无API版)")
print("=" * 50)
print("\n这个演示展示了 Agent 的工作原理：")
print("1. 理解用户输入")
print("2. 决定使用哪个工具")
print("3. 执行工具并获取结果")
print("4. 生成最终回答\n")

def search_web(query):
    """模拟网络搜索工具"""
    print(f"\n  [工具调用] WebSearch: {query}")
    time.sleep(1)
    search_results = {
        "天气": "今天天气晴朗，温度 25°C",
        "新闻": "最新科技新闻：AI 技术取得重大突破",
        "时间": "当前时间：2026年5月16日",
    }
    
    for keyword, result in search_results.items():
        if keyword in query:
            return f"搜索结果: {result}"
    
    return f"搜索结果: 未找到关于 '{query}' 的信息"

def calculate(expression):
    """模拟计算工具"""
    print(f"\n  [工具调用] Calculator: {expression}")
    time.sleep(1)
    try:
        result = eval(expression)
        return f"计算结果: {expression} = {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"

def mock_llm_decide(query):
    """模拟 LLM 的决策过程"""
    print(f"\n  [LLM 推理] 分析问题: {query}")
    time.sleep(0.5)
    
    if any(keyword in query for keyword in ["天气", "新闻", "时间", "搜索"]):
        return "WebSearch"
    elif any(char in query for char in ["+", "-", "*", "/"]):
        return "Calculator"
    else:
        return "直接回答"

def mock_agent(query):
    """模拟 Agent 的完整工作流程"""
    print("-" * 50)
    print(f"用户提问: {query}")
    
    decision = mock_llm_decide(query)
    
    if decision == "WebSearch":
        result = search_web(query)
    elif decision == "Calculator":
        result = calculate(query)
    else:
        result = "这是一个直接回答，不需要使用工具。"
    
    print(f"\n  [最终回答] {result}")
    print("-" * 50)
    return result

def main():
    demo_questions = [
        "今天天气怎么样？",
        "123 * 456 等于多少？",
        "有什么最新新闻？",
    ]
    
    print("运行示例问题:\n")
    for i, question in enumerate(demo_questions, 1):
        print(f"\n{'='*50}")
        print(f"示例 {i}: {question}")
        mock_agent(question)
        time.sleep(1)
    
    print("\n" + "="*50)
    print("演示完成！")
    print("="*50)
    print("\n提示：")
    print("- 要运行真实的 Agent，请安装依赖后运行 simple_agent.py")
    print("- 配置 .env 文件中的 API Key")
    print("- 查看 README.md 获取详细说明")

if __name__ == "__main__":
    main()