watchdir() {
    dir=$1
    shift
    while true; do inotifywait -e modify -r $dir && eval $@; done;
}
