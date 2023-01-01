#!/bin/sh

case "$(uname -s)" in
  Linux*)   xdg-open "$@" ;;
  Darwin*)  open "$@" ;; 
esac
