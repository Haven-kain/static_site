from static_copy import copy_static
from generate_pages import generate_recursive

def main():
    copy_static("./static", "./public")
    generate_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()