grep -Fxq "$1" "$2" || echo "$1" >> "$2"
