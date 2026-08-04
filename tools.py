import os
import glob
import math
from datetime import datetime

def calculator(expression: str) -> str:
    """计算数学表达式，例如: '2 + 2' 或 '15 * 8'。"""
    try:
        # 只允许安全的数学符号与字符
        allowed_chars = set("0123456789+-*/(). %")
        if not set(expression).issubset(allowed_chars):
            return "错误: 表达式包含不安全字符。"
        result = eval(expression, {"__builtins__": None, "math": math})
        return str(result)
    except Exception as e:
        return f"计算出错: {str(e)}"

def search_clipping(query: str) -> str:
    """在 Clipping/ 逐字稿目录中搜索包含关键词的文件内容。"""
    try:
        clipping_dir = os.path.join(os.path.dirname(__file__), "Clipping")
        if not os.path.exists(clipping_dir):
            return "错误: Clipping 目录不存在。"
        
        matches = []
        md_files = glob.glob(os.path.join(clipping_dir, "*.md"))
        query_lower = query.lower()
        
        for filepath in md_files:
            filename = os.path.basename(filepath)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
                for line_idx, line in enumerate(lines, 1):
                    if query_lower in line.lower():
                        clean_line = line.strip()
                        matches.append(f"文件: {filename} (第 {line_idx} 行): {clean_line}")
                        if len(matches) >= 5: # 最多返回前 5 条符合的结果
                            break
            if len(matches) >= 5:
                break
                
        if not matches:
            return f"未在 Clipping/ 中找到与 '{query}' 相关的逐字稿内容。"
        return "\n".join(matches)
    except Exception as e:
        return f"检索出错: {str(e)}"

def get_system_time(input_str: str = "") -> str:
    """获取当前的系统时间。"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 工具注册表
TOOL_REGISTRY = {
    "calculator": {
        "func": calculator,
        "description": "计算数学表达式。输入参数为数学表达式字符串（如 '12 + 34'）。"
    },
    "search_clipping": {
        "func": search_clipping,
        "description": "搜索 Clipping/ 逐字稿库。输入参数为搜索关键词字符串。"
    },
    "get_system_time": {
        "func": get_system_time,
        "description": "获取当前系统时间。输入参数为空字符串即可。"
    }
}
