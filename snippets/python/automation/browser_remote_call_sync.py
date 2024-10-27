# /// script
# dependencies = [
#     "websocket-server",
# ]
# ///
import threading
from queue import Queue
from websocket_server import WebsocketServer

def rpc(port=8765, **kwargs):
    server = WebsocketServer(port=port, **kwargs)
    q = Queue()
    server.set_fn_message_received(lambda clt, srv, message: q.put(message))
    threading.Thread(target=server.run_forever, daemon=True).start()
    def send(message):
        server.send_message_to_all(message)
        return q.get(timeout=3)
    return send