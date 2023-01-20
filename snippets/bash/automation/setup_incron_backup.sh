# sudo vim /etc/incron.allow
# incrontab -e
/location IN_MODIFY,IN_CREATE,IN_MOVED_FROM,IN_MOVED_TO /usr/bin/git -C /location commit -a --allow-empty-message -m ''
