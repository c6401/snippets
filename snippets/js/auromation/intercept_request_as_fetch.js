(function(open, setRequestHeader, send) {
    XMLHttpRequest.prototype.open = function(method, url, async, user, password) {
        this.addEventListener("readystatechange", function() {
            if (this.readyState === 4) {
                console.log(this);
            };
        }, false);
        const headers = {};
        XMLHttpRequest.prototype.setRequestHeader = function(name, value) {
            headers[name] = value;
            setRequestHeader.call(this, name, value);
        };
        XMLHttpRequest.prototype.send = function(body) {
            console.log(method, url, async, user, password, headers, body);
            console.log(`
async function () {
  await fetch(\`${url}\`, {
      method: '${method}',
      headers: ${JSON.stringify(headers)},
      body: '${body}'
  });
}
            `);
            send.call(this, body);
        };
        open.call(this, method, url, async, user, password);
    };
})(XMLHttpRequest.prototype.open, XMLHttpRequest.prototype.setRequestHeader, XMLHttpRequest.prototype.send);
