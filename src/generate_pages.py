import os

from markdown_to_html import markdown_to_html

def extract_title(markdown):
    title = ""
    for line in markdown.split("\n"):
        if line.strip().startswith("# "):
            title = line.strip("# ")
    return title

def generate_recursive(src, temp_path, dest):
    if os.path.isfile(src):
        generate_page(src, temp_path, dest)
        return

    dir_list = os.listdir(src)

    for item in dir_list:
        src_item = os.path.join(src, item)
        dest_item = os.path.join(src, item)
        generate_page(src_item, temp_path, dest_item)

def generate_page(src, temp_path, dest):
    print(f"Generating page from {src} to {dest} using {temp_path}")

    if not os.path.exists(dest) and os.path.isdir(src):
        os.mkdir(dest)

    with open(src, "r") as f:
        md = f.read()

    with open(temp_path, "r") as f:
        temp = f.read()

    node = markdown_to_html(md)
    html = node.to_html()
    title = extract_title(md)

    temp = temp.replace("{{ Title }}", title)
    temp = temp.replace("{{ Content }}", html)

    with open(dest, "w") as f:
        f.write(temp)

    return
