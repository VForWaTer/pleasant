$(function() {
	clearURL = "{% url 'base_app:clear_database' %}";

	/* 1. OPEN THE FILE EXPLORER WINDOW */
	$(".js-upload-files").click(function() {
		$("#fileupload").click();
	});

	/* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
	$("#fileupload").fileupload({
		dataType : 'json',
		done : function(e, data) { /* 3. PROCESS THE RESPONSE FROM THE SERVER */
			if (data.result.is_valid) {
				$("#gallery tbody").prepend(
					"<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>")
				$("#workspace div").prepend(
					"<strong><a href='" + data.result.url + "'>" + data.result.name + "</a></strong>");
				$("#workspace div").prepend(
					"<form method='post' action=" + clearURL + "> " +
					"<input type='hidden' name='next' value='{{ request.path }}'>" +
					"<button type='submit' class='btn btn-danger pull-right'>" +
					" Y</button></form> ");
			
					
				}
			}
		});
});
