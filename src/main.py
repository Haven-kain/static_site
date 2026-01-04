import sys

from static_copy import copy_static
from generate_pages import generate_page, generate_recursive

def main():
    basepath = sys.argv[1]
    if len(sys.argv) < 2:
        basepath = "/"

    copy_static("./static", "./docs")
    generate_recursive("./content", "./template.html", "./docs", basepath)

if __name__ == "__main__":
    main()