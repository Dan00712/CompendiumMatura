#!/venv/bin/python

import os
#import os.path as path
import pathlib as plib

import subprocess

from typing import List

from pprint import pprint 

from publish.util import get_export_files_list
from publish.paths import notebooks

from publish.paths import output_dir

def get_notebook_path()-> plib.Path:
    return notebooks


def get_notebooks()->List[plib.Path]:
    contents = list(get_notebook_path().iterdir())

    files_to_export = get_export_files_list()
    is_notebook = lambda p: p.suffix == ('.ipynb')
    should_be_compiled = lambda p: p.stem in files_to_export

    should_count = lambda p: is_notebook(p) and should_be_compiled(p)
    return list(filter(should_count, contents))


def run_convert(fn):
    return subprocess.call(['jupyter-book', 'build', f'--path-output={output_dir}', '--builder=html', fn])

def main()->int:
    try:
        nbs = get_notebooks()
        for nb in nbs:
            code = run_convert(str(nb))
            if code != 0: return 1
        return 0
    except:
        return 2
    

if __name__ == '__main__':
    exit(main())