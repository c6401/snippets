touch ~/.bashrc.whitelist

_source_rc() {
    if grep -Fxq "$PWD" ~/.bashrc.whitelist
    then
        . .bashrc
    else
        read -p "Whitelist $PWD/.bashrc file? " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]
        then
            echo $PWD >> ~/.bashrc.whitelist
            . .bashrc
        fi
    fi
}

if [ -f .bashrc ] && [ "$PWD" != "$HOME" ]
then
    _source_rc
fi

cd() {
    builtin cd "$@"
    if [ -f .bashrc ]
    then
        _source_rc
    fi
}
