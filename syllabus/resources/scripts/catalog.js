function filterCatalog(){
    var dataDict = {
        term: $('[name="term"]').val()  
    };
    if ($('[name="interest"]').val()){
        dataDict['interest'] = $('[name="interest"]').val();
        if ($('[name="courseNumber"]').val()){
            dataDict['courseNumber'] = $('[name="courseNumber"]').val();
        }
    }
    
    if ($('[name="courseNumber"]').val()){
        dataDict['number'] = $('[name="number"]').val();
    }
    if ($('[name="timeStart"]').val()){
        dataDict['timeStart'] = $('[name="timeStart"]').val();
    }
    if ($('[name="timeEnd"]').val()){
        dataDict['timeEnd'] = $('[name="timeEnd"]').val();
    }
    if ($('[name="unitsUpper"]').val()){
        dataDict['unitsUpper'] = $('[name="unitsUpper"]').val();
    }    
    if ($('[name="unitsLower"]').val()){
        dataDict['unitsLower'] = $('[name="unitsLower"]').val();
    }
    if ($('[name="timeEnd"]').val()){
        dataDict['timeEnd'] = $('[name="timeEnd"]').val();
    }
    if ($('[name="enrollCode"]').val()){
        dataDict['enrollCode'] = $('[name="enrollCode"]').val();
    }
    if ($('[name="instructor"]').val()){
        dataDict['instructor'] = $('[name="instructor"]').val();
    }
    var days = '';
    $('[name="day"]').each(function(){
        if($(this).is(':checked')){
            days = days + $(this).val() + '-';
        }
    });
    if (days){
        dataDict['days'] = days;
    }
    
    $.ajax({
        url: '/myClasses/filterCatalog/',
        data: dataDict,
        success: function(data){
            $('#catalog').empty().append(data);
        }
    });
    
}

function checkCatalog(){
    if ($('.course').length == 0){
        $('#classList').append('No classes were found that matched your criteria...')
    }
}

function toggleAdvancedFilters(){
    $('#catalogAdvancedFilter').toggle();
}

function confirmAddSection(id, Switch, which){
    $.ajax({
        url: '/myClasses/catalog/confirmAddSection/',
        data: {
            id: id,
            zwitch: Switch,
            which: which
        },
        success: function(data){
            overlay(data);
        }
    });
}

function addSection(id){
    $.ajax({
        url: '/myClasses/catalog/addSection/',
        data: {
            id: id
        },
        type: 'POST',
        success: function(data){
            closeOverlay();
            filterCatalog();
        }
    });
}

$(document).ready(function(){
    $('select').change(function (){
        filterCatalog();
    });
    $('input').change(function (){
        filterCatalog();
    });
    
    $('[name="units"]').keydown(function(event) {
        // Allow: backspace, delete, tab, escape, and enter
        if ( event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 || event.keyCode == 27 || event.keyCode == 13 || 
             // Allow: Ctrl+A
            (event.keyCode == 65 && event.ctrlKey === true) || 
             // Allow: home, end, left, right
            (event.keyCode >= 35 && event.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
        }
        else {
            // Ensure that it is a number and stop the keypress
            if (event.shiftKey || (event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105 )) {
                event.preventDefault(); 
            }   
        }
    });

});
