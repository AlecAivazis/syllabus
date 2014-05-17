function updateAddress(which){
    
    var root = '';
    var name = '';
    var phone = '';
    
    if (which == 'residential'){
        root = $('#addressResidential');
    } else if (which == 'permanent'){
        root = $('#addressPermanent');
    } else if (which == 'emergency'){
        root = $('#addressEmergency');
        name = $('#emergencyName').val();
        phone = $('#emergencyPhone').val();
    }
    
    $.ajax({
        url: '/myProfile/updateAddress/',
        type: 'POST',
        data: {
            line1 : $(root).children().eq(0).children('input').eq(0).val(),
            line2 : $(root).children().eq(1).children('input').eq(0).val(),
            city : $(root).children().eq(2).children('input').eq(0).val(),
            state : $(root).children().eq(3).children('input').eq(0).val(),
            zip : $(root).children().eq(4).children('input').eq(0).val(),
            country : $(root).children().eq(5).children('input').eq(0).val(),
            name: name,
            which: which,
            phone: phone
        }
    });
}

function updatePhone(){
    $.ajax({
        url: '/myProfile/updatePhone/',
        type: 'POST',
        data:{
            phone: $('#phone').val()    
        }
    });
}

function updateEmail(){
    $.ajax({
        url: '/myProfile/updateEmail/',
        type: 'POST',
        data:{
            email: $('#email').val()    
        }
    });
}
