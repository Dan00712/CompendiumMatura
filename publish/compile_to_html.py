#!/venv/bin/python
import logging
import os
#import os.path as path
import pathlib as plib

import subprocess
from subprocess import Popen, PIPE, STDOUT, CalledProcessError

from typing import List

from pprint import pprint 

import publish.util as util
from publish.util import get_export_files_list
from publish.paths import notebooks

from publish.paths import output_dir


log = logging.getLogger('Compile')

def get_notebook_path()-> plib.Path:
    return notebooks


def get_notebooks()->List[plib.Path]:
    contents = list(get_notebook_path().iterdir())

    files_to_export = get_export_files_list()
    is_notebook = lambda p: p.suffix == ('.ipynb')
    should_be_compiled = lambda p: p.stem in files_to_export

    should_count = lambda p: is_notebook(p) and should_be_compiled(p)
    return list(filter(should_count, contents))


def run_convert(fn)->int:
    process = Popen(['jupyter-book', 'build', f'--path-output={output_dir}', '--builder=html', fn], stdout=PIPE, stderr=PIPE)

    with process.stdout:
        try:
            for line in iter(process.stdout.readline, b''):
                log.debug(line.decode('utf-8').strip())
        except CalledProcessError as e:
            log.error(str(e))

    return process.wait()
    #return subprocess.call(['jupyter-book', 'build', f'--path-output={output_dir}', '--builder=html', fn])

def main()->int:
    try:
        nbs = get_notebooks()
        log.debug('got notebooks: %s', nbs)
        log.info('converting notebooks...')
        for nb in nbs:
            log.info(f'converting notebook: %s', str(nb))
            code = run_convert(str(nb))
            if code != 0: return 1
        log.info('all notebooks converted')
        return 0
    except:
        return 2
    

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--nb', default=None)
    args = parser.parse_args()

    util.USE_CMD_NBS = args.nb is not None
    util.CMD_NBS = [args.nb]

    exit(main())