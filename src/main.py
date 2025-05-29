import shutil, os, sys
from gencontent import generate_pages_recursive
from recursivecopy import recursive_copy

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
dir_path_contact = "./content/contact"

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to public directory...")
    recursive_copy(dir_path_static, dir_path_docs)

    print("Generating page...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)

main()