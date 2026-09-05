javascript:
(() => {
  const log = (window.__ajaxLog = []);
  const record = (e) => (log.push(e), console.log('[ajax]', e));
  window.dump = () => Object.assign(document.createElement('a'), { href: URL.createObjectURL(new Blob([JSON.stringify(log, null, 2)])), download: 'ajax-log.json' }).click();

  const nativeFetch = fetch;
  window.fetch = async (url, opts) => {
    const res = await nativeFetch(url, opts);
    record({ method: 'GET', url: url.url || url, ...opts, status: res.status, response: await res.clone().text() });
    return res;
  };

  const { open, send, setRequestHeader } = XMLHttpRequest.prototype;
  XMLHttpRequest.prototype.open = function (method, url) {
    const e = { method, url, headers: {} };
    this.setRequestHeader = (k, v) => (e.headers[k] = v, setRequestHeader.call(this, k, v));
    this.send = (b) => {
      e.body = b;
      this.addEventListener('loadend', () => record({ ...e, status: this.status, response: this.responseText }));
      return send.call(this, b);
    };
    return open.apply(this, arguments);
  };
})();
