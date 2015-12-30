function! Search(arg)
    pyfile vimSearch.py
endfunc
command! -nargs=1 Search call Search(<f-args>)
