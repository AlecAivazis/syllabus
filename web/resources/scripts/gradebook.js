function selectSection(event, self, classId, sectionId){
    event.stopPropagation();
    viewGradeBook(self, classId, sectionId);
}

function viewGradeBook(self,classId, sectionId){
    $('.selectedSection').removeClass('selectedSection');
    
    
    var dataString = 'classId=' + classId;
    
    if (sectionId){
	dataString = dataString + '&sectionId=' + sectionId;
	$(self).addClass('selectedSection');
    } else {	
	$(self).children('.gradeBookSelectLabel').addClass('selectedSection');
    }
    
    
    $.ajax({
	url: '/gradebook/viewGradeBook/',
	data: dataString,
	success: function(data){
	    $('#gradeBookContent').html(data);
	    updateGradeBook();

	    $('.eventLabel').bind('click',function(event){
		clearGradeBookSelection();
		event.stopPropagation();
		
		var index = $(this).index();
		$(this).addClass('highlighted').addClass('selectedEvent');
		$('.gradeBookStudent').each(function(){
		    $(this).children().eq(index).addClass('highlighted')
                           .bind('click',function(event){event.stopPropagation();});
		    $('#averages').children().eq(index).addClass('highlighted');
		});
	    });
	    
	    $('.studentName').bind('click', function(event){
		event.stopPropagation();
		clearGradeBookSelection();
		$(this).parent().addClass('selectedStudent').addClass('highlighted');
	    });
	    
	    
	    $('.eventLabel').hover(
		
		//mouse enter				   
		function() {
		    var index = $(this).index();
		    $(this).addClass('highlighted');
		    $('.gradeBookStudent').each(function(){
			$(this).children().eq(index).addClass('highlighted');
			$('#averages').children().eq(index).addClass('highlighted');
		    });
		    
		// mouse leave
		}, function() {
		    if (!$(this).hasClass('selectedEvent')){
			$(this).removeClass('highlighted');
			var index = $(this).index();
			$('.gradeBookStudent').each(function(){
			    $(this).children().eq(index).removeClass('highlighted');
			    $('#averages').children().eq(index).removeClass('highlighted');
			});	
		    }
		});
	    
	    $('.gradeBookTool').click(function(event){event.stopPropagation();});
	    
	}
    });
}

function updateGradeBook(){
    
    $('.gradeBookStudent').each(function(){
	$(this).children().eq(1).each(function(){
	    updateTotalGrade($(this));	
	});	
    });
    
    calculateAverages();
    updateWeights();
}



function calculateAverages(){
    $('#averages').children().not(':first').not(':nth-child(2)').each(function(){
	var me = $(this).index();
	var total = 0;
	var number = 0;
	var possiblePoints =  $('thead').find('tr').children().eq(me).find('.eventPossiblePoints').html().trim(); 
 	$('.gradeBookStudent').each(function(){
	    if ($(this).children().eq(me).html().trim() != '__'){
		number ++;
		total = total + parseInt($(this).children().eq(me).children('span').eq(0).html());
	    }
	});
	
	if (number != 0 && possiblePoints != '--' && total){
	    var string = '';
	    string = string + Math.round(total/number * 10) / 10;
	    $(this).html(string + ' / ' + possiblePoints);
	} else{
 	    $(this).html('n/a');
	}
    });
    
}

function selectClass(self, id){
    $('.selectedClass').removeClass('selectedClass');
    $('.selectedSection').removeClass('selectedClass');
    $('#'+id).find('.gradeBookClassSelectLabel').find('div').addClass('selectedClass');
    $('#'+id).find('.gradeBookClassSelectLabel').addClass('selectedClass');
    
    viewGradeBook(self,id);
}

function rotate(object, degrees) {
    object.css({
        '-webkit-transform' : 'rotate('+degrees+'deg)',
        '-moz-transform' : 'rotate('+degrees+'deg)',  
        '-ms-transform' : 'rotate('+degrees+'deg)',  
        '-o-transform' : 'rotate('+degrees+'deg)',  
        'transform' : 'rotate('+degrees+'deg)',  
        'zoom' : 1

    });
}

function viewSections(event, id){
    event.stopPropagation();
    
    var $arrow = $('#'+id).children('div').eq(0).children('img').eq(0);
    rotate($arrow, 90);
    
    $('#'+id).children('.classSection').toggle();
    
    $arrow.attr('onclick', 'hideSections(event, '+ id +')');
}

function hideSections(event, id){
    event.stopPropagation();
    $('#'+id).children('.classSection').toggle();
    
    var $arrow = $('#'+id).children('div').eq(0).children('img').eq(0);
    rotate($arrow, 0);
    $arrow.attr('onclick','viewSections(event, '+ id+')');
    
}

function displayMessage(message){
    $('#gradeBookError').empty().append(message).show().delay(8000).fadeOut('slow');
}

function print(){
    alert('you want to print');
}

function loadEvent(self, id){
    var me = $(self);
    
    $.ajax({
	method: 'GET',
	data: 'id=' + id,
	url: '/gradebook/loadEvent/',
	success: function(data){
	    $(me).parent().parent().empty().append(data);
	}
    });
}


function updatePossiblePoints(self, id){
    $.ajax({
	url: '/gradeBook/changePossiblePoints/',
	data: 'id=' + id + '&value=' + $(self).html(),
	type: 'POST',
	success: function(data){
	    updateGradeBook();
	    $(self).parent().attr('possiblePoints', $(self).html());
	    
	}
    });
    
}

function changeCategory(self, id){
    $.ajax({
	url: '/gradeBook/changeCategory/',
	type: 'POST',
	data: 'id=' + id + '&value=' + $(self).html().replace('<br>',''),
	success: function(data){
	    updateGradeBook();
	}
    });
}

function addGradeEntry(self){
    
    var student = $(self).parent().siblings().eq(0).attr('value');
    var score = $(self).html();
    var event = $('thead').find('tr').children().eq($(self).parent().index()).attr('value');
    
    var dataString = 'student=' + student + '&score=' + score + '&event=' + event;
    
    if (score != '__'){''
	$.ajax({
	    type: 'POST',
	    data: dataString,
	    url: '/gradebook/addgrade/',
	    success: function(data){
		updateGradeBook(self);
	    }
	});
	              }
}

function updateTotalGrade(self){
    var studentId = $(self).siblings().eq(0).attr('value');
    var classId = $('#gradeBookBreadCrumbs').attr('class');

    $.ajax({
	url: '/gradebook/totalGrade/',
	data: 'studentId=' + studentId + '&classId=' + classId,
	success: function(data){
	    $(self).empty().append(data);
	    
	    var totalGradeTotal = 0.0;
	    var totalGradeNumber = 0.0;
	    
	    $('.gradeBookStudent').each(function(){
		if ($(this).find('.score').html() != 'n/a'){
		    var val = $(this).find('.totalGrade').find('.score').html();
		    if (val){
			totalGradeTotal = totalGradeTotal + parseFloat(val.substring(0,val.length-1));
			totalGradeNumber ++;
		    }
		}
	    });
	    
	    var string = '' +Math.round(totalGradeTotal/totalGradeNumber * 10) / 10 ;
	    
	    
	    if (string != "NaN"){
		$('#totalAverage').empty().append( string + '%');	
	    } else {
		$('#totalAverage').empty().append('n/a');
	    }
	    
	    
	    
	}
    });

}

function closeStat(){
    $('#stat').remove();
    $('#statReturn').remove();
    $('#statTitle').remove();
    $('#gradeBookViewBody').children().show();
    $('#gradingScaleSelect').show();
}

function performance(){
    
    var series = new Array();
    var earned = 0;
    var total = 0;
    var title = 'Performance '
    var index = 0;
    
    if ($('.selectedStudent').is('*')){
	$('.selectedStudent').children().not(':first').not(':nth-child(2)').each(function(){
	    if ($(this).html().trim() != '__' && $('thead').find('tr').children().eq($(this).index()).attr('possiblePoints') != '--'){
		earned = earned + parseInt($(this).children('span').eq(0).html());
		total = total + parseInt($('thead').find('tr').children().eq($(this).index()).attr('possiblePoints'));
		series.push([index, Math.round(earned/total * 100)]);
		index ++;
	    }
	    
	});
	
	title = title + 'of ' + $('.selectedStudent').children().eq(0).html() ;

    } else {
	$('#averages').children().not(':first').not(':nth-child(2)').each(function(i){
	    if ($(this).html().trim() != 'n/a' && $('thead').find('tr').children().eq($(this).index()).attr('possiblePoints') != '--'){
		earned = earned + parseInt($(this).html());
		total = total + parseInt($('thead').find('tr').children().eq($(this).index()).attr('possiblePoints'));
		series.push([index, Math.round(earned/total * 100)]);
		index ++;
	    }
	});
	
	title = title + 'of Entire Class (Average)'
	
    }
    
    $('#gradeBookViewBody').children().hide();
    $('#gradingScaleSelect').hide();
    $('#statReturn').remove();
    $('#statTitle').remove();
    $('#stat').remove();
    $('<div/>').attr({
	id: 'statReturn'
    }).html('return to grade book').appendTo('#gradeBookViewBody');
    
    $('<div/>').attr({
	id: 'statTitle'
    }).html(title).appendTo('#gradeBookViewBody');
    
    $('<div/>').attr({
	id: 'stat',
	style: 'height:400px; width:90%; margin-left:5%;'
    }).appendTo('#gradeBookViewBody');
    
    $.plot($("#stat"), [
	{ label: null,  data: series},
    ], {
	series: {
	    lines: {
		show: true,
		fill: true
	    },
	    points: {
		show: true,
		fill: false
	    },
	    color: '#00a8ff'
	},
	xaxis: {
	    ticks: 0,
	    min: 0
	},
	grid: {
	    backgroundColor: { colors: ["#fff", "#f8f8f8"] },
	    hoverable: true
	}
    });
    
    // create tooltip
    
    var previousPoint = null;
    $("#stat").bind("plothover", function (event, pos, item) {
        $("#x").text(pos.x.toFixed(2));
        $("#y").text(pos.y.toFixed(2));

        if (item) {
            if (previousPoint != item.dataIndex) {
                previousPoint = item.dataIndex;
                
                $("#tooltip").remove();
                var y = item.datapoint[1].toFixed(2);
                
                showTooltip(item.pageX, item.pageY, y);
            }
        }
        else {
            $("#tooltip").remove();
            previousPoint = null;            
        }
    });
}

function timeline(){
    
    var series = new Array();
    var earned = 0;
    var total = 0;
    var title = 'Timeline '
    var index = 0;
    
    if ($('.selectedStudent').is('*')){
	$('.selectedStudent').children().not(':first').not(':nth-child(2)').each(function(){
	    if ($(this).html().trim() != '__' && $('thead').find('tr').children().eq($(this).index()).attr('possiblePoints') != '--'){
		earned = parseInt($(this).children('span').eq(0).html());
		total = parseInt($('thead').find('tr').children().eq($(this).index()).attr('possiblePoints'));
		series.push([index, Math.round(earned/total * 100)]);
		index ++;
	    }
	    
	});
	
	title = title + 'for ' + $('.selectedStudent').children().eq(0).html() ;

    } else {
	$('#averages').children().not(':first').not(':nth-child(2)').each(function(i){
	    if ($(this).html().trim() != 'n/a' && $('thead').find('tr').children().eq($(this).index()).attr('possiblePoints') != '--'){
		earned = parseInt($(this).html());
		total = parseInt($('thead').find('tr').children().eq($(this).index()).attr('possiblePoints'));
		series.push([index, Math.round(earned/total * 100)]);
		index ++;
	    }
	});
	
	title = title + 'for Entire Class (Average)'
	
    }
    
    $('#gradeBookViewBody').children().hide();
    $('#gradingScaleSelect').hide();
    $('#statReturn').remove();
    $('#statTitle').remove();
    $('#stat').remove();
    $('<div/>').attr({
	id: 'statReturn'
    }).html('return to grade book').appendTo('#gradeBookViewBody');
    
    $('<div/>').attr({
	id: 'statTitle'
    }).html(title).appendTo('#gradeBookViewBody');
    
    $('<div/>').attr({
	id: 'stat',
	style: 'height:400px; width:90%; margin-left:5%;'
    }).appendTo('#gradeBookViewBody');
    
    $.plot($("#stat"), [
	{ label: null,  data: series},
    ], {
	series: {
	    lines: {
		show: true,
		fill: true
	    },
	    points: {
		show: true,
		fill: false
	    },
	    color: '#00a8ff'
	},
	xaxis: {
	    ticks: 0,
	    min: 0
	},
	grid: {
	    backgroundColor: { colors: ["#fff", "#f8f8f8"] },
	    hoverable: true
	}
    });
    
    // create tooltip
    
    var previousPoint = null;
    $("#stat").bind("plothover", function (event, pos, item) {
        $("#x").text(pos.x.toFixed(2));
        $("#y").text(pos.y.toFixed(2));

        if (item) {
            if (previousPoint != item.dataIndex) {
                previousPoint = item.dataIndex;
                
                $("#tooltip").remove();
                var y = item.datapoint[1].toFixed(2);
                
                showTooltip(item.pageX, item.pageY, y);
            }
        }
        else {
            $("#tooltip").remove();
            previousPoint = null;            
        }
    });
}

function showTooltip(x, y, contents) {
    $('<div id="tooltip">' + contents + '</div>').css( {
	position: 'absolute',
	display: 'none',
	top: y + 5,
	left: x + 5,
	border: '2px solid #00a8ff',
	padding: '2px',
	'background-color': 'white'
    }).appendTo("body").fadeIn(200);
}

var previousPoint = null;

$("#stat").bind("plothover", function (event, pos, item) {
    alert('hello');
    $("#x").text(pos.x.toFixed(2));
    $("#y").text(pos.y.toFixed(2));

    if (item) {
	if (previousPoint != item.dataIndex) {
	    previousPoint = item.dataIndex;
	    
	    $("#tooltip").remove();
	    var x = item.datapoint[0].toFixed(2),
	    y = item.datapoint[1].toFixed(2);
	    
	    showTooltip(item.pageX, item.pageY,
			item.series.label + " of " + x + " = " + y);
	}
    }
    else {
	$("#tooltip").remove();
	previousPoint = null;            
    }
});

function weights(){
    dataString = '';
    if ($('#gradeBookBreadCrumbs').attr('class')){
	dataString = 'class=' + $('#gradeBookBreadCrumbs').attr('class');
    }
    
    $.ajax({
	url: '/gradebook/weights/view',
	data: dataString,
	success: function(data){
	    $('#weightsWidget').remove();
	    $('<div/>').attr({
		id: 'weightsWidget'	
	    }).css('position','absolute').html(data).appendTo('#gutter');
	}
    });
}

function showGradingScale(){
    dataString = '';
    if ($('#gradeBookBreadCrumbs').attr('class')){
	if ($('#gradeBookBreadCrumbs').attr('section')){
	    dataString = 'section=' + $('#gradeBookBreadCrumbs').attr('section');
	} else{
	    dataString = 'class=' + $('#gradeBookBreadCrumbs').attr('class');
	}
    }
    
    $.ajax({
	url: '/gradebook/gradingScale/view',
	data: dataString,
	success: function(data){
	    $('#gradingScaleSelect').remove();
	    $('<div/>').attr({
		id: 'gradingScaleSelect'	
	    }).css('position','absolute').html(data).appendTo('#gutter');
	    
	    updateCategoryUppers();
	    updateCategoryLowers();
	    $('#closeGradingScaleSelect').unbind('click').bind('click', function(){closeGradingScaleSelect(true)});
	    
	    $('.category').each(function(){
		$(this).append(
		    $('<span/>').attr({
			class: "categorySelectAddRow"
		    }).html('<img src="/resources/images/gradeBook/plug.png"/>&nbsp;')
		).append(
		    $('<span/>').attr({
			class: "categorySelectDeleteRow",
		    }).html('&nbsp;')	   
		);
	    }).not(':last').not(':first').each(function(){
		
		$(this).find('.categorySelectDeleteRow').html('x');
	    });
	    
	}
    });
    
}

function submitWeights() {
    
    dataString = 'class=' + $('#gradeBookBreadCrumbs').attr('class');
    
    dataString += '&weights=' ;
    
    $('.weightCategory').not(':last').each(function(){
	if ($(this).children().eq(0).val() != '' && $(this).children().eq(1).val() != '' ){
	    dataString = dataString + $(this).children().eq(0).val() + '//' + $(this).children().eq(1).val() + '||' ;
	}
	
    });
    
    $.ajax({
	url: '/gradebook/weights/set/',
	type: 'POST',
	data: dataString,
	success: function(data) {
	    closeWeights();
	    updateGradeBook();
	    $('#weightLabel').css('display','block');
	    updateWeights();
	}
    });
}

function updateWeights() {
    $('th').not(':first').not(':nth-child(2)').each(function(){
	var id = $(this).attr('value');
	var self = $(this)
	if (id){
	    $.ajax({
		url: '/gradebook/weights/eventWeight?id=' + id,
		success: function(data){
		    if (data != '' && $('#weightLabel').is(':visible')){
			$(self).children('.eventWeight').html(data + '%').css('display','block');
		    }
		    
		}
	    });	
	}
	
    });
}

function newWeightCategory(){
    var target = $('.weightCategory').eq(-1);
    if ($(target).children().eq(0).val() != '' && $(target).children().eq(2).val() != ''){
	var clone = $(target).clone();
	$(clone).children().eq(0).val('').siblings().eq(1).val('');
	$(target).after(clone);
    }
    
    var totalPercentage = 0;
    
    $('.weightCategory').each(function(){
	if ($(this).children().eq(0).val() != '' && $(this).children().eq(2).val() != ''){
	    totalPercentage += parseInt($(this).children().eq(2).val());
	}	
    });
    
    if (totalPercentage == 100){
	$('#weightsButtons').children().eq(1).removeClass('disabled').bind('click', function(){submitWeights();});
    } else {
	$('#weightsButtons').children().eq(1).removeClass('disabled').addClass('disabled').unbind('click');
    }
    
}

function addGradeScaleCategory(self){
    var clone = $(self).clone();
    $(self).after(clone);
    var one = Math.round(parseFloat($(clone).find('.categoryUpper').attr('value')));
    var two = Math.round(parseFloat($(clone).find('.categoryLower').attr('value')));
    
    
    if($(self).index() == 1){
	$(clone).append($('.categorySelectDeleteRow').eq(0).clone());
    }
    
    $(self).find('.categoryLower').attr('value', (two + one) / 2);

    updateCategoryUppers();
    
    $('#closeGradingScaleSelect').unbind('click').bind('click', function(){closeGradingScaleSelect(false)});

}

function deleteGradeScaleCategory(self){
    $(self).remove();
    updateCategoryLowers();
    
    $('#closeGradingScaleSelect').unbind('click').bind('click', function(){closeGradingScaleSelect(false)});

}

function closeGradingScaleSelect(applied){
    if (applied){
	$('#gradingScaleSelect').remove();
    } else{
	if (confirm("You're grading scale has un-applied changes. Exit anyway? Changes will be lost")){
	    closeGradingScaleSelect(true);
	}
	
    }
}

function updateCategoryUppers(){
    $('.category').not(':first').each(function(){
	$(this).find('.categoryUpper').val(parseFloat($(this).parent().children().eq($(this).index()-1).find('.categoryLower').val()));	
    });
    
    $('#closeGradingScaleSelect').unbind('click').bind('click', function(){closeGradingScaleSelect(false)});
}

function updateCategoryLowers(){

    $('.category').not(':last').each(function(){
	$(this).find('.categoryLower').val(parseFloat($(this).parent().children().eq($(this).index()+1).find('.categoryUpper').val()));	
    });
    
    $('#closeGradingScaleSelect').unbind('click').bind('click', function(){closeGradingScaleSelect(false)});
}

function histogram(){
    var data = '';
    var title = '';
    var max = 110;
    
    if ($('.selectedEvent').is('*')){
	var index = $('.selectedEvent').index();
	max = parseInt($('.selectedEvent').attr('possiblePoints')) + 10;
	
	$('.gradeBookStudent').each(function(){
	    $(this).children().eq(index).each(function(){
		var val = $(this).children('span').eq(0).html();
		if (val.trim() != '__'){
		    data += val + ',';
		}
	    });	
	});
	
	data = data.substring(0,data.length-1);
	title = "Frequency of Grades in " + $('.selectedEvent').find('.eventTitle').html();

    } else {
	$('.gradeBookStudent').each(function(){
	    $(this).children().eq(1).each(function(){
		var val = $(this).children().eq(1).html();
		data += val.substring(0,val.length-1) + ',';
	    });	
	});
	
	data = data.substring(0,data.length-1);
	title = "Frequency of Class Grades" ;
	
	
    }
    
    $.ajax({
	url: '/gradebook/count/?data=' + data ,
	success: function(data){
	    
	    $('#gradeBookViewBody').children().hide();
	    $('#gradingScaleSelect').hide();
	    $('#statReturn').remove();
	    $('#statTitle').remove();
	    $('#stat').remove();
	    $('<div/>').attr({
		id: 'statReturn'
	    }).html('return to grade book').appendTo('#gradeBookViewBody');
	    
	    $('<div/>').attr({
		id: 'statTitle'
	    }).html(title).appendTo('#gradeBookViewBody');
	    
	    $('<div/>').attr({
		id: 'stat',
		style: 'height:400px; width:90%; margin-left:5%;'
	    }).appendTo('#gradeBookViewBody');
	    
	    var series = new Array();
	    
	    $(data.split('_')).each(function(){
		var array = new Array()
		array.push(this.split(',')[0]);
		array.push(this.split(',')[1]);
		
		series.push(array);
	    });
	    
	    $.plot($("#stat"), [
		{ label: null,  data: series},
	    ], {
		series: {
		    bars: {
			show: true,
			barWidth: 10
		    },
		    color: '#00a8ff'
		},
		xaxis: {
		    ticks: 10,
		    min: 0,
		    max: max
		},
		yaxis: {
		    tickSize: 1,
		    tickDecimals: 0
		},
		grid: {
		    backgroundColor: { colors: ["#fff", "#f8f8f8"] }
		}
	    });
            
	}
    });
    
}

function downloadSubmission(student, event){
    $.ajax({
	url: '/downloadSubmission/?event=' + event + '&student=' + student,
	success: function(){
	    alert('hello');
	}
    });
}

function clearGradeBookSelection(){
    $('.highlighted').removeClass('highlighted');
    $('.selectedEvent').removeClass('selectedEvent');
    $('.selectedStudent').removeClass('selectedStudent');
}

function applyGradingScale(){
    $('.categoryLower').blur();
    $('categoryUpper').blur();
    var dataString = '';
    
    dataString += 'class=' + $('#gradeBookBreadCrumbs').attr('class');
    dataString += '&categories='
    
    $('.category').each(function(i){
	if (i != 0){
	    dataString += ',';
	}
	dataString += $(this).find('.categoryLower').val() + '-' + encodeURIComponent($(this).find('.categoryValue').val());
    });
    
    $.ajax({
	url: '/gradebook/gradingScale/setScale',
	type: 'POST',
	data: dataString,
	success: function(data){
	    updateGradeBook();
            closeGradingScaleSelect(true);
	}
    });
    
}

function isolateHighlightedStudent(){
    $('.gradebookStudent').each(function(){
        if (! $(this).hasClass('highlighted')) {
            $(this).hide();
        }
    });

    $('#isolate').hide();
    $('#unisolate').show();
}

function showAllStudents(){
    $('.gradebookStudent').show();
    $('#isolate').show();
    $('#unisolate').hide();
}

function manageAssistants() {
    overlay('<div id="selectAssistantsHeader">Select Assistants</div><div id="selectAssistants"></div><div id="submitAssistants" onclick="submitAssistants()">Apply</div> ');
    $('#selectAssistants').m2m({
	url: '/gradebook/allStudents/',
	objectName: 'Assistant'
    });
    preSelectAssistants();
    
}

function preSelectAssistants(){
    if ($('#gradeBookBreadCrumbs').attr('section')){
	preselect = '?sectionId=' + $('#gradeBookBreadCrumbs').attr('section');
    } else {
	preselect = '?classId=' + $('#gradeBookBreadCrumbs').attr('class');
    }
    
    $.ajax({
	type: "GET",  
	url: '/gradebook/selectedAssistants/' + preselect,  
	async:false,  
	dataType: "html",
	success: function(data) {
	    var selectedAssistants = data.split('__');
	    $(selectedAssistants).each(function(){
		var target = this;
	 	$('.m2m_listPanelContent').children().each(function (){
	 	    
		    if( $(this).attr('value') == target){
			var copy = $(this).hide().clone();
			var originalId = $(this).attr('id');
			var originalValue = $(this).attr('value');
			
			var value = $(this).attr('value');
			var newValue = $('#selectAssistants').attr('value') + ',' + value;
			
			$(copy).appendTo('.m2m_selectedPanelContent').removeClass('m2m_selectedEntry').show();
			
			$(copy).attr('value',originalValue).attr('originalId', originalId ).attr('id', '_'+originalId);
			
			$(copy).unbind('click').bind('click',function(){
			    $('.m2m_selectedEntry').removeClass('m2m_selectedEntry');
			    $(this).addClass('m2m_selectedEntry');
			});
			
			$('#selectAssistants').attr('value', newValue);
			
			
		    }
		});
	    })
		}
    });
}

function submitAssistants() {
    var ids = $('#selectAssistants').attr('value');
    var id = $('#gradeBookBreadCrumbs').attr('section');
    dataString = 'id=' + id + '&ids=' + ids;
    $.ajax({
	url: '/gradebook/setSectionAssistants/',
	data: dataString,
	success: function(data) {
	    closeOverlay();
	    viewGradeBook($('#gradeBookBreadCrumbs').attr('class'), id);
	}
    });
}

function closeWeights(){
    $("#weightsWidget").remove();
}

$(document).click(function(){
    clearGradeBookSelection();
});

function addExemption(id){
    
    $.ajax({
        url: '/registrar/users/addExemption/',
        data: {
            id: id
        },
        success: function(data){
            overlaly(data);
        }
    });

}


$('#statsTool').on("mouseover mouseout", function(event) {
    if ( event.type == "mouseover" ) {
	$(this).find('ul').css({
	    position: 'fixed',
	    top: '117px',
	    right: '97px',
	    width: $(this).width() * 3
	    
	}).show();
    } else {
	$(this).find('ul').hide();
    }
});

$('.categorySelectAddRow').on('click', function(){
    addGradeScaleCategory($(this).parent());
    
});

$('.categorySelectDeleteRow').on('click', function(){
    deleteGradeScaleCategory($(this).parent());
    
});

$(".studentName").on("mouseover mouseout", function(event) {
    if ( event.type == "mouseover" ) {
	$(this).parent().addClass('highlighted');
    } else {
	if (!$(this).parent().hasClass('selectedStudent')){
	    $(this).parent().removeClass('highlighted').removeClass('selectedStudent');	
	}
	
    }
});

$('.categoryUpper').on('keypress', function(e){
    
    if (e.which == 13) {
	e.preventDefault();
	updateCategoryLowers();
	$('.categoryUpper').blur();
	
    } 
}).on('focusout', function(){
    updateCategoryLowers();
});

$('.categoryLower').on('keypress', function(e){
    
    if (e.which == 13) {
	e.preventDefault();
	updateCategoryUppers();
	$('.categoryLower').blur();
	
    } 
}).on('focusout', function(){
    updateCategoryUppers();
});

$('.entry').on('keypress', function(e){
    if (e.which == 13) { 
	e.preventDefault();
	addGradeEntry($(this).children('span').eq(0));
	$('.gradeBookEntry').blur();
	
    } 
}).on('focusout', function(){
    alert('focused out');
    addGradeEntry($(this).children('span').eq(0));
}).on("mouseover mouseout", function(event) {
    if ( event.type == "mouseover" ) {
	$(this).children('a').toggle();
    } else {
	$(this).children('a').toggle();
    }
});


$('.eventPossiblePoints').on('keypress', function(e){
    if (!(e.which >= 48 && e.which <=  57 ) && e.which != 8 && e.which < 37 && e.which > 40){
	alert('hello');
    }
    if (e.which == 13) { 
	e.preventDefault();
	updatePossiblePoints(this, $(this).parent().attr('value'));
	if ($(this).html() == '' || $(this).html() == '<br>' || $(this).html() == ' '){
	    $(this).html('--');
	}
	$('.possiblePointsHeader').blur();
    }
}).on('focusout', function(){
    updatePossiblePoints(this, $(this).parent().attr('value'));
    if ($(this).html() == '' || $(this).html() == '<br>' || $(this).html() == ' '){
	$(this).html('--');
    }
});

$('#statReturn').on('click', function(e){
    e.stopPropagation();
    closeStat();
});

$('.eventCategory').on('keypress', function(e){
    if (e.which == 13) { 
	e.preventDefault();
    }
}).on('focusout', function(){
    changeCategory(this, $(this).parent().attr('value'));
});
