function login(){
    var username = $('#id_username').val();
    var password = $('#id_password').val();

    $.ajax({
	url: '/login/',
	type: 'POST',
	data: 'username=' + username + '&password=' + password,
	success: function(data){
	    window.location = '/';
	},
	error: function(){
	    $('<div/>').attr({
	    }).addClass('error').html('Your username/password combination was incorrect...').appendTo('#content').delay(10000).fadeOut('medium');
	} 
    });
}
