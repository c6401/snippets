# pip install websocket-server
# javascript:(function(){var ws;function call(data){try{return eval(data)}catch(e){return e.toString()}};function setup(){ws=new WebSocket('ws://localhost:'+%s);ws.onclose=function(){setTimeout(setup,5000)};ws.onmessage=async function(ev){var rs=call(ev.data);ws.send(rs.then?await rs:rs)}};setup()})();
import queue, threading, websocket_server
q = queue.Queue()
server = websocket_server.WebsocketServer(host='127.0.0.1', port=8080)
server.set_fn_message_received(lambda cl, srv, message: q.put(message))
server.set_fn_new_client(lambda cl, srv: print('connected'))
def rpc(data): server.send_message(server.clients[0], data); return q.get()
thread = threading.Thread(target=server.run_forever)
thread.start()
# rpc('(async () => (await (fetch("example.org"))).text())()')
