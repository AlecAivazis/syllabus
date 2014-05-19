function newTutor(){
    $.ajax({
	url: '/tutors/new/',
	success: function(data){
	    overlay(data);
	}

    });
}

