# scripts/build_site.py

import os
import shutil
import sys
from generate_index import get_generated_index_html # 从 generate_index.py 导入函数

def build_site(output_dir):
    """
    构建静态站点，将所有必要文件复制到指定的输出目录，并生成 index.html。
    """
    print(f"Starting site build to '{output_dir}'...")

    # 1. 清理旧的构建目录 (如果存在)
    if os.path.exists(output_dir):
        print(f"  Removing existing directory: {output_dir}")
        shutil.rmtree(output_dir)

    # 2. 创建新的构建目录
    print(f"  Creating new directory: {output_dir}")
    os.makedirs(output_dir)

    # 3. 复制 'assets' 目录及其内容到输出目录
    assets_src = "assets"
    assets_dest = os.path.join(output_dir, "assets")
    if os.path.exists(assets_src):
        print(f"  Copying '{assets_src}' to '{assets_dest}'")
        shutil.copytree(assets_src, assets_dest)
    else:
        print(f"  Warning: Source directory '{assets_src}' not found. Skipping assets copy.")
        
    # 4. 复制 'docs' 目录下的所有语言子目录及其内容到输出目录
    # 例如：docs/zh/determinant -> dist/zh/determinant
    docs_src = "docs"
    if os.path.exists(docs_src):
        print(f"  Copying content from '{docs_src}' to '{output_dir}'")
        for item in os.listdir(docs_src):
            s = os.path.join(docs_src, item) # 源路径，例如 docs/zh 或 docs/index.html
            d = os.path.join(output_dir, item)   # 目标路径，例如 dist/zh 或 dist/index.html
            
            if os.path.isdir(s): # 如果是语言目录 (如 zh, en)
                print(f"    Copying language directory '{s}' to '{d}'")
                shutil.copytree(s, d)
            elif os.path.isfile(s): # 如果是 docs/index.html 文件
                print(f"    Copying file '{s}' to '{d}'")
                shutil.copy2(s, d) # copy2 preserves metadata

    else:
        print(f"  Warning: Source directory '{docs_src}' not found. No documentation will be copied.")

    # 5. 生成项目根目录的 index.html 文件并写入输出目录
    # 这个 index.html 应该作为网站的导航页，列出所有可用的语言和文章
    print(f"  Generating root index.html in '{output_dir}'")
    # 注意：get_generated_index_html 需要能处理多语言结构
    index_html_content = get_generated_index_html() 
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html_content)

    print("Site build complete successfully!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/build_site.py <output_directory>")
        print("Example: python scripts/build_site.py dist")
        sys.exit(1)

    output_directory = sys.argv[1]
    build_site(output_directory)