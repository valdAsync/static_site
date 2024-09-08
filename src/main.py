import os
import shutil

from copystatic import copy_directory
from htmlnode import HTMLNode, LeafNode
from textnode import TextNode

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copy_directory(dir_path_static, dir_path_public)


main()
