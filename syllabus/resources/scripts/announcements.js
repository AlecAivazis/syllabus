function newAnnouncement(){
    $.ajax({
        url: '/announcements/newAnnouncement/',
        success: function(data){
            overlay(data);
        }
    });
}

function submitNewAnnouncement(){
    
    var check = '';
    
    $(':checked').each(function(){
        check = check + $(this).attr('value') + ',';
    });
    
    alert(check);
    
    $.ajax({
        url: '/announcements/create',
        type: 'POST',
        data: {
            'title': $('#newAnnouncementTitle').val(),
            'message': $('#newAnnouncementBody').val(),
            'to': check
        },
        success: function(data){
            closeOverlay();
            $('.selected').trigger('click');
        }
    });
}

function viewAnnouncements(self, type, id){
    $('.selected').removeClass('selected');
    $(self).addClass('selected');
    $.ajax({
        url:'/announcements/view/',
        data:{
            'type': type,
            'id': id
        },
        success: function(data){
            $('#announcements').empty().append(data);
        }
    });
    
}

$(document).ready(function(){
    $('.filterAnnouncements').eq(0).trigger('click');    
});
