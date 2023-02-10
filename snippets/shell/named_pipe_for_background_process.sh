mkfifo /tmp/mypipe
tail -f /tmp/mypipe | myserver &
