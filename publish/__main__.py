import publish.util as util
from publish.util import is_main_branch

import publish.compile_to_html as to_html
import publish.prepare_to_publish as prepare 
import publish.github_pages as export

import argparse
 
def main()->int:
    parser = argparse.ArgumentParser(
        prog="publish",
        description="converts the jupyter notebooks and publishes them to gh-pages"
    )

    parser.add_argument('-l', '--local-only', action='store_true', dest='local_only', default=False)
    parser.add_argument('--nb', default=None)
    args = parser.parse_args()

    util.USE_CMD_NBS = args.nb is not None
    util.CMD_NBS = [args.nb]
 
    if to_html.main() != 0: return 1
    if prepare.main() != 0: return 2
    if not is_main_branch(): return 0
    if export.main(args.local_only) != 0: return 3
    return 0


if __name__ == '__main__':
    exit(main())