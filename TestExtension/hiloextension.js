console.log("loaded extension");

function loadProduct( productID ) {
	console.log("loading product");
	var proText = "";
	var conText = "";
	$.ajax({ // get the #1 pro
		url : "products/" + productID + "/gettoppros=1",
		success : function (data) {
		proText = data.message
	},
	error : function () {},
	async : true
	});
	$.ajax({ // get the #1 con
		url : "products/" + productID + "/gettopcons=1",
		success : function (data) {
		conText = data.message
		},
		error : function () {},
		async : true
	});
	if (proText === "") proText = "Be the first to add a pro!";
	if (conText === "") conText = "Be the first to add a con!";
	var element = document.getElementById("header");
	element.innerHTML = "Pro: " + proText;
	
}

chrome.runtime.onMessage.addListener(
	function(request, sender, sendResponse) {
		console.log("got a message");
		// chrome.windows.create({'url': 'hilopopup.html', 'type': 'popup'}, function(window) {     });
    loadProduct(request.prodID);
  });