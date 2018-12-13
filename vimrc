set encoding=utf-8
set number "Display line numbers
set list "List all whitespace chars
set listchars=eol:<,tab:>-,trail:~,extends:>,precedes:< "Set what caracters to use for the listing
set scrolloff=10 "The minimum number of lines to se above or bellow cursor

"Setup python
let python_tabsize = 4
au BufNewFile,BufRead *.py
    \execute "set shiftwidth=".tabsize
    \execute "set tabstop=".tabsize
    \execute "set softtabstop=".tabsize
    \set expandtab "Insert spaces instead of tabs
    \set autoindent
    \set fileformat=unix
    \set textwidth=79
"Setup vundle
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'

"All vundle plugins go here
Plugin 'vim-scripts/indentpython.vim'
Bundle 'Valloric/YouCompleteMe'
Plugin 'vim-syntastic/syntastic'
Plugin 'nvie/vim-flake8'
call vundle#end()
filetype plugin indent on

let python_highlight_all=1
syntax on

"Yooucomplete me settings
let g:ycm_autoclose_preview_window_after_completion=1
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
