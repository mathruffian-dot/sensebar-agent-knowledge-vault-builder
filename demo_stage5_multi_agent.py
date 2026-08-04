import os
import sys
import time
from colorama import init, Fore, Style

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

init(autoreset=True)

class Agent:
    def __init__(self, name: str, role: str, color: str):
        self.name = name
        self.role = role
        self.color = color

    def speak(self, message: str):
        print(f"{self.color}{Style.BRIGHT}[{self.name} - {self.role}]{Style.RESET_ALL} {message}")

def run_multi_agent_demo(topic: str = "设计一套 '用 Agent 学习 Agent' 的 1 小时体验课程"):
    print(f"{Fore.BLUE}{Style.BRIGHT}=== 🤖🤖 Stage 5: 多 Agent 协同系统 (Multi-Agent System) 演示 ==={Style.RESET_ALL}\n")
    print(f"{Fore.WHITE}{Style.BRIGHT}共同目标: {topic}{Style.RESET_ALL}\n")

    planner = Agent("PlannerAgent", "主控规划师", Fore.CYAN)
    researcher = Agent("ResearcherAgent", "知识库检索员", Fore.YELLOW)
    writer = Agent("WriterAgent", "教案撰写员", Fore.GREEN)

    # 步骤 1: Planner 拆解任务
    planner.speak(f"已接收任务：'{topic}'。拆解步骤：1. 检索 Clipping 逐字稿精华；2. 整理核心纲要；3. 生成课程大纲。")
    time.sleep(0.5)

    # 步骤 2: Researcher 检索
    researcher.speak("正在检索 Clipping/ 中的核心影片（EP01~EP05、AntiGravity 2.0、Claude Code...）")
    time.sleep(0.5)
    researcher.speak("检索完成！关键要点：1. ReAct 思考循环概念；2. 知识库三层架构；3. 动手手写 Agent 调试。")
    time.sleep(0.5)

    # 步骤 3: Writer 撰写教案
    writer.speak("接收知识要点，开始生成 1 小时体验课程大纲...")
    time.sleep(0.5)

    outline = """
    📌 【1 小时体验课程大纲：用 Agent 来学习 Agent】
    ---------------------------------------------------
    - 00:00 - 00:15 | 概念引入：什么是 Agent？ReAct (Thought-Action-Observation) 循环
    - 00:15 - 00:35 | 动手实操：在 d:/Antigravity_SenseBar 运行 simple_agent.py
    - 00:35 - 00:50 | 知识库检索：体验 Clipping/ 逐字稿 RAG 检索
    - 00:50 - 01:00 | 总结与 Q&A：三层 Obsidian 知识库构建策略
    ---------------------------------------------------
    """
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}🎉 多 Agent 协同完成结果：{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{outline}{Style.RESET_ALL}\n")

if __name__ == "__main__":
    run_multi_agent_demo()
