import pathlib as plib
from typing import List

def get_export_files_list() -> List[str]:
    with (plib.Path().cwd()/'export_files').open() as f:
        return [line.rstrip('\n') for line in f]
