function* findall(expr, str) {
  re = new RegExp(expr, 'g');
  while ((found = (re.exec(str))) !== null) {
    yield found;
  }
}
