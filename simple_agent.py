import os
import re
import sys
from dotenv import load_dotenv
from colorama import init, Fore, Style

# 确保在 Windows 终端中 UTF-8 字符（中文与 Emoji）正确输出
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

from tools import TOOL_REGISTRY


# 初始化 colorama
init(autoreset=True)

# 载入环境变量
load_dotenv()

SYSTEM_PROMPT_TEMPLATE = """你是一个具备推理与工具调用能力的 ReAct (Reasoning & Action) AI Agent。
请严格按照以下格式回答问题与解决任务：

问题: 输入你需要解决的问题
Thought: 思考目前已知信息，并决定下一步采取的行动
Action: 调用的工具名称，必须是 [{tool_names}] 之一
Action Input: 传入工具的参数字符串
Observation: 工具返回的结果

（Thought/Action/Action Input/Observation 的过程可以重复多次）

Thought: 我现在知道了最终答案
Final Answer: 针对原始问题的最终回答

你可以使用的工具列表如下：
{tool_descriptions}

请开启你的回答：
"""

def format_tools_prompt():
    tool_names = ", ".join(TOOL_REGISTRY.keys())
    tool_descriptions = "\n".join(
        [f"- {name}: {info['description']}" for name, info in TOOL_REGISTRY.items()]
    )
    return tool_names, tool_descriptions

def run_react_loop(user_query: str, max_steps: int = 5):
    api_key = os.getenv("GEMINI_API_KEY")
    
    tool_names, tool_descriptions = format_tools_prompt()
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        tool_names=tool_names, tool_descriptions=tool_descriptions
    )
    
    prompt_history = system_prompt + f"\n问题: {user_query}\n"
    
    print(f"{Fore.BLUE}{Style.BRIGHT}=== 🚀 开启 ReAct Agent 思考循环 ==={Style.RESET_ALL}\n")
    print(f"{Fore.WHITE}{Style.BRIGHT}用户问题: {user_query}{Style.RESET_ALL}\n")

    if not api_key or api_key == "your_gemini_api_key_here":
        print(f"{Fore.YELLOW}⚠️  警告: 未检测到有效的 GEMINI_API_KEY。演示模拟 ReAct 循环：{Style.RESET_ALL}\n")
        # 模拟 1：如果在查 Clipping 或算术
        print(f"{Fore.YELLOW}Thought: 用户想要查询与 'AntiGravity' 相关的逐字稿内容，我需要调用 search_clipping 工具。{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Action: search_clipping{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Action Input: AntiGravity{Style.RESET_ALL}")
        
        obs = TOOL_REGISTRY["search_clipping"]["func"]("AntiGravity")
        print(f"{Fore.GREEN}Observation: {obs}{Style.RESET_ALL}\n")
        
        print(f"{Fore.YELLOW}Thought: 我已经获取到了相符的逐字稿片段，可以总结回答。{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Final Answer: 在 Clipping/ 目录中找到了包含 'AntiGravity' 的影片逐字稿（如 AntiGravity 2.0 测评与教学应用等）。请在 .env 中配置 GEMINI_API_KEY 以开启完整大模型智能推演。{Style.RESET_ALL}\n")
        return

    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        for step in range(1, max_steps + 1):
            print(f"{Fore.WHITE}{Style.DIM}--- [Step {step}] ---{Style.RESET_ALL}")
            response = model.generate_content(prompt_history)
            response_text = response.text.strip()
            
            # 解析输出
            print(f"{Fore.YELLOW}{response_text}{Style.RESET_ALL}")
            prompt_history += response_text + "\n"
            
            if "Final Answer:" in response_text:
                print(f"\n{Fore.MAGENTA}{Style.BRIGHT}=== 🎉 任务完成 ==={Style.RESET_ALL}")
                break
                
            # 正则匹配 Action 与 Action Input
            action_match = re.search(r"Action:\s*([^\n]+)", response_text)
            action_input_match = re.search(r"Action Input:\s*([^\n]+)", response_text)
            
            if action_match and action_input_match:
                action_name = action_match.group(1).strip()
                action_input = action_input_match.group(1).strip()
                
                if action_name in TOOL_REGISTRY:
                    tool_func = TOOL_REGISTRY[action_name]["func"]
                    observation = tool_func(action_input)
                    obs_str = f"Observation: {observation}"
                    print(f"{Fore.GREEN}{obs_str}{Style.RESET_ALL}\n")
                    prompt_history += obs_str + "\n"
                else:
                    obs_str = f"Observation: 错误，未找到名为 '{action_name}' 的工具。"
                    print(f"{Fore.RED}{obs_str}{Style.RESET_ALL}\n")
                    prompt_history += obs_str + "\n"
            else:
                # 若未匹配到标准 Action 格式且没有 Final Answer，防止卡死循环
                print(f"{Fore.RED}无法解析 Agent 输出中的 Action/Action Input，循环终止。{Style.RESET_ALL}")
                break

    except Exception as e:
        print(f"{Fore.RED}ReAct 循环运行出错: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "请问 Clipping 中有哪些关于 AntiGravity 的内容？"
    run_react_loop(query)
