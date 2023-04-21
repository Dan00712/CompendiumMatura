import pathlib as plib
from typing import List

from publish.paths import export_files

def get_export_files_list() -> List[str]:
    with export_files.open() as f:
        return [line.rstrip('\n') for line in f]
