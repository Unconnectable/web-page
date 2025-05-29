# scripts/build_site.py

import os
import shutil

def build(output_dir="dist"):
    print(f"Building site to {output_dir}...")

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    # 复制文章内容
    for root, dirs, files in os.walk("articles"):
        for d in dirs:
            src = os.path.join(root, d)
            dst = os.path.join(output_dir, d)
            shutil.copytree(src, dst)

    # 复制 assets
    if os.path.exists("assets"):
        shutil.copytree("assets", os.path.join(output_dir, "assets"))

    # 生成首页
    os.system("python scripts/generate_index.py > " + os.path.join(output_dir, "index.html"))

    print(f"Build completed at {output_dir}")

if __name__ == "__main__":
    build()