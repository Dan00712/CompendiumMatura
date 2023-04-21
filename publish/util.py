import pathlib as plib
from typing import List

from publish.paths import export_files
import argparse

def get_export_files_list() -> List[str]:
    if USE_CMD_NBS:
        return CMD_NBS
    with export_files.open() as f:
        return [line.rstrip('\n') for line in f]


def get_active_branch_name()->str:
    head_dir = plib.Path(".") / ".git" / "HEAD"
    with head_dir.open("r") as f: content = f.read().splitlines()

    for line in content:
        if line[0:4] == "ref:":
            return line.partition("refs/heads/")[2]


def is_main_branch()->bool:
    return get_active_branch_name() == 'main'