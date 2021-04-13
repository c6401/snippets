function *findText(text, { prefix, tag }={ prefix: '', tag: '*' }) {
  var results = document.evaluate(
    `//${tag}[${prefix}contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), text)]`,
    document, null, XPathResult.ANY_TYPE, null
  );
  var result = 1;
  while (result) {
    yield result = results.iterateNext();
  }
}
