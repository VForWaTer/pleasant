//Select Data
function select_data(evt) {
	var files = evt.target.files;
	for (var i = 0, f; f = files[i]; i++) {
		document.getElementById("workspace").innerHTML += "<li class='respo-padding' " +"id='"+f.name+
		"'><span class='respo-medium'><strong>"+f.name+"</strong> \r\n("+ f.type + ") - "+f.size+
 		"  bytes</span><a href='javascript:void(0)' onclick=this.parentElement.remove(); " +
		"class='respo-hover-white respo-right'><i class='fa fa-remove fa-fw'></i></a><br></li>";
		}

}