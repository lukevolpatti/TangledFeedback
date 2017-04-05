function increaseSize(){
	var max = 15;
	var bodySize = document.body.style.fontSize.substring(0, document.body.style.fontSize.length - 2);
	if (bodySize === "") {
		document.body.style.fontSize = "7vh";
	} else if (parseInt(bodySize) < max) {
		document.body.style.fontSize = parseInt(bodySize) + 1 + "vh";
	}
	document.getElementById("mainTitle").style.fontSize="15vh";
}

function decreaseSize(){
	document.body.style.fontSize="6vh";
	document.getElementById("mainTitle").style.fontSize="15vh";
}