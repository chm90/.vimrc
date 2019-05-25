"""
Installs the vimrc file from this repo.
It does so by adding a line to load the new vimrc to the vim rc in the users home directory.
Creates a new .vimrc file if no one currently exists.
"""
import os
from argparse import ArgumentParser
from os import path

parser = ArgumentParser(description='Script for installing vim configuration')
parser.add_argument('--force-vundle',action='store_true')
agrs = parser.parse_args()
vimrc_path=path.abspath(path.join(path.dirname(__file__),'vimrc'))
dot_vimrc_path = path.expanduser('~/.vimrc')
vundle_path = '~/.vim/bundle/Vundle.vim'


#Installing vimrc
print('Overwriting vim rc')
if path.isfile(dot_vimrc_path):
    os.remove(dot_vimrc_path)

os.link(vimrc_path,dot_vimrc_path)

#load_vimrc_code = (
#    'source {path}\n'
#).format(path=vimrc_path)

#with open(dot_vimrc_path,'a') as dot_vimrc:
#    dot_vimrc.write(load_vimrc_code)

# Install vundle 
if path.isdir(vundle_path) and args.force_vundle:
    os.removedirs(vundle_path)
if path.isdir(vundle_path):
    print('Vundle exists not installing, run with --force-vundle to override')
else:
    os.system('git clone https://github.com/VundleVim/Vundle.vim.git ' + vundle_path)
#Install vundle plugins

os.system('vim +PluginInstall +qall')

print('Success!')
