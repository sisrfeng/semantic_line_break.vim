" bucky.vim - Ventilated prose
" Author:   Daniel B. Marques
" Version:  0.1
" License:  Same as Vim

" if exists("g:loaded_bucky") || &cp
"   finish
" endif
" let g:loaded_bucky = 1

setlocal formatexpr=bucky#md#format()

set formatprg=python3\ ~/PL/SemanticLineBr.vim/sent_tokenize.py\|par\ 78p2dh

