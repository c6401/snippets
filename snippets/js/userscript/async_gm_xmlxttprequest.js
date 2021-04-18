function gm_xhr(kwargs) {
  return new Promise(
    (resolve, reject) => GM_xmlhttpRequest({
      onload: resolve,
      onerror: reject,
      ...kwargs,
    })
  );
};

response = await gm_xhr({url: 'http://localhost'});
response.responseText;
