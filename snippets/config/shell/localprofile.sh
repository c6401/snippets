function _localprofile () {
  if [ -f .localprofile ]; then
    . .localprofile
  fi
}

function cd () {
  _localprofile
}

_localprofile
