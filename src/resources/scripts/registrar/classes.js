function newClass(id){ 
	$.ajax({
		url: '/registrar/classes/newClass/',
		data: 'id=' + id,
		success: function(data) {
			overlay(data);
        }
	});
}

function newCollege(){
    $.ajax({
        url:'/registrar/classes/newCollege/',
        success: function(data){
                overlay(data);
        }    
    });
}

function createCollege(){
    $.ajax({
        url: '/registrar/classes/createCollege/',
        type: 'POST',
        data: {
            name: $('#name').val()
        },
        success: function(data){
            updateColleges();
            closeOverlay();
        }
    });
}

function updateColleges(){
    var selected = $('.college.current').attr('id');
    $.ajax({
        url: '/registrar/classes/collegeList/',
        success: function(data){
                $('#departmentFilter').empty().append(data);
                $('#' + selected ).addClass('current');
        }
    });
}

function loadCollege(id){
    
    $.ajax({
        url: '/registrar/classes/departmentList/',
        data: {
            id: id
        },
        success: function(data){
            $('#departments').empty().append(data);
        }
    });
}

function newDepartment(id){
    $.ajax({
        url:'/registrar/classes/newDepartment/',
        data: {
            id: id
        },
        success: function(data){
                overlay(data);
        }    
    });
}

function createDepartment(id){
    $.ajax({
        url:'/registrar/classes/createDepartment/',
        data: {
            id: id,
            name: $('#name').val()
        },
        type: 'POST',
        success: function(data){
            updateDepartments(id);
            closeOverlay();
        }    
    });
}

function updateDepartments(id) {
    var selected = $('.department.current').attr('id');
    $.ajax({
        url: '/registrar/classes/departmentList/',
        data: {
            id: id
        },
        success: function(data){
                $('#departments').empty().append(data);
                $('#' + selected ).addClass('current');
        }
    });
}

function loadDepartment(id){
    
    $('.department.current').removeClass('current');
    $('#department'+id).addClass('current');
    
    $.ajax({
        url: '/registrar/classes/interestList/',
        data: {
            id: id
        },
        success: function(data){
                $('#profiles').empty().append(data);
        }
    });
}

function viewProfile(id){
    $.ajax({
        url: '/registrar/classes/profile/',
        data: {
            id: id
        },
        success: function(data){
            $('#classes').empty().append(data);
            $('#class'+id).addClass('current');
        }
    });
}

function newProfile(id){
    $.ajax({
        url:'/registrar/classes/newProfile/',
        data: {
            id: id
        },
        success: function(data){
                overlay(data);
        }    
    });
}

$(document).ready(function(){
    $('.department').eq(1).addClass('current');
    $('.class').eq(1).addClass('current');
});
