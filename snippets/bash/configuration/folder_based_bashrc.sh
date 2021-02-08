if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi
function cd () {
    builtin cd "$@"
    if [ -f ~/.bashrc ]; then
        . ~/.bashrc
    fi
}
