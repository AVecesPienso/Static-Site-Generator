import shutil, os
from textnode import TextType, TextNode
from block_markdown import markdown_to_html_node

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))
    recursive_copy("static/", "public/")
    generate_page("content/index.md", "template.html", "public/index.html")

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

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("#"):
            return line.strip("#").strip()
    raise Exception("No h1 header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as markdown_file:
        markdown = markdown_file.read()
    with open(template_path, 'r') as template_file:
        template = template_file.read()

    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    actual_title = template.replace("{{ Title }}", title)
    final_html = actual_title.replace("{{ Content }}", html_string)

    path = os.path.dirname(dest_path)
    os.makedirs(path, exist_ok=True)
    with open(dest_path, 'w') as destination_path:

        destination_path.write(final_html)
main()