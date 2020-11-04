const { JSDOM } = require('jsdom');
var dom = new JSDOM(text);
dom.window.document;
