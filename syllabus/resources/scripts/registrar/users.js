$(document).ready(function(){
    $('#usersTable').dataTable({
        "aaSorting": [[ 1, "asc" ]] ,
        "sDom": '<"userTableToolBar">frtip'
    });
    
    $('.userTableToolBar').bind('click',function(){
        addUser();    
    }).html('add user');;
    
    $('#name').watermark('Enter Name...');
    $('#perm').watermark('Enter Perm Number...');
    
    $('.user').on('mouseenter',function(){
        $(this).children('.userTools').eq(0).children().show();
    }).on('mouseleave',function(){
        $(this).children('.userTools').eq(0).children().hide();
    });
});

function userProfile(id){
    $.ajax({
        url: '/registrar/users/userProfile/',
        data: {
            id: id
        },
        success: function(data) {
            overlay(data);
        }
    });
}

function refreshUserList(){
    $.ajax({
        url:'/registrar/users/list/',
        success: function(data){ 
            $('.user').remove();
            $('tr:first-child').after(data);
            
            $('.user').on('mouseenter',function(){
                $(this).children('.userTools').eq(0).children().show();
            }).on('mouseleave',function(){
                $(this).children('.userTools').eq(0).children().hide();
            });
        }
    });
}


function  filterList(){
    
    $('.user').show()
    
    // filter out names that don't match
    var name = $('#name').val();
    if (name){
            $('.user').each(function(){
            if($(this).children().eq(0).html().indexOf(name) == -1){
                $(this).hide();
            }
        });  
    }
    
    // filter out ID
    
    var id = $('#perm').val();
    if (id){
            $('.user').each(function(){
            if($(this).children().eq(1).html().indexOf(id) == -1){
                $(this).hide();
            }
        });  
    }
    
    // filter out roles
    
    var role = $('#role').val();
    if (role){
            $('.user').each(function(){
            if($(this).children().eq(2).html().indexOf(role) == -1){
                $(this).hide();
            }
        });  
    }
}


function deleteUser(id){
    if (confirm("Are you sure you want to delete this user from the database?")){
        $.ajax({
            url:'/registrar/users/delete/',
            data:{
                id: id
            },
            success: function(data){
                $('#'+id).remove();
            }
        }); 
    }
}

function newUser(){
    $.ajax({
        url:'/registrar/users/new/',
        success: function(data){
            overlay(data);
        }
    });
}

function createUser(){
    if ($('#pass1').val() == $('#pass2').val()){ 
        var pass = $('#pass1').val();
    }
    
    $.ajax({
        url:'/registrar/users/create/',
        type: 'POST',
        data:{
            firstName : $('#firstName').val(),
            lastName: $('#lastName').val(),
            username: $('#username').val(),
            password : pass,
            email: $('#email').val(),
            role: $('#roleSelect').val()
            
        },
        success: function(data){
            closeOverlay();
            refreshUserList();
        }
    });
}

function editUser(id){
    $.ajax({
        url: '/registrar/users/edit/',
        data:{
            id: id
        },
        success: function(data){
            overlay(data);
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
        }
    });
}

function getInterestCourseNumbers(id, self){

    alert('hello');
    $.ajax({
        url:'/registrar/users/getInterestCourseNumbers',
        data: {
            id: id
        },
        success: function(data){
            $(this).parent().siblings('.courseNumbers').empty().append(data);
        }
    });
}


function newExemption(id){

    $.ajax({
        url: '/registrar/users/addExemption/',
        data: {
            id: id 
        },
        success: function(data){
            $('#userInfo').hide();
            $('#exemptionForm').empty().append(data).show();
        }
        
        
    });
}

function getPossibleClasses(id){

    $.ajax({

        url: '/registrar/users/getPossibleClassesForExemption/',
        data: {
            id: id
        },
        sucess: function(data){
            
        }

    });

}

