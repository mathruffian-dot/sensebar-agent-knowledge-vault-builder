import os
import sys
import json
from dotenv import load_dotenv
from colorama import init, Fore, Style

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

init(autoreset=True)
load_dotenv()

class ConversationMemory:
    def __init__(self, max_history: int = 4):
        self.history = []
        self.max_history = max_history

    def add_message(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def get_context(self) -> str:
        # 使用滑动窗口限制对话长度
        trimmed = self.history[-self.max_history:]
        context_str = ""
        for msg in trimmed:
            context_str += f"{msg['role'].upper()}: {msg['content']}\n"
        return context_str

    def get_summary(self) -> str:
        return f"已记录 {len(self.history)} 条对话（保留最新 {self.max_history} 条作为短期上下文）"

def run_memory_demo():
    print(f"{Fore.BLUE}{Style.BRIGHT}=== 🧠 Stage 3: Agent 记忆与状态管理 (Memory & State) 演示 ==={Style.RESET_ALL}\n")
    
    memory = ConversationMemory(max_history=4)
    
    dialogues = [
        ("user", "你好，我是三师爸，我平时主要在 YouTube 上分享 AI Agents 教学。"),
        ("assistant", "你好三师爸！很高兴认识你。我会记住你的身份以及你在 YouTube 上分享 AI Agents 教学的信息。"),
        ("user", "我最喜欢的 AI 工具包括 AntiGravity 和 Claude Code。"),
        ("assistant", "记下了！三师爸最喜欢的工具是 AntiGravity 和 Claude Code。"),
        ("user", "请问你还记得我是谁吗？我最喜欢的工具是什么？")
    ]

    print(f"{Fore.YELLOW}模拟多轮对话与 Agent 内存上下文演进：{Style.RESET_ALL}\n")

    for role, content in dialogues[:-1]:
        memory.add_message(role, content)
        print(f"{Fore.CYAN}[写入 Memory] {role.upper()}: {content}{Style.RESET_ALL}")

    print(f"\n{Fore.YELLOW}当前 Agent 读取到的短期记忆缓冲区 (Context Window)：{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Style.DIM}{memory.get_context()}{Style.RESET_ALL}")

    user_query = dialogues[-1][1]
    print(f"{Fore.WHITE}{Style.BRIGHT}最新提问: {user_query}{Style.RESET_ALL}\n")

    # 演示结果输出
    print(f"{Fore.GREEN}Agent 调取 Context 后推理回答：{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}Final Answer: 当然记得！你是三师爸，主要在 YouTube 分享 AI Agents 教学，最喜欢的 AI 工具是 AntiGravity 和 Claude Code。{Style.RESET_ALL}\n")

if __name__ == "__main__":
    run_memory_demo()
