from publish.paths import NOTEBOOK_PATH, BUILD_PATH
from subprocess import Popen, PIPE, call, CalledProcessError

import logging
log = logging.getLogger('compile')

def build_book(path=NOTEBOOK_PATH, output=BUILD_PATH):
    cmds = ['jupyter-book', 'build', f'{path}', f'--path-output={output}']
    log.debug('running compile with: %s', cmds)
    process = Popen(cmds, stdout=PIPE, stderr=PIPE)

    with process.stdout:
        try:
            for line in iter(process.stdout.readline, b''):
                log.debug(line.strip())
        except CalledProcessError as e:
            log.error(str(e))
    with process.stderr:
        try:
            for line in iter(process.stderr.readline, b''):
                log.warning(line.strip())
        except CalledProcessError as e:
            log.error(str(e))
    
    code = process.wait()
    return code
    
    

def main()-> int:
    try:
        code = build_book()
    except:
        return 1
    return code

if __name__ == '__main__':
    exit(main())