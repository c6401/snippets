# Snippets lib
## Bookmarklets
wsrpc:  
javascript:(()=>{wsrpc0=(new WebSocket('ws://localhost:8080'));wsrpc0.onmessage=m=>wsrpc0.send(eval(m.data))})()

xhrlog:  
javascript:(()=>{let{open:o,setRequestHeader:sh,send:sn}=p=XMLHttpRequest.prototype;p.open=function(...a){let h={};p.setRequestHeader=(k,v)=>{h[k]=v;sh.call(this,k,v)};p.send=b=>{wsrpc0.send(JSON.stringify([...a,h,b]));sn.call(this,b)};o.call(this,...a)}})();

2x:  
javascript:(()=>{document.getElementsByTagName('video')[0].playbackRate=2.0})()

ed:  
javascript:document.body.contentEditable='true';document.designMode='on';void 0

no-listen:  
javascript:document.querySelectorAll('*').forEach((e)=>e.parentNode.replaceChild(e.cloneNode(true),e))

no-style:  
javascript:[...document.styleSheets].forEach(x=>x.disabled=true)