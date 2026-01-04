def extract_title(markdown):
    title = ""
    for line in markdown.split("\n"):
        if line.strip().startswith("# "):
            title = line.strip("# ")
    return title