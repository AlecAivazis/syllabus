function makeEditor(id){
    jQuery(function($) {
        $('#syllabusContent').editor({
            enableUi: false,
            ui: {
                alignCenter: true,
                alignJustify: true,
                alignLeft: true,
                cancel: true,
                clean: true,
                embed: true,
                floatLeft: true,
                floatRight: true,
                floatNone: true,
                fontSizeDec: true,
                fontSizeInc: true,
                listUnordered: true,
                quoteBlock: true,
                redo: true,
                textBold: true,
                textItalic: true,
                textStrike: true,
                textSub: true,
                textSuper: true,
                textUnderline: true,
                undo: true,
                viewSource: true,
                save: {
                    plugin: 'saveRest'
                }
            },
            plugins: {
                dock: {
                    docked: true
                },
                saveRest: {
                    
                    ajax: {
                        type: 'POST',
                        url: function() {
                            return '/course/setSyllabus/';
                        },
                        data: function() {
                                return {
                                    id: id,
                                    syllabus: $('#syllabusContent').html()
                                };
                        }
                    }
                }
            }
            
        });
    });
}


function filterTimeline(which){
    $('.emptyTimelineNotice').remove();
    if (which == 'all'){
        $('#timeline').children().each(function(){
            $(this).show();
            $(this).children().show();
        });    
    } else {
        $('#timeline').children().each(function(){
            $(this).show();
            $(this).children().show();
        });
        
        $('#timeline').children().each(function(){
            var parent = $(this);
            $(this).children().not('.timeline_'+which).not('.timelineDateLabel').hide();
           
            if ($(this).children(':visible').length == 1){
                $(this).hide();
            }
        });
        
        if (! $('#timeline').children(':visible').length){
            $('<span/>').addClass('emptyTimelineNotice').html('There are no events of that type').appendTo('#timeline');
        }
    }
}

function viewSpace(self, which, id){
    $.ajax({
        url: '/course/view'+ which + '/',
        data: {
            id:id
        },
        success: function(data){
            $('#spaceContent').empty().html(data);
            $(self).siblings().removeClass('current');
            if (which == 'Syllabus'){
                window.location.href="/myClasses/classPage/?id=" + id ;
            }
            $(self).addClass('current');
            $('.topic').live('mouseenter',function(){
                $(this).children('.topicReplies').css('background','url("/resources/images/bubbleHighlight.png")');                
            }).live('mouseleave',function(){
                $(this).children('.topicReplies').css('background','url("/resources/images/bubble.png")');                
            });
        }
    });
}

function createTopic(id){
    
    if ($('#topicTitle').val() != ''){
        var title=$('#topicTitle').val();
    } else {
        $('#topicTitle').focus();
        return;
    }
    if ($('#topicBody').val() != ''){
        var body = $('#topicBody').val();
    } else{
        $('#topicBody').focus();
        return;
    }
    
    $.ajax({
        url: '/course/messageBoard/createTopic/',
        type: 'POST',
        data: {
            id: id,
            title: title,
            body: body
        },
        success: function(data){
            closeOverlay();
            viewMessageBoard(id);
        }
    });
}

function newTopic(id){
    $.ajax({
        url: '/course/messageboard/newTopic',
        data: {
            id:id
        },
        success: function(data){
            overlay(data);
        }
    });
}

function viewTopic(id){
    $.ajax({
        url: '/course/messageboard/viewTopic',
        data: {
            id:id
        },
        success: function(data){
            $('#spaceContent').empty().html(data);
        }
    });
}

function createReply(id){
    $.ajax({
        url: '/course/messageboard/createReply/',
        data: {
          topic: id,
          kind: 'text',
          body : $('.textQuickReplyContent').val()
        },
        type: 'POST',
        success: function(data){
            viewTopic(id);
        }
    })
}

function focusQuickReply(){
    $('.submitTextQuickReply').show();
    $('.textQuickReplyContent').empty().focus();
}

function selectQuickReplyType(self, which){
    $('.quickReplySelectorTriangle').hide();
    $(self).find('.quickReplySelectorTriangle').eq(0).show();
    
    $('.quickReplyWidget').hide();
    $('#'+which+'QuickReply').css('display','inline');
}

$('.eventTitle').live('focusout', function(){
    $.ajax({
        url: '/course/timeline/changeEventTitle/',
        type: 'POST',
        data: {
            id: $(this).parent().parent().attr('id'),
            title : $(this).html()
        }
    });
        
}).live('keypress',function(e){
    if (e.which == 13) { 
            e.preventDefault();
    } 	    
});

$('.associatedReading').live('focusout', function(){

    $.ajax({
        url: '/course/timeline/changeEventAssocReading/',
        type: 'POST',
        data: {
            id: $(this).parent().parent().attr('id'),
            associatedReading : $(this).html()
        }
    });
        
}).live('keypress',function(e){
    if (e.which == 13) { 
            e.preventDefault();  
    } 	    
});

$('.timelineEventDescription').live('focusout', function(){
    $.ajax({
        url: '/course/timeline/changeEventDescription/',
        type: 'POST',
        data: {
            id: $(this).parent().attr('id'),
            description : $(this).html()
        }
    });
        
}).live('keypress',function(e){
    if (e.which == 13) { 
            e.preventDefault();  
    } 	    
});