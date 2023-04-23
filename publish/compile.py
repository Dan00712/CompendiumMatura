from publish.paths import NOTEBOOK_PATH, BUILD_PATH
from subprocess import Popen, PIPE, call, CalledProcessError

import logging
log = logging.getLogger('compile')

def build_book(path=NOTEBOOK_PATH, output=BUILD_PATH):
    cmds = ['jupyter-book', 'build', f'{path}', f'--path-output={output}']
    log.debug('running compile with: %s', cmds)
    process = Popen(cmds, stdout=PIPE)

    with process.stdout:
        try:
            for line in iter(process.stdout.readline, b''):
                log.debug(line.strip())
        except CalledProcessError as e:
            log.error(str(e))
    
    return process.wait()
    

def main()-> int:
    try:
        build_book()
    except:
        return 1
    return 0

if __name__ == '__main__':
    exit(main())