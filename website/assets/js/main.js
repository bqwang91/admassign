$(document).ready(function() {
	$.ajax({
	url: 'cgi-bin/main_page_handler.py',
	type: 'GET',
	data: {}
	})
	.done(function(data) {
		tokens = data.split('\t');
		if(tokens[0] == "success"){
			$("#welcome-message").html("Welcome User " + tokens[1]);
			var ul_html = "";
			for(i = 2; i < tokens.length; i++){
				ul_html += tokens[i];
			}
			$("#listening_counts ul:first").html(ul_html);
		}
		else{
			$("body").html(data)
		}
		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
});

/*
 *
 */
$("#get-data").on('click', function(event) {
	/* Act on the event */
	var $form = $("#query-form");
	var name = $form.find("input[name='name']").val();

	$.ajax({
	url: 'cgi-bin/test.py',
	type: 'GET',
	data: {name: name},
	})
	.done(function(data) {
		$("#result").html(data);
		console.log("success");
	})
	.fail(function() {
		console.log("error");
	})
	.always(function() {
		console.log("complete");
	});
});


