# scripts/generate_index.py

import os

def generate_index():
    articles_dir = "articles"
    article_folders = [f for f in os.listdir(articles_dir) if os.path.isdir(os.path.join(articles_dir, f))]

    links = ""
    for folder in article_folders:
        html_file = None
        for file in os.listdir(os.path.join(articles_dir, folder)):
            if file.endswith(".html"):
                html_file = file
                break
        if html_file:
            title = folder.replace('_', ' ').title()
            links += f'  <li><a href="{folder}/{html_file}">{title}</a></li>\n'

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
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(generate_index())