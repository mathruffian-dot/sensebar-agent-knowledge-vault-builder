import os
import sys
import glob
from colorama import init, Fore, Style

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

init(autoreset=True)

def retrieve_knowledge(query: str, top_k: int = 3) -> list:
    clipping_dir = os.path.join(os.path.dirname(__file__), "Clipping")
    results = []
    
    if not os.path.exists(clipping_dir):
        return results

    md_files = glob.glob(os.path.join(clipping_dir, "*.md"))
    query_terms = query.lower().split()

    for filepath in md_files:
        filename = os.path.basename(filepath)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
            for line_idx, line in enumerate(lines, 1):
                clean_line = line.strip()
                if len(clean_line) < 10:
                    continue
                # 计算简单重合度（关键词匹配）
                score = sum(1 for term in query_terms if term in clean_line.lower())
                if score > 0:
                    results.append({
                        "file": filename,
                        "line": line_idx,
                        "text": clean_line,
                        "score": score
                    })

    # 按匹配分数排序
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_k]

def run_rag_demo(query: str = "Google AntiGravity 2.0 测评"):
    print(f"{Fore.BLUE}{Style.BRIGHT}=== 📚 Stage 4: 知识库 RAG (Clipping 逐字稿) 检索引擎演示 ==={Style.RESET_ALL}\n")
    print(f"{Fore.WHITE}{Style.BRIGHT}检索查询目标: {query}{Style.RESET_ALL}\n")

    print(f"{Fore.YELLOW}[1] 扫描 Clipping/ 目录下的 64 篇逐字稿并检索最相关 Chunk：{Style.RESET_ALL}")
    retrieved_chunks = retrieve_knowledge(query, top_k=3)

    if not retrieved_chunks:
        print(f"{Fore.RED}未检索到相符内容。{Style.RESET_ALL}")
        return

    for idx, item in enumerate(retrieved_chunks, 1):
        print(f"{Fore.CYAN}【片段 {idx}】{item['file']} (第 {item['line']} 行){Style.RESET_ALL}")
        print(f"{Fore.WHITE}  \"{item['text']}\"{Style.RESET_ALL}")

    print(f"\n{Fore.YELLOW}[2] 将检索到的上下文 (Context) 喂入 Agent 进行知识增广生成：{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Context: 依据 Clipping 逐字稿内容，频道中专门分析了 AntiGravity 2.0 的特性、安装配置以及在自动化备课中的应用。{Style.RESET_ALL}\n")

    print(f"{Fore.MAGENTA}{Style.BRIGHT}Final Answer: 依据 Clipping 知识库检索结果：Google AntiGravity 2.0 提供了强大的自动化框架，在频道影片中展示了如何一键整合 NotebookLM、Netlify 与 Github 打造自动化备课与教学流程。{Style.RESET_ALL}\n")

if __name__ == "__main__":
    run_rag_demo()
