# scripts/generate_index.py

import os

def get_generated_index_html():
    docs_dir = "docs" # 现在指向 'docs' 目录

    language_folders = []
    if os.path.exists(docs_dir):
        # 筛选出 'docs' 目录下的所有文件夹，这些通常是语言文件夹 (e.g., 'en', 'zh')
        language_folders = [f for f in os.listdir(docs_dir) if os.path.isdir(os.path.join(docs_dir, f))]
    else:
        print(f"Warning: Directory '{docs_dir}' not found. No documentation will be listed.")

    # 构建链接列表，按语言分类
    language_sections = ""
    for lang_folder in sorted(language_folders):
        lang_path = os.path.join(docs_dir, lang_folder)
        article_links_for_lang = ""
        
        # 遍历每个语言文件夹内的文章子目录
        article_subfolders = [f for f in os.listdir(lang_path) if os.path.isdir(os.path.join(lang_path, f))]
        
        for article_folder in sorted(article_subfolders):
            article_path = os.path.join(lang_path, article_folder)
            html_file = None

            # 遍历文章目录，找到第一个 .html 文件
            for file in os.listdir(article_path):
                if file.endswith(".html"):
                    html_file = file
                    break

            if html_file:
                # 假设文件夹名就是标题，或对其进行简单处理
                title = article_folder.replace('_', ' ').title()
                # 链接路径相对于最终的 index.html (在 dist 目录下)
                # 例如：dist/zh/determinant/determinant.html
                links_relative_path = os.path.join(lang_folder, article_folder, html_file).replace(os.sep, '/')
                article_links_for_lang += f'      <li><a href="{links_relative_path}">{title}</a></li>\n'
            else:
                print(f"Warning: No .html file found in '{article_path}'. Skipping this folder.")
        
        if article_links_for_lang:
            language_sections += f"""  <h2>{lang_folder.upper()} Articles</h2>
  <ul>
{article_links_for_lang}
  </ul>
"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Wiki 主页</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <h1>我的 Wiki 文章列表</h1>
{language_sections if language_sections else '  <p>No articles found.</p>'}
</body>
</html>
"""

if __name__ == "__main__":
    print(get_generated_index_html())