import publish.compile as compile
import publish.gh_pages as ghp
import publish.util as util

import logging
import logging_config
log = logging.getLogger('manager')

def main()-> int:
    if compile.main() != 0: return 1
    log.info('Compile finished')

    is_main = util.is_main_branch()
    log.debug('is main branch: %s', is_main)
    if is_main:
        log.info('publishing using ghp-import')
        if ghp.main(push=True) != 0: return 2
    else:
        log.info('skipping publish')
    log.info('finished')
    return 0

if __name__ == '__main__':
    exit(main())