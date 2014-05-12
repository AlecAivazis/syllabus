/*
 $(document).ajaxStart(function() {
    $('body').css('cursor','wait');
}).ajaxStop(function(){
    $('body').css('cursor','default');
});
*/

function nyi(){
    alert("not yet implimented");
}

$(document).ready(function(){
    var base = window.location.href.split('/')[3].toLowerCase();
    if (base){
        if (base == 'registrar'){
            var stem = window.location.href.split('/')[4].toLowerCase();
            $('[href="/registrar/'+stem+'/"]').addClass('navCurrent');
        }else {
            $('#nav_'+base).addClass('navCurrent');
        }
    }else {
        $('#nav_home').addClass('navCurrent');
    }
});

function courseInfo(id){
    $.ajax({
        url: '/viewClass/',
        data: {
            class: id,
        },
        success: function(data){
            overlay(data);
        }
    });
}

function getUrlVars()
{
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}
