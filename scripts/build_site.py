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

    # 4. 复制 'articles' 目录下的所有文章子目录到输出目录的根部
    # 例如：articles/field_space -> dist/field_space
    articles_src = "articles"
    if os.path.exists(articles_src):
        print(f"  Copying article folders from '{articles_src}' to '{output_dir}'")
        for item in os.listdir(articles_src):
            s = os.path.join(articles_src, item) # 源路径，例如 articles/field_space
            d = os.path.join(output_dir, item)   # 目标路径，例如 dist/field_space
            if os.path.isdir(s):
                print(f"    Copying '{s}' to '{d}'")
                shutil.copytree(s, d)
            else:
                print(f"    Skipping non-directory item: '{s}'")
    else:
        print(f"  Warning: Source directory '{articles_src}' not found. No articles will be copied.")

    # 5. 生成 index.html 文件并写入输出目录
    print(f"  Generating index.html in '{output_dir}'")
    index_html_content = get_generated_index_html() # 调用 generate_index.py 中的函数
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html_content)

    print("Site build complete successfully!")

if __name__ == "__main__":
    # 检查是否提供了输出目录参数
    if len(sys.argv) < 2:
        print("Usage: python scripts/build_site.py <output_directory>")
        print("Example: python scripts/build_site.py dist")
        sys.exit(1) # 退出并返回错误码

    output_directory = sys.argv[1]
    build_site(output_directory)