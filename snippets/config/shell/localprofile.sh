function _localprofile () {
  builtin cd "$@"
  if [ -f .localprofile ]; then
    . ./.localprofile
  fi
}

function cd () {
  _localprofile
}

_localprofile
