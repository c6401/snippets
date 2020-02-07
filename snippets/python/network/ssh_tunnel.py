# !python3 -mpip install --user sshtunnel
from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    'remote_host',
    ssh_username="user",
    ssh_password="secret",
    remote_bind_address=('127.0.0.1', 8080)
)

server.start()

print(server.local_bind_port)  # show assigned local port
# work with `SECRET SERVICE` through `server.local_bind_port`.

# server.stop()
