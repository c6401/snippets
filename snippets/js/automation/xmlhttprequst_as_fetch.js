return new Promise((resolve, reject) => {
  GM_xmlhttpRequest({
    method: method.toUpperCase(),
    url: url,
    headers: headers,
    data: body,
    onload: (response) => {
      resolve({
        ok: response.status >= 200 && response.status < 300,
        status: response.status,
        statusText: response.statusText,
        url: response.finalUrl || url,
        headers: new Headers(response.responseHeaders?.split('\r\n').reduce((acc, line) => {
          const [key, ...values] = line.split(':');
          if (key) acc[key.trim()] = values.join(':').trim();
          return acc;
        }, {}) || {}),
        text: () => Promise.resolve(response.responseText),
        json: () => Promise.resolve(JSON.parse(response.responseText)),
      });
    },
    blob: () => Promise.resolve(new Blob([response.response])),
    onerror: (response) => { reject(new Error(`Network request failed: ${response.statusText}`)); },
    ontimeout: () => { reject(new Error('Network request timed out')); },
  });
});
