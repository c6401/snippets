ansible-playbook -i localhost, /dev/stdin << EOF
- hosts: localhost
  connection: local
  tasks:
    - debug: msg="hello"
EOF
