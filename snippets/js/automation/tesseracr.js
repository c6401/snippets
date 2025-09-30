
var s = document.createElement("script")
s.src = "https://unpkg.com/tesseract.js@v2.1.0/dist/tesseract.min.js";
document.head.appendChild(s);
s.onload = (async () => {
    const imageUrls = Array.from(document.querySelectorAll('img')).filter(img => {
        const style = window.getComputedStyle(img);
        return style.display !== 'none' && style.visibility !== 'hidden' && img.src.endsWith('.jpg');
    }).map(img => img.src);

  const worker = Tesseract.createWorker();
  await worker.load();
  await worker.loadLanguage('por');
  await worker.initialize('por');
  for (const url of imageUrls) {
    console.log(url);
    var { data: { text } } = await worker.recognize(url);
    console.log(text);
  }
});

