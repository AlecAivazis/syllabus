(function( $ ){

  $.fn.tooltip = function( options ) { 
   
    var settings = {

    };

      return this.each(function() {    

	      var initialContent = $(this).html();
	      if (options){
	        $.extend( settings, options );
	      }
		    
		  $(this).live('hover',function(){
            
                alert('hello');
              
            });

    	});
    };
})( jQuery );
