function! Search(arg)
    pyfile ~/.vim/bundle/VimSearch/plugin/vimSearch.py
endfunc
command! -nargs=1 Search call Search(<f-args>)
