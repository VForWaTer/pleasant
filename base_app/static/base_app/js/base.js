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
function select_data() {
		
	var selectedData = document.getElementById("select_data").value;

	if (!document.getElementById(selectedData) && selectedData!=0){
		document.getElementById("workspace").innerHTML += "<li class='respo-padding' " +
		"id='"+selectedData+"'><span class='respo-medium'>"+selectedData+
		"</span><a href='javascript:void(0)' onclick=this.parentElement.remove(); " +
		"class='respo-hover-white respo-right'><i class='fa fa-remove fa-fw'></i></a><br></li>";
	}
}

function select_data2(evt) {
	var files = evt.target.files;
	var files = document.getElementsByName("files[]");
	var output = [];
	for (var i = 0, f; f = files[i]; i++) {
		output.push('<li><strong>', f.name, '</strong> (', f.type || 'n/a', ') - ',
                f.size, ' bytes</li>');
		}
    document.getElementById("workspace").innerHTML += '<ul>' + output.join('') + '</ul>';
//**	document.getElementById
//**	var newButton = document.createElement("INPUT");
//**    	newButton.setAttribute("type", "file");

}
//    document.getElementById("workspace").innerHTML += "<li class='respo-padding' id='"+x+"'><span class='respo-medium'>"+x+"</span><a href='javascript:void(0)' onclick=this.parentElement.remove(); class='respo-hover-white respo-right'><i class='fa fa-remove fa-fw'></i></a><br></li>";
//**    if (!document.getElementById(newButton) && newButton!=0){
 //   	document.body.appendChild(newButton);


//document.getElementById('files').addEventListener('change', dateiauswahl, false);

