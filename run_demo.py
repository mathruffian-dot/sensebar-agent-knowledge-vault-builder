import sys
import os
from colorama import init, Fore, Style

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

init(autoreset=True)

def print_banner():
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print("=" * 60)
    print("      🤖 AI Agent 核心机制演示控制台 (Demonstration Suite)")
    print("      SenseBar Agent Knowledge Vault Builder")
    print("=" * 60)
    print(f"{Style.RESET_ALL}")

def show_menu():
    print(f"{Fore.YELLOW}请选择欲观看的 AI Agent 阶段示范：{Style.RESET_ALL}\n")
    print("  [1] Stage 1: ReAct (Reasoning & Action) 思考循环 (simple_agent.py)")
    print("  [2] Stage 2: 原生 Function Calling 工具调用 (demo_stage2_function_calling.py)")
    print("  [3] Stage 3: Agent 记忆与状态管理 Memory (demo_stage3_memory.py)")
    print("  [4] Stage 4: 知识库 RAG (Clipping 逐字稿) 检索 (demo_stage4_rag.py)")
    print("  [5] Stage 5: 多 Agent 协同系统 Multi-Agent (demo_stage5_multi_agent.py)")
    print("  [A] 一键全套运行 (Run All Demos)")
    print("  [Q] 退出控制台 (Quit)")
    print()

def main():
    print_banner()

    # 如果有命令行参数直接运行指定序号
    if len(sys.argv) > 1:
        choice = sys.argv[1].upper()
    else:
        show_menu()
        choice = input(f"{Fore.GREEN}请输入选项 [1-5 / A / Q]: {Style.RESET_ALL}").strip().upper()

    print()

    if choice == "1":
        from simple_agent import run_react_loop
        run_react_loop("请问 Clipping 中有哪些关于 AntiGravity 的内容？")
    elif choice == "2":
        from demo_stage2_function_calling import run_function_calling_demo
        run_function_calling_demo()
    elif choice == "3":
        from demo_stage3_memory import run_memory_demo
        run_memory_demo()
    elif choice == "4":
        from demo_stage4_rag import run_rag_demo
        run_rag_demo()
    elif choice == "5":
        from demo_stage5_multi_agent import run_multi_agent_demo
        run_multi_agent_demo()
    elif choice == "A":
        print(f"{Fore.MAGENTA}=== 🚀 开始全套 AI Agent 阶段顺序演示 ==={Style.RESET_ALL}\n")
        
        from simple_agent import run_react_loop
        run_react_loop("请问 Clipping 中有哪些关于 AntiGravity 的内容？")
        print("\n" + "-" * 50 + "\n")
        
        from demo_stage2_function_calling import run_function_calling_demo
        run_function_calling_demo()
        print("\n" + "-" * 50 + "\n")

        from demo_stage3_memory import run_memory_demo
        run_memory_demo()
        print("\n" + "-" * 50 + "\n")

        from demo_stage4_rag import run_rag_demo
        run_rag_demo()
        print("\n" + "-" * 50 + "\n")

        from demo_stage5_multi_agent import run_multi_agent_demo
        run_multi_agent_demo()
    elif choice == "Q":
        print("感谢使用，演示结束！")
    else:
        print(f"{Fore.RED}无效选项，请输入 1-5, A 或 Q。{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
