function _localprofile () {
  if [ -f .localprofile ]; then
    . ./.localprofile
  fi
}

function cd () {
  builtin cd "$@"
  _localprofile
}

_localprofile
