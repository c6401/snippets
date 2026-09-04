(() => {
  const log = (window.__ajaxLog = []);
  const record = (e) => (log.push(e), console.log('[ajax]', e));

  const nativeFetch = fetch;
  window.fetch = async (url, opts = {}) => {
    const res = await nativeFetch(url, opts);
    record({ method: 'GET', url: url.url || url, ...opts, status: res.status, response: await res.clone().text() });
    return res;
  };

  const p = XMLHttpRequest.prototype;
  const { open, send, setRequestHeader } = p;
  p.open = function (method, url, ...rest) {
    this._e = { url, method, headers: {} };
    return open.call(this, method, url, ...rest);
  };
  p.setRequestHeader = function (key, value) {
    this._e.headers[key] = value;
    return setRequestHeader.call(this, key, value);
  };
  p.send = function (body) {
    this._e.body = body;
    this.addEventListener('loadend', () => record({ ...this._e, status: this.status, response: this.responseText }));
    return send.call(this, body);
  };
})();