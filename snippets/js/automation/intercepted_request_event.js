(()=>{var {open:o,setRequestHeader:sh,send:sn}=p=XMLHttpRequest.prototype;p.open=function(m,u,a){var h={};p.setRequestHeader=(k,v)=>{h[k]=v;sh.call(this,k,v)};p.send=b=>{document.dispatchEvent(new CustomEvent('myreq',{detail:{method:m,url:u,headers:h,body:b}}));sn.call(this,b)};o.call(this,m,u,a)}})();