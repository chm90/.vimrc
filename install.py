"""
Installs the vimrc file from this repo.
It does so by adding a line to load the new vimrc to the vim rc in the users home directory.
Creates a new .vimrc file if no one currently exists.
"""

from os import path

vimrc_path=path.abspath(path.join(path.dirname(__file__),'vimrc'))
dot_vimrc_path = path.expanduser('~/.vimrc')

load_vimrc_code = (
    'source {path}\n'
).format(path=vimrc_path)

with open(dot_vimrc_path,'a') as dot_vimrc:
    dot_vimrc.write(load_vimrc_code)
print('Success!')
