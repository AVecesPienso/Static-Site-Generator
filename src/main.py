import shutil, os
from textnode import TextType, TextNode

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))
    recursive_copy("static/", "public/")

def recursive_copy(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    src = os.listdir(source)
    for item in src:
        path = os.path.join(source, item)
        if os.path.isfile(path):
            shutil.copy(path, destination)
        else:
            dir_path = os.path.join(destination, item)
            os.mkdir(dir_path)
            recursive_copy(path, dir_path)


main()