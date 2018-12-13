set encoding=utf-8
set number "Display line numbers
set list "List all whitespace chars
set listchars=eol:<,tab:>-,trail:~,extends:>,precedes:< "Set what caracters to use for the listing
set scrolloff=10 "The minimum number of lines to se above or bellow cursor

"Setup tabs
let tabsize = 4
execute "set shiftwidth=".tabsize
execute "set tabstop=".tabsize
set expandtab "Insert spaces instead of tabs

"Setup vundle
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'

"All vundle plugins go here


call vundle#end()
filetype plugin indent on
