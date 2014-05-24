function selectDay(date){
    if (date){
	$('.selectedDay').removeClass('selectedDay');
	$('#'+date).addClass('selectedDay');
    }
    
}

function eventDrag(target, event){
    event.dataTransfer.setData('id', target.id);
}

function eventDropMoveEvent(target, event){
    var label = event.dataTransfer.getData('id').split('label');
    var term = event.dataTransfer.getData('id').split('term');
    var date = $(target).attr('id');



    if (label[1]){
        
	$.ajax({
	    url: '/calendar/moveLabel/',
	    type: 'POST',
	    data:{ 
                id: label[1].split('-')[0],
                which: label[1].split('-')[1],
                date: date,
                type: 'group'
            },
	    success: function(data) {
	        $(target).find('.calendarDayLabel').append($('#'+ event.dataTransfer.getData('id')));
                
            }
        });
    } else if(term[1]) {
        $.ajax({
	    url: '/calendar/moveLabel/',
	    type: 'POST',
	    data:{ 
                id: term[1].split('-')[0],
                which: term[1].split('-')[1],
                date: date,
                type: 'term'
            },
	    success: function(data) {
	        $(target).find('.calendarDayLabel').append($('#'+ event.dataTransfer.getData('id')));
                
            }
        });
    } else {
        
        var id =  event.dataTransfer.getData('id');

	$.ajax({
	    url: '/calendar/moveEvent/',
	    type: 'POST',
	    data:{ 
                id: id,
                date: date
            }, 
	    success: function(data) {
	        $(target).find('.calendarDayBody').append($('#' + id));
	        $(target).find('.calendarWeekEvents').append($('#' + id));
            }
        });	
    }
    
    event.preventDefault();
}

function eventDropDeleteEvent(target, event){
    var id = event.dataTransfer.getData('id');
    deleteEvent(id);
    event.preventDefault();
}

function deleteEvent (id){

    if (confirm('Are you sure you want to delete this event?')){
	$.ajax({
	    url: '/calendar/deleteEvent/',
	    type: 'POST',
	    data: 'id=' +id,
	    success: function(data) {
		var which = $('#calendar').attr('which');
		var number = $('#calendar').attr('number');
		var year = $('#calendar').attr('year');
		
		
		loadCalendar(which, year, number);
		$('#' + id).remove();
	    }
	});	
    }
}

function editEvent(id){
    
    $.ajax({
	url: '/calendar/editEventForm/',
	data: 'id=' + id,
	success: function(data) {
	    overlay(data);
	}
    });
}

function submitEditEventForm(id){
    
    var dataString = "";
    
    var title = $('#editEventTitle').val();
    if (title != ""){
	dataString += "title=" + title;
    } else {
	$('#id_title').focus();
	return;
    }
    
    
    var category = $('#editEventCategory').val();
    if (category !=""){
	dataString += "&category=" + category;
    }else {
	$('#id_category').focus();
	return;
    }
    
    var date = $('#editEventDate').val();
    if (date !=""){
	dataString += "&date=" + date;
    }
    
    var time = $('#editEventTime').val();
    if (time !=""){
	dataString += "&time=" + time;
    }
    
    if ($('#possiblePoints').length > 0){
	var possiblePoints = $('#possiblePoints').val();
	dataString += "&possiblePoints=" + possiblePoints;
    }
    
    if ($('#associatedReading').length > 0){
	var associatedReading = $('#associatedReading').val();
	dataString += "&associatedReading=" + associatedReading;
    }
    
    var description = $('#editEventDescription').val();
    dataString += "&description=" + description;
    
    $.ajax({
	url: "/calendar/editEvent/",
	type: "POST",
	async: false,
	data: dataString + "&id=" + id,
	success: function(data) {
	    
	    var which = $('#calendar').attr('which');
	    var number = $('#calendar').attr('number');
	    var year = $('#calendar').attr('year');
	    
	    closeOverlay();
	    loadCalendar(which, year, number);
    	}
    });
}

function loadView(which){
    loadCalendar(which, $('#calendar').attr('year'), $('#calendar').attr('number'));
}

function loadCalendar(which, year, number){
    $.ajax({
	url: '/calendar/ajax/',
	async: false,
	data: 'which=' + which + "&year=" + year + '&number=' + number,
	success: function(data) {
	    // save the currently selected day
            var id = $('.selectedDay').attr('id');
            // update the calendar
            $("#calendar").replaceWith(data);
            // create the tooltips
            $('.tooltip').tooltipster({
                interactive: true,
                theme: 'eventTooltip'             
            });
            
    	}
    });
}

function refreshCalendar(){
    var which = $('#calendar').attr('which');
    var year = $('#calendar').attr('year');
    var number = $('#calendar').attr('number');
    
    loadCalendar(which, year, number);
}

function loadPrevCalendar(){
    var which = $('#calendar').attr('which');
    var number = $('#calendar').attr('number');
    var year = $('#calendar').attr('year');	
    
    if (which == 'month'){
	if (parseInt(number) == 1){
	    newYear = parseInt(year) - 1
	    if (which == "month"){
		loadCalendar(which, newYear, 12);
	    }
	}
	else {
	    newNumber = parseInt(number) - 1;
	    if (which == "month"){
		loadCalendar(which, year, newNumber);
	    }
	}
    } else {
	if (which == 'week'){
	    if (number > 1){
		var numberNew = parseInt(number) - 1;	
		loadCalendar(which, year, numberNew);
	    } else {
		var numberNew = 52;
		var yearNew = parseInt(year) - 1;
		loadCalendar(which, yearNew, numberNew);
	    }
	}
    }
}

function loadNextCalendar(){
    var which = $('#calendar').attr('which');
    var number = $('#calendar').attr('number');
    var year = $('#calendar').attr('year');	
    
    if (which == 'month'){
	if (parseInt(number) == 12){
	    newYear = parseInt(year) + 1
	    if (which == "month"){
		loadCalendar(which, newYear, 1);
	    }
	}
	else {
	    newNumber = parseInt(number) + 1;
	    if (which == "month"){
		loadCalendar(which, year, newNumber);
	    }
	}
    } else {
	if (which = 'week'){
	    var numberNew = parseInt(number) + 1;	
	    loadCalendar(which, year, numberNew);
	}
    }
}

function loadTodayCalendar(){
    var which = $('#calendar').attr('which');
    var number = $('#calendar').attr('todaynumber');
    var year = $('#calendar').attr('todayyear');
    
    loadCalendar(which, year, number);
}

function deleteEventFromButtonClick(){
    deleteEvent($('.selectedSidebarEvent').attr('id').substring(12));
}

function newEvent(category){
    var date = $('.selectedDay').attr('id');
    if (date != undefined){
	$.ajax({
	    data: {
		date: date,
		category: category
	    },
	    url: '/calendar/newEventForm/',
	    success: function(data) {
		overlay(data);
	    }
	});
    } else{
	alert('Please select a day');
    }
}

function selectSidebarEvent(id){
    $('.selectedSidebarEvent').removeClass('selectedSidebarEvent');
    $('#sidebarEvent' + id).addClass('selectedSidebarEvent');
}

function loadSections(){
    loadSectionByClassId($('#classId').find(':selected').attr('value'));
}

function closeEventForm(year, month, day){
    var which = $('#calendar').attr('which');
    var number = $('#calendar').attr('number');
    var year = $('#calendar').attr('year');
    var date = "" + year + "-" + month + "-" + day;
    closeOverlay();
    loadCalendar(which, year, number);
}

function removeFileUpload(self, id){
    var fileName = $(self).parent().children().eq(0).html();
    $(self).parent().empty().append($('<span/>').addClass('deletedFile').html('removed ' + fileName));
    $('[name="deletedFiles"]').attr('value', $('[name="deletedFiles"]').attr('value') + id + ',');
}

function loadSectionByClassId(id){
    if (id >0){
	$.ajax({
	    url: '/calendar/getSectionsById/',
	    data: 'id=' + id,
	    success: function(data) {
		
		$('#newEventFormSectionChoice').empty().prepend(data);
	    }
	    
	});
    } else {
	$('#newEventFormSectionChoice').empty();
    }
}

function selectView(which){
    
    var selectedDayId = $('.selectedDay').attr('id');
    var calWhich = $('#calendar').attr('which');
    
    // did they select a day?
    if (selectedDayId){
	
	if (which == 'month'){
	    if (calWhich == 'month'){
		return;
		
	    } else {
		if (calWhich == 'week'){
		    var year = $('#calendar').attr('year');
		    var number = selectedDayId.split('-')[1];
		    
		    loadCalendar(which, year, number);
		}	
	    }
	} else {
	    if (which == 'week'){
		
		if (calWhich == 'week'){
		    return;
		} else{
		    if (calWhich == 'month'){
			var year = $('#calendar').attr('year');
			var number = getWeekNumber($('#' + selectedDayId).attr('id'));
			
			loadCalendar(which, year, number);
		    }
		}
		
		
	    }
	}
    } else{
	if (which == 'month'){
	    if (calWhich == 'month'){
		return;
	    } else {
		if (calWhich == 'week'){
		    var year = $('#calendar').attr('year');
		    var number = $('#calendar').find('.calendarWeekDay').eq(4).attr('id').split('-')[1]
		    
		    loadCalendar(which, year, number);
		}
	    } 
	}else{
	    if (which == 'week'){
		if (calWhich == 'week'){
		    return;
		} else {
		    if (calWhich == 'month'){
			var year = $('#calendar').attr('year');
			var number = getWeekNumber($('#calendar').find('.calendarDay').eq(3).attr('id'));
			
			loadCalendar(which, year, number);
                        
		    }
		}
	    }
	}
    }
}

function getWeekNumber(date) {
    
    var d = new Date(date);
    
    var day = d.getDay();
    if(day == 0) day = 7;
    d.setDate(d.getDate() + (4 - day));
    var year = d.getFullYear();
    var ZBDoCY = Math.floor((d.getTime() - new Date(year, 0, 1, -6)) / 86400000);
    return 1 + Math.floor(ZBDoCY / 7);
}


function viewEventInfo(id){
    $.ajax({
	url: '/viewEvent/?id=' + id,
	success: function(data){
	    overlay(data);
	}
    });
}

function startTerm(){
    var date = $('.selectedDay').eq(0).attr('id')
    if (date) {
        $.ajax({
            url: '/calendar/newTermStart/',
            data: {
                date : date 
            }, 
            success: function (data) {
                overlay(data);
            } 

        });
    } else {
        alert('please select a day to start the term on');
    }
}

function endTerm(){
    var date = $('.selectedDay').eq(0).attr('id')
    if (date) {
        $.ajax({
            url: '/calendar/newTermEnd/',
            data: {
                date : date 
            }, 
            success: function (data) {
                overlay(data);
            } 

        });
    } else {
        alert('please select a day to startend the term on');
    }
}

function createTermEnd(date){
    $.ajax({
        url: '/calendar/createTermEnd/',
        type: 'POST',
        data: {
            date: date,
            id: $('#term').val()
        },
        success: function(data){
            refreshCalendar();
            closeOverlay();
        }
    });
}

function createTerm(date){
    $.ajax({
        url: '/calendar/createTerm/',
        type: 'POST',
        data: {
            date: date,
            name: $('#name').val()
        },
        success: function(data){
            refreshCalendar();
            closeOverlay();
        }
    });
}

function startRegistration(){
    var date = $('.selectedDay').eq(0).attr('id')

    if (date){
        $.ajax({
            url: '/calendar/startRegistration/',
            data: {
                date: date
            },
            success: function(data){
                overlay(data);
            }
        });
        
    } else {
        alert('Please select a day to start registration on');
    }
}

function endRegistration(){
    var date = $('.selectedDay').eq(0).attr('id')

    if (date){
        $.ajax({
            url: '/calendar/endRegistrationForm/',
            data: {
                date: date
            },
            success: function(data){
                overlay(data);
            }
        });
        
    } else {
        alert('Please select a day to start registration on');
    }
}

function createRegistration(date){
    $.ajax({
        url: '/calendar/createRegistration/',
        data: {
            date: date,
            name : $('#name').val(),
            term : $('#term').val()
        },
        type: 'POST',
        success: function(data){
            refreshCalendar();
            closeOverlay();
        }
    });
}

function setEndRegistration(date){
    $.ajax({
        url: '/calendar/endRegistration/',
        data: {
            date: date,
            id : $('#id').val(),
            term : $('#term').val()
        },
        type: 'POST',
        success: function(data){
            refreshCalendar();
            closeOverlay();
        }
    });
}


$(document).ready(function(){
    var which = $('#calendar').attr('which');
    var number = $('#calendar').attr('number');
    var year = $('#calendar').attr('year');
    
    loadCalendar(which, year, number);
    
    $('#prevMonthSelector').live('click',function(){
	loadPrevCalendar();
    });
    $('#nextMonthSelector').live('click',function(){
	loadNextCalendar();
    });
    $('#todayMonthSelector').live('click',function(){
	loadTodayCalendar();
    });
    
    
    
    setInterval( "refreshCalendar()", 300000 );
    
});
