(()=>{var {open:o,setRequestHeader:sh,send:sn}=p=XMLHttpRequest.prototype;p.open=function(...a){var h={};p.setRequestHeader=(k,v)=>{h[k]=v;sh.call(this,k,v)};p.send=b=>{console.log(JSON.stringify([...a,h,b]));sn.call(this,b)};o.call(this,...a)}})();