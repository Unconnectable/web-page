# scripts/generate_index.py

import os

def get_generated_index_html():
    articles_dir = "articles" # 假设此脚本从项目根目录运行，因此直接查找 "articles"

    article_folders = []
    # 检查 "articles" 目录是否存在
    if os.path.exists(articles_dir):
        # 筛选出 "articles" 目录下的所有文件夹
        article_folders = [f for f in os.listdir(articles_dir) if os.path.isdir(os.path.join(articles_dir, f))]
    else:
        print(f"Warning: Directory '{articles_dir}' not found. No articles will be listed in index.html.")

    links = ""
    for folder in sorted(article_folders): # 排序一下，让列表更整齐
        html_file = None
        current_article_path = os.path.join(articles_dir, folder)

        # 遍历文章目录，找到第一个 .html 文件
        for file in os.listdir(current_article_path):
            if file.endswith(".html"):
                html_file = file
                break # 找到第一个就够了

        if html_file:
            # 将文件夹名中的下划线替换为空格，并首字母大写作为标题
            title = folder.replace('_', ' ').title()
            # 链接路径相对于最终的 index.html (在 dist 目录下) 是正确的
            # 例如：如果 index.html 在 dist/，而文章在 dist/field_space/field_space.html
            # 那么链接就是 folder/html_file (即 field_space/field_space.html)
            links += f'  <li><a href="{folder}/{html_file}">{title}</a></li>\n'
        else:
            print(f"Warning: No .html file found in '{current_article_path}'. Skipping this folder.")


    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Wiki 主页</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <h1>我的 Wiki 文章列表</h1>
  <ul>
{links}
  </ul>
</body>
</html>
"""

if __name__ == "__main__":
    # 仅当此脚本直接运行时，将生成的 HTML 打印到标准输出
    # 正常情况下，它会被 build_site.py 导入并使用
    print(get_generated_index_html())