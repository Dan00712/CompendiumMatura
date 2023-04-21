import logging
from publish.paths import export_path
from ghp_import import ghp_import


log = logging.getLogger('GH-Pages')

def main(only_local=False)->int:
    log.info('moving files to gh-pages...with local_only=%s', only_local)
    ghp_import(str(export_path.absolute()), nojekyll=True, force=True, push=not only_local)
    log.info('gh-pages ready!')
    return 0

if __name__ == '__main__':
    exit(main(True))