from textnode import *
from extract_markdown import *
from blocks import *
import os
import shutil
import sys

def recursive_copy(source_path: str, dest_path: str) -> None:
    if not os.path.exists(source_path):
        raise Exception(f"Source path \"{source_path}\" does not exist")
    
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
        print(f"rmtreeing {dest_path}")

    os.mkdir(dest_path)
    print(f"creating {dest_path}")

    if os.path.isfile(source_path):
        raise Exception(f"Source path \"{source_path}\" is not a directory")
    
    else:
        for e in os.listdir(source_path):
            source_path_e = os.path.join(source_path, e)

            if os.path.isfile(source_path_e):
                shutil.copy(source_path_e, dest_path)
                print(f"copying {source_path_e} to {dest_path}")

            else:
                dest_dir = os.path.join(dest_path, e)
                #os.mkdir(dest_dir)
                print(f"creating {dest_dir}")
                recursive_copy(source_path_e, dest_dir)


def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    if not os.path.exists(from_path) and not os.path.isfile(from_path):
        raise Exception(f"{from_path} is not a valid path or not a file")
    if not os.path.exists(template_path) and not os.path.isfile(template_path):
        raise Exception(f"{template_path} is not a valid path or not a file")

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_md_file = open(from_path)
    from_md = from_md_file.read()

    template_html_file = open(template_path)
    template_html = template_html_file.read()

    from_html = markdown_to_html_node(from_md).to_html()
    title = extract_title(from_md)
    if "{{ Title }}" not in template_html or "{{ Content }}" not in template_html:
        raise Exception(f"{template_path} is not a valid template file")
    dest_html = template_html.replace("{{ Title }}", title).replace("{{ Content }}", from_html)
    dest_html = dest_html.replace("href=\"/", f"href=\"{basepath}").replace("src=\"/", f"src=\"{basepath}")

    dest_path_dir = os.path.dirname(dest_path)
    os.makedirs(dest_path_dir, exist_ok=True)
    dest_html_file = open(dest_path, mode='w')
    dest_html_file.write(dest_html)

    from_md_file.close()
    template_html_file.close()
    dest_html_file.close()


def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str) -> None:
    if not os.path.exists(dir_path_content):
        raise Exception(f"Content path {dir_path_content} does NOT exist.")
    if not os.path.isfile(dir_path_content):
        for e in os.listdir(dir_path_content):
            generate_pages_recursive(os.path.join(dir_path_content, e), template_path, os.path.join(dest_dir_path, e).replace(".md", ".html"), basepath)
    else:
        if dir_path_content.split(".")[-1] == "md":
            generate_page(dir_path_content, template_path, dest_dir_path, basepath)
        pass

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "":
        basepath = "/"
    else:
        basepath = sys.argv[1]
    recursive_copy("static","docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()