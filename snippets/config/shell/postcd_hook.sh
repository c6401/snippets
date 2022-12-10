function cd () {
  builtin cd "$@"
  local IFS=$';'
  for f in $POST_CD; do
    "$f"
  done
  unset IFS
}

POST_CD="___"
