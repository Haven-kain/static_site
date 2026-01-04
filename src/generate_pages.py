from markdown_to_html import markdown_to_html

def extract_title(markdown):
    title = ""
    for line in markdown.split("\n"):
        if line.strip().startswith("# "):
            title = line.strip("# ")
    return title

def generate_page(src, temp_path, dest):
    print(f"Generating page from {src} to {dest} using {temp_path}")

    with open(src, "r") as f:
        md = f.read()

    with open(temp_path, "r") as f:
        temp = f.read()

    node = markdown_to_html(md)
    html = node.to_html()
    title = extract_title(md)

    temp = temp.reaplce("{{ Title }}", title)
    temp = temp.replace("{{ Content }}", html)

    with open(dest, "w") as f:
        f.write(temp)

    return
