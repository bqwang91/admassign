
$("#log-in").on('click', function(event) {
	/* Act on the event */
	var $form = $("#login-form");
	var name = $form.find("input[name='user_name']").val();

	$.ajax({
	url: 'cgi-bin/login.py',
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


/*
$("#logout-a").on('click', function(event) {


});
*/
