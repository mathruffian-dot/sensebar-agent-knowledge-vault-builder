import os
import sys
import json
from dotenv import load_dotenv
from colorama import init, Fore, Style

# 确保在 Windows 终端中 UTF-8 字符正确输出
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

init(autoreset=True)
load_dotenv()

def get_weather(location: str, unit: str = "celsius") -> str:
    """获取指定城市的实时天气预报。
    
    Args:
        location: 城市名称，例如 'Taipei' 或 'Tokyo'
        unit: 温度单位 'celsius' 或 'fahrenheit'
    """
    mock_data = {
        "taipei": "台北目前天气晴朗，气温 28°C，湿度 65%",
        "tokyo": "东京目前多云，气温 18°C，湿度 50%",
        "new york": "纽约目前有小雨，气温 15°C，湿度 80%"
    }
    loc_key = location.lower()
    return mock_data.get(loc_key, f"{location} 目前天气宜人，气温 25°C。")

def run_function_calling_demo(user_query: str = "请问台北现在的天气怎么样？"):
    print(f"{Fore.BLUE}{Style.BRIGHT}=== 🛠️ Stage 2: 原生 Function Calling 机制演示 ==={Style.RESET_ALL}\n")
    print(f"{Fore.WHITE}{Style.BRIGHT}用户问题: {user_query}{Style.RESET_ALL}\n")

    api_key = os.getenv("GEMINI_API_KEY")

    # 简化的 JSON Schema 演示
    schema_demo = {
        "name": "get_weather",
        "description": "获取指定城市的实时天气预报",
        "parameters": {
            "type": "OBJECT",
            "properties": {
                "location": {"type": "STRING", "description": "城市名称"},
                "unit": {"type": "STRING", "description": "温度单位 (celsius/fahrenheit)"}
            },
            "required": ["location"]
        }
    }

    print(f"{Fore.YELLOW}[1] 注册函数工具，自动转换为 JSON Schema 标准规范：{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{json.dumps(schema_demo, ensure_ascii=False, indent=2)}{Style.RESET_ALL}\n")

    if not api_key or api_key == "your_gemini_api_key_here":
        print(f"{Fore.YELLOW}⚠️  未检测到有效的 GEMINI_API_KEY。开启 Function Calling 原理模拟演示：{Style.RESET_ALL}\n")
        print(f"{Fore.YELLOW}[2] 模型识别意图，生成原生 Tool Call 请求：{Style.RESET_ALL}")
        call_payload = {"name": "get_weather", "args": {"location": "Taipei", "unit": "celsius"}}
        print(f"{Fore.CYAN}{json.dumps(call_payload, ensure_ascii=False, indent=2)}{Style.RESET_ALL}\n")

        print(f"{Fore.YELLOW}[3] 本地控制器接收 Tool Call 请求，执行对应 Python 代码：{Style.RESET_ALL}")
        result = get_weather(**call_payload["args"])
        print(f"{Fore.GREEN}执行结果 Observation: {result}{Style.RESET_ALL}\n")

        print(f"{Fore.YELLOW}[4] 将执行结果喂回模型，整合生成最终人类语言回答：{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Final Answer: 台北目前天气晴朗，气温 28°C，非常舒适。{Style.RESET_ALL}\n")
        return

    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash", tools=[get_weather])
        
        chat = model.start_chat(enable_automatic_function_calling=True)
        response = chat.send_message(user_query)
        
        print(f"{Fore.MAGENTA}{Style.BRIGHT}模型自动感知并完成 Function Calling，最终回答：{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{response.text}{Style.RESET_ALL}\n")
    except Exception as e:
        print(f"{Fore.RED}Function Calling 运行失败: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    run_function_calling_demo()
