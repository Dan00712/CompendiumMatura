from publish.paths import export_path
from ghp_import import ghp_import

def main(only_local=False)->int:
    ghp_import(str(export_path.absolute()), nojekyll=True, force=True, push=not only_local)
    return 0

if __name__ == '__main__':
    exit(main(True))