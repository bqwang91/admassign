
/*
 * Submit login form on click of login button
 */
$("#log-in").on('click', function(event) {

	var $form = $("#login-form");
	var user_id = $form.find("input[name='user_id']").val();

	if(user_id == ""){
		$("#input_userid").addClass('has-error');
		$("#result").css('color','#a94442');
		$("#result").html("Please enter an user id");
	}
	else{
		$.ajax({
		url: 'cgi-bin/login.py',
		type: 'GET',
		data: {user_id: user_id},
		})
		.done(function(data) {
			if(data.trim() == "fail"){
				$("#input_userid").addClass('has-error');
				$("#result").css('color','#a94442');
				$("#result").html("No such user");
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
	}
	
});


/*
$("#logout-a").on('click', function(event) {


});
*/
