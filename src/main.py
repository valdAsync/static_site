import os
import shutil

from htmlnode import HTMLNode, LeafNode
from textnode import TextNode

dir_path_static = "./static"
dir_path_public = "./public"


def copy_directory(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isdir(source_path):
            print(f"Copying directory {source_path} to {destination_path}")
            copy_directory(source_path, destination_path)
        else:
            print(f"Copying file {source_path} to {destination_path}")
            shutil.copy2(source_path, destination_path)


def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copy_directory(dir_path_static, dir_path_public)


main()
