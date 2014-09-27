console.log("Message sending");
setTimeout(function() { 
	parentForm = document.getElementsByClassName("order-item")[0];
	foundId = parentForm.productId.value;
	console.log(foundId);
	chrome.runtime.sendMessage({prodId: foundId});}, 3000);