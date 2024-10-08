document.addEventListener('myEvent', e => { console.info(e.detail) });
document.dispatchEvent(new CustomEvent('myEvent', { detail: { ... } }));
