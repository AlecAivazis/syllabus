(function( $ ){

  $.fn.m2m = function( options ) { 
   
    // set default values for variables
    var settings = {
        'url'     : '',
        'preSelectedUrl'     : '',
        'entrySeparator' : '__',
        'attrSeparator' : ',',
        'submitValueSeparator' : ',',
        'objectName':'objectName'
    };

      return this.each(function() {    
	       // If options exist, lets merge them
	      // with our default settings
	      $(this).attr('value',"").attr('entrySeparator',settings['entrySeparator']).attr('attrSeparator',settings['attrSeparator']).attr('submitValueSeparator',settings['submitValueSeparator']).addClass('');
	      
	      
	      var initialContent = $(this).html();
	      if (options){
	        $.extend( settings, options );
	      }
		    
		  // create mainGutter and give it the right class.
          var mainGutter = $('<div/>').attr({
		  }).addClass('m2m_mainGutter').appendTo(this);
			
		  $(this).empty().append(mainGutter);
	
		  		     
	      // create body container
	      var contentGutter = $('<div/>').attr({
		  }).addClass('m2m_contentGutter').appendTo(mainGutter); 
		  
		  // create listPanelGutter	
		  var listPanelGutter = $('<div/>').attr({
		  }).addClass('m2m_listPanelGutter').appendTo(contentGutter);
		  
		  // create listPanelHeader
		  var listPanelHeader = $('<div/>').attr({
		  }).addClass('m2m_listPanelHeader').html('Available ' + settings['objectName'] + 's').appendTo(listPanelGutter);
		  
		  // create listPanelSearchFieldGutter
		  var listPanelSearchFieldGutter = $('<div/>').attr({
		  }).addClass('m2m_listPanelSearchFieldGutter').appendTo(listPanelGutter);
		  
		  // create icon for listPanelSearchField
		  var listPanelSearchFieldIcon = $('<img/>').attr({
		  	src: '/resources/images/searchicon.png'
		  }).addClass('m2m_listPanelSearchFieldIcon').html('hello').appendTo(listPanelSearchFieldGutter);
		  
		  //create listPanelSearchField
		  var searchField = $('<input type="text"/>').attr({
		  }).addClass('m2m_listPanelSearchField').appendTo(listPanelSearchFieldGutter).keyup(function(event){
		  	m2m_filter('m2m_listPanel');
		  	return;
		  });
		  
		  // create listPanelContent
		  var listPanel = $('<div/>').attr({
		  }).addClass('m2m_listPanelContent').appendTo(listPanelGutter);
			
		  // create controlPanel
		  var controlPanel = $('<div/>').attr({
		  }).addClass('m2m_controlPanel').appendTo(contentGutter);
		  
		  //create selectedPanelGutter
		  var selectedPanelGutter = $('<div/>').attr({	  
		  }).addClass('m2m_selectedPanelGutter').appendTo(contentGutter); 
		  
		  // create selectedPanelHeader	
		  var selectedPanelHeader = $('<div/>').attr({	  
		  }).addClass('m2m_selectedPanelHeader').html('Chosen ' + settings['objectName']+ 's').appendTo(selectedPanelGutter); 
		  
		  // create selectedPanelSearchFieldGutter
		  var selectedPanelSearchFieldGutter = $('<div/>').attr({
		  }).addClass('m2m_selectedPanelSearchFieldGutter').appendTo(selectedPanelGutter);
		  
		  // create icon for selectedPanelSearchField
		  var selectedPanelSearchFieldIcon = $('<img/>').attr({
		  	src: '/resources/images/searchicon.png'
		  }).addClass('m2m_selectedPanelSearchFieldIcon').html('hello').appendTo(selectedPanelSearchFieldGutter);
		  
		  //create selectedPanelSearchField
		  var searchField = $('<input type="text"/>').attr({
		  }).addClass('m2m_selectedPanelSearchField').appendTo(selectedPanelSearchFieldGutter).keyup(function(event){
		  	m2m_filter('m2m_selectedPanel');
		  	return;
		  });
		  	
		  // create selectedPanelContent
		  var selectedPanelContent = $('<div/>').attr({	  
		  }).addClass('m2m_selectedPanelContent').appendTo(selectedPanelGutter); 

		  //create selectedPanelFooter
		  var selectedPanelFooter = $('<div/>').attr({	  
		  }).addClass('m2m_selectedPanelFooter').html('Highlight your choice(s) and click <img width="15px" src="/resources/images/rightArrow.png"/> to select a ' + settings['objectName'].toLowerCase()).appendTo(mainGutter); 

		  // create a control gutter to vertically align the controls
		  var controlContent = $('<div/>').attr({  
		  }).addClass('m2m_controlContent').appendTo(controlPanel); 
		  
		  // create the right control arrow
		  var rightArrow = $('<img/>').attr({
		    src: '/resources/images/rightArrow.png',
		    onclick: 'm2m_selectEntry("' + $(this).attr('id') + '"' + ',"' + $(this).attr('submitValueSeparator') +'")'
		  }).bind('click', function() {
                m2m_selectEntry("" + $(this).parent().parent().parent().parent().parent().attr('id'), "" + $(this).parent().parent().parent().parent().parent().attr('submitValueSeparator'));
            }).addClass('m2m_controlArrow').appendTo(controlContent); 
		  
		  // create the left control arrow
		  var leftArrow = $('<img/>').attr({
		    src: '/resources/images/leftArrow.png'
		  }).bind('click', function(){
                m2m_deselectEntry("" + $(this).parent().parent().parent().parent().parent().attr('id'), "" + $(this).parent().parent().parent().parent().parent().attr('submitValueSeparator'));
            }).addClass('m2m_controlArrow').appendTo(controlContent); 
		  
		  //populate listPanel with the elements described at url
		  m2m_populate(settings['url'], settings['entrySeparator'], settings['attrSeparator']);
		  
    	});
    };
})( jQuery );

function m2m_populate(url, entrySeparator, attrSeparator){
	$.ajax({  
		type: "GET",  
		url: url,  
		async:false,  
		dataType: "html",
		success: function(data) {

			var eventArray = data.split(entrySeparator);
	 		$(eventArray).each(function (i) {
		      var attributes = this.split(attrSeparator);
		      var content = attributes[0];
		      var value = attributes[1];
		      
		      $('<div/>').attr({
		      	id: 'm2m_'+i,
		      	value: value
		      	}).bind('click', function(){
                    m2m_highlightEntry("" + i );
                }).addClass('m2m_listPanelEntry').html(content).appendTo($('.m2m_listPanelContent')); 
		      
		    });
		  		
		  }  
		});
	
}

function m2m_deselectEntry(parent, submitValueSeparator){
	var selectedEntry = $('.m2m_selectedEntry');
    var parentElement = $('#' + parent);
    var value = $('.m2m_selectedEntry').attr('value');
	var newValue = $(parentElement).attr('value') + ',' + value;
    var array = $(parentElement).attr('value').split(',');
	if(jQuery.inArray(value, array) != -1){
		var position = jQuery.inArray(value, array);
		var id = $(selectedEntry).attr('id');
		array.splice(position, 1);
		selectedEntry.remove().removeClass('m2m_selectedEntry');
		$('#' + $(selectedEntry).attr('originalId')).show();
		$('#' + parent).attr('value', array.join(','));
		$('#registrarM2MStatus').removeClass('registrarM2MSubmitted').addClass('registrarM2MNotSubmitted').html('not submitted');
	} 
}

function m2m_filter(which){
	var text = $('.' + which + 'SearchField').val();
	if (text !=""){
	  $('.'+ which + 'Content').children().each(function(){
	    if ($(this).html().indexOf(text) == -1){
	      $(this).hide();
	    }
	  });
	} else{
	  $('.'+ which + 'Content').children().each(function(){
	  	$(this).show();
	  });
	}
}

function m2m_submit(parent){
	alert($('#registrarm2m').attr('value'));
}




function m2m_selectEntry(parent, submitValueSeparator){

	var selectedEntry = $('.m2m_selectedEntry');
    var parentElement = $('#' + parent);
    var value = $('.m2m_selectedEntry').attr('value');
	var newValue = $(parentElement).attr('value') + ',' + value;
	var array = $(parentElement).attr('value').split(',');
	
	
	if(!(jQuery.inArray(value, array) > 0)){
		var copy = $(selectedEntry).hide().clone();
		var originalId = $(selectedEntry).attr('id');
		var originalValue = $(selectedEntry).attr('value');
		
		$(copy).appendTo('.m2m_selectedPanelContent').removeClass('m2m_selectedEntry').show();
		copy.attr('value',originalValue).attr('originalId', originalId ).attr('id', '_'+originalId);
		copy.unbind('click').bind('click',function(){
			$('.m2m_selectedEntry').removeClass('m2m_selectedEntry');
			$(this).addClass('m2m_selectedEntry');
		});
		
		$('#' + parent).attr('value', newValue);
		$('#registrarM2MStatus').removeClass('registrarM2MSubmitted').addClass('registrarM2MNotSubmitted').html('not submitted');
	}
}


function m2m_highlightEntry(id){
	$('.m2m_selectedEntry').removeClass('m2m_selectedEntry');
	$('#m2m_' + id).addClass('m2m_selectedEntry');
}