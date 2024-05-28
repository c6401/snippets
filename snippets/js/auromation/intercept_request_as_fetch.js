(function({open, setRequestHeader, send}) {
    const proto = XMLHttpRequest.prototype;
    proto.open = function(method, url, async, user, password) {
        const headers = {};
        proto.setRequestHeader = (name, value) => {
            headers[name] = value;
            setRequestHeader.call(this, name, value);
        };
        proto.send = (body) => {
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
})(XMLHttpRequest.prototype);
