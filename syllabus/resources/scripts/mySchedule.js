function to12Hrs(strHrs, strMin) {            
    var hrs = Number(strHrs);
    var min = Number(strMin);
    var ampm = "am";

    if(isNaN(hrs) || isNaN(min) || hrs > 23 || hrs < 0)   {
       throw ("Invalid Date " + str24Hrs);
    }           

    if(hrs >= 12)   {
       hrs = (hrs - 12) || 12;
    }
    var strHr = hrs
    var strMin = (min < 10) ? "0".concat(min) : min;
    return (strHr + ":" + strMin);
 }

function refreshCalendar(term, year){
    $("#calendar").replaceWith('<div id="calendar"></div>');
    loadCalendar(term, year);
    
}

function loadCalendar(term, year){
    var $calendar = $('#calendar');
    var id = 10;
    
    $calendar.weekCalendar({
        displayOddEven:true,
        timeslotsPerHour : 2,
        firstDayOfWeek : 0,
        businessHours :{start: 8, end: 23, limitDisplay: true },
        daysToShow : 7,
        showTimes: false,
        showTitle: true,
        showIndividualDate: false,
        readonly: true,
        height : function($calendar) {
           return 665;
        },
        allowCalEventOverlap: true,
        
        data : function(start, end, callback) {
           //callback(getEventData());
           callback(getClasses(term,year));
        }
    });
    
    var sunday = new Date(2012,8,1);
    
    $calendar.weekCalendar("gotoWeek", new Date(2012,0,8));
}

function getClasses(term, year) {
    var eventz = Array();

    $.ajax({
        url: '/myClasses/getSchedule/',
        data: {
             term: term,
             year : year
        },
        async: false,
        success: function(data) {
            
            infos = data.split('__');
           
            for (var i = 0; i < infos.length; i++){
                
                
                info = infos[i].split(',,');
                
                day = info[0];
                start = info[1];
                end = info[2];
                id = info[3];
                name = info[4];
                
                if (info.length == 6) {
                    description = info[5];
                } else {
                    description = ''                
                }
                

                eventz.push({
                    'id' : id,
                    'start' : new Date(2012, 0,8+parseInt(day), start.split(":")[0], start.split(":")[1]),
                    'end' : new Date(2012, 0,8+parseInt(day), end.split(":")[0], end.split(":")[1]),
                    'title': ''+name+'<br>'+ to12Hrs(start.split(":")[0],start.split(":")[1]) + ' - ' + to12Hrs(end.split(":")[0],end.split(":")[1]) + '<br>' + description
                    }
                );
            }
            
        }
    });
    return {
       events : eventz
    };
 }

function confDrop(id){
    $.ajax({
        url:'/myClasses/confDrop',
        type: 'GET',
        data: {
            id: id
        },
        success: function(data){
            overlay(data);
        }
    });
}

function drop(id){
    if (confirm("Are you sure you want to drop this class?")){
        $.ajax({
        url: '/myClasses/runTask/',
        type: 'GET',
        data: {
            cmd : 'drop',
            id: id
        },
        success: function(data){
            closeOverlay();
            refreshInfoTable();
            $('#alertArea').empty().html(data).show().delay(5000).slideUp(1000);
            loadCalendar($('#calendar').attr('name'),$('#calendar').attr('year'));
        }
        });
    } else {
        
    }
}



function refreshInfoTable(){
    $.ajax({
        url: '/myClasses/courseInfoTable',
        success: function(data){
            $('#classInfoTable').empty().html(data);
        }
    });
}

$(document).ready(function() {
    loadCalendar($('#calendar').attr('name'),$('#calendar').attr('year'));
    
});

