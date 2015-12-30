function! Search(query)
    pyfile vimSearch.py
endfunc
command! Search call Search(query)
