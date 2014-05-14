function viewEventInfo(which){
	$.ajax({
		url: '/viewEvent/?id=' + which,
		success: function(data){
			overlay(data);
		}
	});
}

function turnedIn(number, filename, overwrite){
    
    if (overwrite){
    } else{
        $('#turnInFormContainer' + number).before(filename + '<br>');
        
        if ($("parent > div.show").length > 0){
            alert('hello');
        }

    }
    if(! $('#turnInFormContainer' + number).parent().siblings('.turnedInHeader').length){
        $('#turnInFormContainer' + number).parent().before('<div class="turnedInHeader">Uploaded:</div>');
    }
    $('#turnInForm' + number).children('.turnIn').empty().append('Upload Another Document').siblings('span .turnInSubmit').hide();;
}

function ignoreEvent(self, event, user){
    $.ajax({
        url: '/updateState/',
        type: 'POST',
        data: 'user=' + user + '&owner=' + user + '&event=' + event + '&status=ignored',
        success: function(){
            var assignment = $(self).parent().parent().parent().parent();
            var classDesc = assignment.parent();
            var late = $('#LateAssignments');
            
            if (classDesc.children().size() > 1 ){
                assignment.remove();
            } else{
                if (late.children('.class').size() > 1 ){
                    classDesc.parent().remove();
                } else {
                    late.remove();
                }
            }    
        }
    });
}

function completeEvent(self, event, user){
    if ($(self).attr('checked') != "true"){
        $.ajax({
            url: '/updateState/',
            type: 'POST',
            data: 'user=' + user + '&owner=' + user + '&event=' + event + '&status=turned-in',
            success: function(){
                $('#turnInFormContainer' + event).hide();
                $(self).css('background','url(/resources/images/checkmark.png)').attr('checked','true');
            }
        });
	} else{
        $.ajax({
            url: '/updateState/',
            type: 'POST',
            data: 'user=' + user + '&owner=' + user + '&event=' + event + '&status=revoked',
            success: function(){
                $('#turnInFormContainer' + event).show();
                $(self).css('background','white').attr('checked','');
            }
        });
		
	}
}

function selectedFile(self){
    $(self).siblings('span .turnIn').html($(self).val());
    $(self).siblings('span .turnInSubmit').show();
}

$(document).ready(function(){
    $('.nextWeekEvent').click(function(e){
        e.stopPropagation();
    });
    
    var GET = getUrlVars();
    $('#'+GET['when']+' li').addClass('current');
});

