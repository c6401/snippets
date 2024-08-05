// @grant GM_xmlhttpRequest


GM_xmlhttpRequest({
  method: "GET",
  // method: "POST",
  url: "http://www.example.net/",
  // data: "username=johndoe&password=xyz123",
  // data: JSON.stringify({...}),
  headers: {
    // "Content-Type": "application/x-www-form-urlencoded",
    // "Content-Type": "application/json",
  },
  onload: function(response) {
    var responseXML = null;
    // if (!response.responseXML) {
    //   responseXML = new DOMParser()
    //     .parseFromString(response.responseText, "text/xml");
    // }
    // json = JSON.parse(response.responseText);

    console.log([
      response.status,
      response.statusText,
      response.readyState,
      response.responseHeaders,
      response.responseText,
      response.finalUrl,
      // responseXML,
      // json,
    ].join("\n"));
  }
});
