#!/usr/bin/env sh
cat > /tmp/.filtr
tilix -q -e 'bash -c "cat /tmp/.filtr | fzf > /tmp/.filtr-res"' 2> /dev/null
rm /tmp/.filtr
cat /tmp/.filtr-res
rm /tmp/.filtr-res
