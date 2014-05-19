$(document).ready(function(){
    $('.filter').watermark('Search Majors...');
    $('input.filter').on('change',function(){
        if ($('.filter').val()){
            $('.major').show();
            $('.major').each(function(){
                if($(this).html().indexOf($('.filter').val()) == -1){
                    $(this).hide();    
                }

            });
        } else {
            $('.major').show();
        }
    });
    
    $('.major').on('click',function(){
        $('.current').removeClass('current');
        $(this).addClass('current');
    });
    $('.college').on('click',function(){
        $('.current').removeClass('current');
        $(this).addClass('current');
    });
});

function viewCollegeDegree(id){
    $.ajax({
        url:'/registrar/graduationRequirements/viewCollegeDegree/',
        data:{
            id: id    
        },
        success: function(data){
            $('#degree').empty().append(data);
        }
    });
}

function viewDegree(id, type){
    $.ajax({
        url: '/registrar/graduationRequirements/viewDegree/',
        data: {
            id: id,
            type: type
        },
        success: function(data) {
            $('#degree').empty().append(data);
            
            if (type){
                $('.degree').each(function(){
                    if ($(this).html() == type){
                        $(this).addClass('current');   
                    }
                });
            } else {
                $('.degree').eq(0).addClass('current');
            }
        }
    });
}

function newCollegeRequirement(id){
    
    $.ajax({
        url:'/registrar/graduationrequirements/newCollegeRequirement/',
        data:{
            id: id,
        },
        success: function(data) {
            overlay(data);
        }
    });
}

function newRequirement(id){
    
    $.ajax({
        url:'/registrar/graduationrequirements/newRequirement/',
        data:{
            major: id,
            type: $('.degree.current').html()
        },
        success: function(data) {
            overlay(data);
        }
    });
}

function editRequirement(id){
    $.ajax({
        url:'/registrar/graduationrequirements/editRequirement/',
        data:{
            id:id
        },
        success: function(data) {
            overlay(data);
        }
    });
}

function profilesByInterest(self, interest){
    
    $.ajax({
        url: '/registrar/graduationRequirements/profilesByInterest/',
        data: {
            interest: interest
        },
        success: function(data){
            $(self).siblings('#profileList').eq(0).empty().html(data);
        }
    });
}

function selectedProfile(){
    var id = $('.formLine').eq(-1).children('#profileList').val();
    if (id){
        if(Math.floor(id) == id && $.isNumeric(id)){
            var clone = $('.formLine:not(:last-child)').eq(-1).clone();  
            $('.formLine').eq(-1).after(clone);
            
            $(clone).children('#profileList').children(':not(:first-child)').remove();
        }
    }
}

function submitCollegeRequirement(idd){
    var name = $('.formLine').eq(0).children('input').val();
    var abbrv = $('.formLine').eq(1).children('input').val();
    var number = parseInt($('.formLine').eq(2).children('input').val());
    var minGrade = parseInt($('.formLine').eq(3).children('input').val());
    var classes = '';
    $('.formLine').not(':last-child').not(':first-child').each(function(){
        var id = $(this).children('#profileList').val();
        if (id){
            if( Math.floor(id) == id && $.isNumeric(id)){
                classes = classes + id + ','
            }
        }
    });
    

    $.ajax({
        url: '/registrar/graduationRequirements/submitCollegeRequirement/',
        type: 'POST',
        data: {
            number : number,
            classes : classes,
            minGrade : minGrade,
            name: name,
            id: idd,
        },
        success: function(data){
            closeOverlay();
            viewCollegeDegree(idd, $('.degree.current').html());
        }
    });
}

function submitRequirement(idd){
    var number = parseInt($('.formLine').eq(0).children('input').val());
    var minGrade = parseInt($('.formLine').eq(1).children('input').val());
    var classes = '';
    $('.formLine').not(':last-child').not(':first-child').each(function(){
        var id = $(this).children('#profileList').val();
        if (id){
            if( Math.floor(id) == id && $.isNumeric(id)){
                classes = classes + id + ','
            }
        }
    });
    

    $.ajax({
        url: '/registrar/graduationRequirements/submitRequirement/',
        type: 'POST',
        data: {
            number : number,
            classes : classes,
            minGrade : minGrade,
            id: idd,
            level: $("input:checked").val()
        },
        success: function(data){
            closeOverlay();
            viewDegree(idd, $('.degree.current').html());
        }
    });
}

function updateMajors(){
    $.ajax({
        url: '/registrar/graduationRequirements/majorList/',
        success: function(data) {
            $('.major').remove();
            $('.filter').parent().after(data);
        }
    });
}

function createMajor() {
    $.ajax({
        url: '/registrar/graduationRequirements/createMajor/',
        type: 'POST',
        data: {
            college: $('#college').val(),
            name: $('#name').val(),
            type: $('#type').val()
        },
        success: function(data){
            updateMajors();
            closeOverlay();
        }
    });
}

function newMajor(){
    $.ajax({
        url: '/registrar/graduationRequirements/newMajor/',
        success: function(data){
            overlay(data);
        }
    });
}

function deleteRequirement(id){
    if (confirm('Are you sure you want to delete this requirement?')){
        $.ajax({
        url: '/registrar/graduationrequirements/deleteRequirement',
        data:{
            id: id
        },
        success: function(data){
            if ($('.degree.current').length > 0){
                $('.degree.current').click();
            } else {
                $('.college.current').click();
            };
        }
    });
    }
}

function modifyRequirement(idd){
    var number = parseInt($('.formLine').eq(0).children('input').val());
    var minGrade = parseInt($('.formLine').eq(1).children('input').val());
    var classes = '';
    $('.formLine').not(':last-child').not(':first-child').each(function(){
        var id = $(this).children('#profileList').val();
        if (id){
            if( Math.floor(id) == id && $.isNumeric(id)){
                classes = classes + id + ','
            }
        }
    });
    

    $.ajax({
        url: '/registrar/graduationRequirements/modifyRequirement/',
        type: 'POST',
        data: {
            number : number,
            classes : classes,
            minGrade : minGrade,
            id: idd,
            level: $("input:checked").val()
        },
        success: function(data){
            closeOverlay();
            viewDegree(idd, $('.degree.current').html());
        }
    });
}