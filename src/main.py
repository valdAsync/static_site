import os
import shutil

from copystatic import copy_directory
from getcontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
dir_path_templates = "./template.html"


def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files")
    copy_directory(dir_path_static, dir_path_public)

    print("Generating pages")
    generate_page(
        f"{dir_path_content}/index.md",
        dir_path_templates,
        f"{dir_path_public}/index.html",
    )


main()
