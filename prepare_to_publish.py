#!/venv/bin/python
import os
import shutil
import pathlib as plib
from util import get_export_files_list
from typing import List

import jinja2

export_path = plib.Path('build')/'to_publish'
template_path = plib.Path('html_templates/')

def get_compiled_sites():
    return plib.Path('./build/_build/_page').iterdir()


def get_filtered_sites()->List[plib.Path]:
    export_list = get_export_files_list()
    is_in_list = lambda p: p.is_dir() and p.name in export_list
    return list(filter(is_in_list, get_compiled_sites()))

def create_export_dir():
    export_path.mkdir(parents=True, exist_ok=True)


def copy_exported_files():
    site_dirs = get_filtered_sites()

    for site_path in site_dirs:
        export_subdir = export_path/site_path.name
        #os.mkdir(export_subdir)
        shutil.copytree(site_path, export_subdir, dirs_exist_ok=True)


def copy_html_template():
    global template_path
    template_loader = jinja2.FileSystemLoader(template_path)
    template_env = jinja2.Environment(loader=template_loader)

    FILE = 'index.html'

    template = template_env.get_template(FILE)
    output_text = template.render(sites=get_export_files_list())

    global export_path
    index = export_path/'index.html'
    index.touch()
    with index.open('w') as f:
        f.write(output_text)


def copy_css_files():
    is_css = lambda p: p.is_file() and p.suffix == '.css'

    css_files = (filter(is_css, template_path.iterdir()))
    for file in css_files:
        new_file = export_path/file.name
        new_file.touch()
        shutil.copy(file, new_file)

def main()-> int:
    create_export_dir()
    copy_exported_files()

    copy_html_template()
    copy_css_files()

if __name__ == '__main__':
    exit(main())