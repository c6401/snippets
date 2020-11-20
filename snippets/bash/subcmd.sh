subcmd() { if [ $2 ]; then cmd=$1; sub=$2; shift 2; eval $cmd-$sub $@; else eval $1-default; fi; }
#alias command="subcmd command"
#alias command-default="..."
#alias command-...="..."
