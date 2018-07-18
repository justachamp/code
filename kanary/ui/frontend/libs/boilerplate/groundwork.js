(function() {
	if(window.location.protocol === 'file:') {
		window.alert("App might not work when opened directly from the file system. Please deploy in to a web server and access with 'http://' url");
	}

	
})();
