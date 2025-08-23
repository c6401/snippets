document.body.appendChild(Object.assign(document.createElement('script'), { src: 'https://cdn.jsdelivr.net/npm/pyodide/pyodide.min.js', async: true }));
py = await loadPyodide()
py.runPython('print(1)')
