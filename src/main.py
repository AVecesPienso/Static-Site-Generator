import shutil, os
from gencontent import generate_page
from recursivecopy import recursive_copy

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    recursive_copy(dir_path_static, dir_path_public)

    src = os.listdir(os.path.join(dir_path_content, "blog"))
    for item in src:
        input_md = os.path.join(dir_path_content, "blog", item, "index.md")
        output_html = os.path.join(dir_path_public, "blog", item, "index.html")
        generate_page(input_md, template_path, output_html)

    print("Generating page...")

    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )

    os.makedirs(os.path.join(dir_path_public, "contact"), exist_ok=True)
    generate_page(
        os.path.join(dir_path_content, "contact", "index.md"),
        template_path,
        os.path.join(dir_path_public, "contact", "index.html"),
    )

main()