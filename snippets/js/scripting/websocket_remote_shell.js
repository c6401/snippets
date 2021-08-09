var socket;
function evalData(data) {
  var result;
  try {
    result = eval(data);
  } catch (e) {
    result = e.toString();
  }
  return result;
}

function setup() {
  socket = new WebSocket(`ws://localhost:${port}`);
  socket.onclose = function(){
    setTimeout(setup, 2000);
  };
  socket.onmessage = function (event) {
    var result = evalData(event.data)
    socket.send(result);
  }
}
setup()
