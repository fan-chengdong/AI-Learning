#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_openai import OpenAI
from langchain.memory import ConversationBufferMemory

load_dotenv()

def search_web(query):
    """模拟网络搜索工具 - 当需要获取最新信息时使用"""
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
    """计算工具 - 用于数学计算"""
    try:
        result = eval(expression)
        return f"计算结果: {expression} = {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"

def create_agent():
    """创建并初始化 Agent"""
    
    tools = [
        Tool(
            name="WebSearch",
            func=search_web,
            description="当需要获取最新信息、天气、新闻或时间时使用此工具"
        ),
        Tool(
            name="Calculator",
            func=calculate,
            description="当需要进行数学计算时使用此工具，输入应该是一个数学表达式，如 '2+2' 或 '10*5'"
        )
    ]

    llm = OpenAI(
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY", "demo_key"),
        base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    )

    memory = ConversationBufferMemory(memory_key="chat_history")

    agent = initialize_agent(
        tools,
        llm,
        agent="conversational-react-description",
        memory=memory,
        verbose=True
    )
    
    return agent

def main():
    print("=" * 50)
    print("       LangChain Agent Demo")
    print("=" * 50)
    print("这是一个简单的 AI Agent 示例，包含以下工具：")
    print("  1. WebSearch - 网络搜索（获取天气、新闻等）")
    print("  2. Calculator - 计算器")
    print("\n输入 'exit' 或 'quit' 退出程序\n")

    agent = create_agent()
    
    while True:
        try:
            user_input = input("\n你: ").strip()
            
            if user_input.lower() in ['exit', 'quit', '退出']:
                print("再见！")
                break
                
            if not user_input:
                continue
                
            print("Agent 正在思考...")
            response = agent.run(user_input)
            print(f"\nAgent: {response}")
            
        except KeyboardInterrupt:
            print("\n再见！")
            break
        except Exception as e:
            print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()