(function(open, setRequestHeader, send) {
    XMLHttpRequest.prototype.open = function(method, url, async, user, password) {
        const headers = {};
        XMLHttpRequest.prototype.setRequestHeader = function(name, value) {
            headers[name] = value;
            setRequestHeader.call(this, name, value);
        };
        XMLHttpRequest.prototype.send = function(body) {
            console.log(JSON.stringify({method, url, async, user, password, headers, body}));
            send.call(this, body);
        };
        open.call(this, method, url, async, user, password);
    };
})(XMLHttpRequest.prototype.open, XMLHttpRequest.prototype.setRequestHeader, XMLHttpRequest.prototype.send);
