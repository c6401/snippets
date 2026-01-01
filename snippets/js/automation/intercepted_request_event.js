(()=>{var{open:o,setRequestHeader:sh,send:sn}=p=XMLHttpRequest.prototype;p.open=function(m,u){var h={};p.setRequestHeader=(k,v)=>{h[k]=v;sh.call(this,k,v)};p.send=b=>{postMessage({method:m,url:u,headers:h,body:b},'*');sn.call(this,b)};o.call(this,m,u)}})();

addEventListener('message',e=>{if(e.data.method)console.log(e.data)})
