function movePiece()
{

	var moveFrom = document.getElementById("moveFrom").value;
	var moveTo = document.getElementById("moveTo").value;
	document.getElementById(moveTo).innerHTML = document.getElementById(moveFrom).innerHTML;
	document.getElementById(moveFrom).innerHTML = "&nbsp;";
	return false;

}
