document.addEventListener('click', function listener(event) {
  console.log(event.target);
  console.log(event.target.parentNode.parentNode.parentNode);
  document.removeEventListener('click', listener, true);
  event.preventDefault();
  event.stopPropagation();
  return false;
}, true);
