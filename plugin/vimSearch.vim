function! Search(arg)
    pyfile vimSearch.py
endfunc
command! Search call Search(arg)
