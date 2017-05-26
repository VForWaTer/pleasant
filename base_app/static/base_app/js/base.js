//Toggle between showing and hiding the sidenav, and add overlay effect
function respo_open() {
	// Get the Sidenav
	var mySidenav = document.getElementById("mySidenav");

	// Get the DIV with overlay effect
	var overlayBg = document.getElementById("myOverlay");

	if (mySidenav.style.display === "block") {
		mySidenav.style.display = "none";
		overlayBg.style.display = "none";
	} else {
		mySidenav.style.display = "block";
		overlayBg.style.display = "block";
	}
}

//Close the sidenav with the close button
function respo_close() {
	var mySidenav = document.getElementById("mySidenav");

	var overlayBg = document.getElementById("myOverlay");

	mySidenav.style.display = "none";
	overlayBg.style.display = "none";
}

//Search
function search_close(){

	document.getElementById("search_box").outerHTML = "<a href='#' onclick='open_search()' id='srch_box' class='respo-hover-white'><i class='fa fa-search fa-fw'></i>  Search</a>";
	document.getElementById("search_but").outerHTML = "<a id='srch_but' class='respo-hover-none'></a>";
	document.getElementById("search_close_but").outerHTML = "<a id='srch_close_but' class='respo-hover-none'></a>";
}

function search_open(){
	if (!document.getElementById("search_box")){
		var searchBox = document.getElementById("srch_box");
		searchBox.outerHTML = "<a class='respo-hover-none' style='height:10px' id='search_box'><input type='search' value='' placeholder='Search ...' style='height:15px; font-size:75%;'></a>";

		var searchBut = document.getElementById("srch_but");
		searchBut.outerHTML = "<a href='#' class='respo-hover-white' style='height:80px' id='search_but' onclick='search_close()'><i class='fa fa-search fa-fw'></i></a>";

		var closeBut = document.getElementById("srch_close_but");
		closeBut.outerHTML = "<a href='javascript:void(0)' class='respo-hover-white' style='height:80px' id='search_close_but' onclick='search_close()'><i class='fa fa-remove fa-fw'></i></a>";
	}
}

//Select Data
function select_data(evt) {
	var files = evt.target.files;
	for (var i = 0, f; f = files[i]; i++) {
		document.getElementById("workspace").innerHTML += "<li class='respo-padding' " +
		"id='"+f.name+"'><span class='respo-medium'><strong>"+f.name+
		"</strong> \r\n("+ f.type + ") - "+f.size+"  bytes</span><a href='javascript:void(0)' onclick=this.parentElement.remove(); " +
		"class='respo-hover-white respo-right'><i class='fa fa-remove fa-fw'></i></a><br></li>";
		}

}
