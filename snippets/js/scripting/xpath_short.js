$x = e => {let r = [], it = document.evaluate(e, document, null, XPathResult.ANY_TYPE, null); while (x = it.iterateNext()) {r.push(x)}; return r}
