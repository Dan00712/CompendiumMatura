#!/venv/bin/python

import os
#import os.path as path
import pathlib as plib

import subprocess

from typing import List

from pprint import pprint 

def get_notebook_path()-> str:
    return plib.Path().cwd()/'notebooks'


def get_notebooks()->List[str]:
    contents = list(get_notebook_path().iterdir())

    is_notebook = lambda p: p.suffix == ('.ipynb')
    return list(filter(is_notebook, contents))


def run_convert(fn):
    subprocess.run(['jupyter-book', 'build', '--path-output=build', '--builder=html', fn])

def main():
    try:
        nbs = get_notebooks()
        for nb in nbs:
            run_convert(nb)
        return 0
    except:

        return 1
    

if __name__ == '__main__':
    exit(main())