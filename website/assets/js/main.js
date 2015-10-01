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
			$("body").html(data);
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
$("#tag_name_submit").on('click', function(event) {
	/* Act on the event */
	var $form = $("#popular_artists_by_tag_form");
	var tag_name = $form.find("input[name='tag_search_name']").val();

	$.ajax({
	url: 'cgi-bin/get_popular_artists_by_tag.py',
	type: 'GET',
	data: {tag_name: tag_name},
	})
	.done(function(data) {
		tokens = data.split('\t')
		if(tokens[0] == "success"){
			$("#tag_listening_count ul:first").html(tokens[1]);
		}
		else{
			$("body").html(data);
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

$("#search_by_recommendation").on('click', function(event){
	/* Act on the event */
	var $form = $("#recommendation_form");
	var recommendation_type = $form.find("select[name='recommendation_type']").val();

	$.ajax({
	url: 'cgi-bin/get_artists_by_recommendation.py',
	type: 'GET',
	data: {recommendation_type: recommendation_type},
	})
	.done(function(data) {
		tokens = data.split('\t')
		if(tokens[0] == "success"){
			$("#artists_display").html(tokens[1]);		
		}
		else{
			$("body").html(data);
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

$("a.listen").on('click', function(event){
	/* Act on the event */
	var artist_id = $(this).attr('artist_id');

	$.ajax({
	url: 'cgi-bin/listen.py',
	type: 'GET',
	data: {artist_id: artist_id},
	})
	.done(function(data) {
		tokens = data.split('\t')
		if(tokens[0] == "success"){
			confirm("You have listened");		}
		else{
			$("body").html(data);
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

