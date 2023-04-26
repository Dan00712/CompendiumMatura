from publish.paths import HTML_PATH
from ghp_import import ghp_import

def main(push=False)-> int:
    ghp_import(srcdir=str(HTML_PATH), push=push, force=True, nojekyll=True)
    return 0

if __name__ == '__main__':
    exit(main())