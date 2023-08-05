myElement.addEventListener("myEvent", function(e) {
	console.info(e.detail);
})

var myEvent = new CustomEvent("myEvent", {
	detail: {...},
	bubbles: true,
	cancelable: false
});

myElement.dispatchEvent(myEvent);
