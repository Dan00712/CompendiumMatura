
import pathlib as plib

root_path = plib.Path('.')

notebooks = root_path/'notebooks'
export_files  = plib.Path().cwd()/'export_files'

output_dir = 'build'

export_path = plib.Path('build')/'to_publish'
template_path = plib.Path('html_templates/')
