function listener(event) {
  console.log(event.target);
  document.removeEventListener('click', listener, true);
}
document.addEventListener('click', listener, true);
