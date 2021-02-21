export MYGITDIR='.mygit'
alias mg-here='export MYGITTREE="$PWD"'
alias mg-init='git init --bare "$MYGITTREE/$MYGITDIR"'
alias mg='/usr/bin/git --git-dir="$MYGITTREE/$MYGITDIR" --work-tree="$MYGITTREE"'