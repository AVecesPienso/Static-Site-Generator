import os
from block_markdown import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} {template_path} -> {dest_path}")

    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    new_html = html.replace(
        "href=\"/", f"href=\"{basepath}"
        ).replace(
        "src=\"/", f"src=\"{basepath}"
        )

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", new_html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    input_list = os.listdir(dir_path_content)
    os.makedirs(dest_dir_path, exist_ok=True)
    for item in input_list:
        input_md = os.path.join(dir_path_content, item)
        if os.path.isfile(input_md):
            if input_md.endswith(".md"):
                file = os.path.splitext(item)
                new_filename = file[0] + ".html"
                html_file = os.path.join(dest_dir_path, new_filename)
                generate_page(input_md, template_path, html_file, basepath)
        else:
            generate_pages_recursive(input_md, template_path, os.path.join(dest_dir_path, item), basepath)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")