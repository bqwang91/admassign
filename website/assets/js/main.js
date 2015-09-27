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
			var ul_one_html = tokens[2];
			var ul_two_html = tokens[3];

			$("#listening_counts ul:first").html(ul_one_html);
			$("#number_of_users ul:first").html(ul_two_html);
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
$("#query-by-name").on('click', function(event) {
	/* Act on the event */
	var $form = $("#query-form");
	var artist_name = $form.find("input[name='artist_name']").val();

	$.ajax({
	url: 'cgi-bin/get_artist_by_name.py',
	type: 'GET',
	data: {artist_name: artist_name},
	})
	.done(function(data) {
		tokens = data.split('\t')
		if(tokens[0] == "success"){
			$("#artists_display").html(tokens[1]);
		}
		else{
			$("body").html = data
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


