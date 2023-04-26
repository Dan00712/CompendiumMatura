from pathlib import Path

def get_active_branch_name()->str:
    head_dir = Path(".") / ".git" / "HEAD"
    with head_dir.open("r") as f: content = f.read().splitlines()

    for line in content:
        if line[0:4] == "ref:":
            return line.partition("refs/heads/")[2]

def is_main_branch()->bool:
    return get_active_branch_name() == 'main'