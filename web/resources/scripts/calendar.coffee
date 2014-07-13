# These scripts handle the user interface for the calendar and displays the current users
# events (homework, lectures, meetings, etc.)


# when a day is selected add the appropriate class
selectDay = (date) ->
  $('.selectedDay').removeClass 'selectedDay'
  $('#' + date).addClass 'selectedDay'


# when the event drag begins save the id and type to the DOM event
eventDrag = (target, event) ->
  # extract the type and pk from the element id
  info = target.id.split ':'
  # save the data to the DOM event
  event.dataTransfer.setData 'id', info[1]
  event.dataTransfer.setData 'type', info[0]


# when an events is dropped on a particular date
eventDropMoveEvent = (target, event) ->
  # grab the target date
  date = $(target).attr 'id'
  # save the event type
  type = event.dataTransfer.getData 'type'
  # save the id of the event
  id = event.dataTransfer.getData 'id'

  # make the ajax request
  $.ajax
    url: '/calendar/moveEvent/'
    type: 'POST'
    data:
      date: date
      id: id
      type: type
    # if it succeeds
    success: (data) ->
      # grab the appropriate spot in the target container
      switch type
        when 'event' then targetElement = $(target).find('.calendarDayBody')
        when 'group' then targetElement = $(target).find('.calendarDayLabel')
        when 'term' then targetElement = $(target).find('.calendarDayLabel')

      # add the event to the target element
      $('#' + type + '\\:' + id).remove().appendTo(targetElement)


# remove the event from the database and then the UI
deleteEvent = (id) ->
  if confirm 'Are you sure you want to delete this event?'
    $.ajax
      url: '/calendar/deleteEvent/'
      type: 'POST'
      data:
        id: id
      success: (data) ->
        which = $('#calendar').attr 'which'
        number = $('#calendar').attr 'number'
        year = $('#calendar').attr 'year'

        loadCalendar which, year, number

        $('#' + id).remove()


# pull up the edit event form
editEvent = (id) ->
  $.ajax
    url: '/calendar/editEventForm/'
    data:
      id: id
    success: (data) ->
      overlay data


# validate the event form
validateEventForm = (id) ->
  submitEventForm id


# submit the event form
submitEventForm = (id) ->
  # send the request to the server
  $.ajax
    url: '/calendar/editEvent/'
  	type: 'POST'
  	data:
      id: id
      title: $('#editEventTitle').val()
      date: $('#editEventDate').val()
      time: $('#editEventTime').val()
      possiblePoints: $('#possiblePoints').val()
      associatedReading: $('#associatedReading').val()
      description: $('#editEventDescription').val()
    success: (data) ->
      refreshCalendar()
      closeOverlay()


# switch views 
loadView = (which) ->
  loadCalendar which, $('calendar').attr 'year', $('#calendar').attr 'number'


# load a specific calendar from the
loadCalendar = (which, year, number) ->
  $.ajax
    url: '/calendar/ajax/'
    data:
      which: which
      year: year
      number: number
    success: (data) ->
      # load the new calendar
      $('#calendar').replaceWith data
      # create the tooltips
      $('.tooltip').tooltipster
        interactive: true
        theme: 'eventTooltip'

  
# reload the calendar with the current values (ie refresh)
refreshCalendar = () ->
  # grab the current date values off of the calendar
  which = $('#calendar').attr 'which'
  number = $('#calendar').attr 'number'
  year = $('#calendar').attr 'year'
  # reload the calendar
  loadCalendar which, year, number


# load the previous calendar for either view
loadPrevCalendar = () ->
  # grab the current date values off of the calendar
  which = $('#calendar').attr 'which'
  number = $('#calendar').attr 'number'
  year = $('#calendar').attr 'year'

  # the meaning of prev depends on the type of calendar
  switch which
    when 'month'
      # if the current month is january
      if parseInt(number) == 1
        # load the december calendar of the previous year
        loadCalendar which, parseInt(year) - 1, 12
      # current month is not january (safe to subtract one)
      else
        # load the previous calendar
        loadCalendar which, year, parseInt(number) - 1
    when 'week'
      # if we're at the first week of the year
      if number <= 1
        # load the last week of the previous year
        loadCalendar which, parseInt(year) - 1, 52 
      # we're not at the beginning of the year
      else
        # load the previous calendar
        loadCalendar which, year, parseInt(number) - 1
  
# load the next calendar
loadNextCalendar = () ->
  # grab the current date values off of the calendar
  which = $('#calendar').attr 'which'
  number = $('#calendar').attr 'number'
  year = $('#calendar').attr 'year'

  # the meaning of prev depends on the type of calendar
  switch which
    when 'month'
      # if the current month is december
      if parseInt(number) == 12
        # load the january calendar of the next year
        loadCalendar which, parseInt(year) + 1, 1
      # current month is not december (safe to add one)
      else
        # load the next calendar
        loadCalendar which, year, parseInt(number) + 1
    when 'week'
      # if we're at the last week of the year
      if number == 52
        # load the last week of the previous year
        loadCalendar which, parseInt(year) + 1, 1
      # we're not at the beginning of the year
      else
        # load the previous calendar
        loadCalendar which, year, parseInt(number) + 1


# load todays calendar
loadTodayCalendar = () ->
  # grab todays data from the calendar 
  which = $('#calendar').attr 'which'
  number = $('#calendar').attr 'todaynumber'
  year = $('#calendar').attr 'todayyear'
  # load the appropriate calendar
  loadCalendar which, year, number
  

# bring up the new event form
newEvent = (category) ->
  date = $('.selectedDay').attr 'id'
  # if it had a valid id
  if date?
    # make the ajax request
    $.ajax
      url: '/calendar/newEventForm/'
      data:
        date: date
        category: category
      success: (data) ->
        overlay data
  else
    alert 'please select a day'


# load the sections of a class for the new event form
loadSectionsByClassId = (id) ->
  # if the id is zero
  if id == 0
    # clear the ui element
    $('#newEventFormSectionChoice').empty()
  # if the id is non zero
  else
    # load the sections of the class into the ui element
    $.ajax
      url: '/calendar/getSectionsById/'
      data:
        id: id
      success: (data) ->
        $('#newEventFormSectionChoice').empty().prepend data
      

# load the sections of the selected class
loadSections = () ->
  loadSectionByClassId $('#classId').find(':selected').attr 'value'


# close the event form
closeEventForm = () ->
  # refresh the calendar to get changes
  refreshCalendar()
  # close the overlay
  closeOverlay()


# remove the uploaded file from the upload list in the event form
removeFileUpload = (self, id) ->
  # grab the file name
  fileName = $(self).parent().children().eq(0).html()
  # add the removed tag
  $(self).parent().empty().append $('</span>').addClass('selectedFile').html('removed ' + fileName)
  # add the id to the list of deleted files so that they can be removed on the database
  $('[name="deletedFiles"]').attr('value', $('[name="deletedFiles"]').attr('value') + id + ',')


# return the week number of the date
getWeekNumber = (date) ->
  d = new Date(date)
  day = d.getDay()
  if day == 0
    day = 7
  d.setDate(d.getDate() + (4-day))
  year = d.getFullYear()
  ZBDoCY = Math.floor((d.getTime() - new Date(year, 0, 1, -6)) / 86400000)
  return 1 + Math.floor(ZBDoCY / 7)


# select a particular view focused on the selected day if it exists
selectView = (which) ->
  # if they asked to see the view already displayed
  if  which == $('#calendar').attr 'which'  
    # do nothing
    return

  # grab the selected date
  selectedDate = $('.selectedDay').attr 'id'
  # if it exists
  if selectedDate
    # check what view they asked for
    switch which
      when 'month'
        year = $('#calendar').attr 'year'
        number = selectedDate.split('-')[1]
        # load the appropriate calendar
        loadCalendar which, year, number
      when 'week'
        year = $('#calendar').attr 'year'
        number = getWeekNumber selectedDate
        # load the appropriate calendar
        loadCalendar which, year, number

  # they did not select a day
  else
    # check what view they asked for
    switch which
      when 'month'
        year = $('#calendar').attr 'year'
        number = $('#calendar').find('.calendarWeekDay').eq(4).attr('id').aplit('-')[1]
        # load the appropriate calendar
        loadCalendar which, year, number
      when 'week'
        year = $('#calendar').attr 'year'
        number = getWeekNumber $('#calendar').find('.calendarDay').eq(3).attr('id')
        # load the appropriate calendar
        loadCalendar which, year, number


# bring up a detailed view of the event info
viewEventInfo = () ->
  $.ajax
    # make the ajax request
    url: '/viewEvent/'
    data:
      id: id
    success: (data) ->
      # display it in an overlay
      overlay(data)


# display the start of term form
startTerm = ()->
  # grab the selected date
  date = $('.selectedDay').eq(0).attr 'id'
  # if it exist
  if date
    # grab the form off of the server
    $.ajax
      url: '/calendar/newTermStart/'
      data:
        date: date
      success: (data) ->
        overlay data
  # they didn't select a date
  else
    alert 'please select a term to begin the term on'
  
  
# display the end of term form
endTerm = () ->
  # grab the selected date
  date = $('.selectedDay').eq(0).attr 'id'
  # if it exists
  if date
    # grab the form from the server
    $.ajax
      url: '/calendar/newTermEnd/'
      data:
        date: date
      success: (data) ->
        # display the form in an overlay
        overlay(data)


# submit the end of new term form
createTermEnd = (date) ->
  $.ajax
    url: '/calendar/createTermEnd/'
    type: 'POST'
    data:
      date: date
      id: $('#term').val()
    # if it succeeded 
    success: (data) ->
      refreshCalendar()
      closeOverlay()


# submit the create term form
createTerm = (date) ->
  $.ajax
    url: '/calendar/createTerm/'
    type: 'POST',
    data:
      date: date
      name: $('#name').val()
    # if it succeeds
    success: (data) ->
      refreshCalendar()
      closeOverlay()


# bring up the begin registration group form
startRegistration = () ->
  # grab the selected day
  date =  $('.selectedDay').eq(0).attr 'id'
  # get the form from the server
  if date
    $.ajax
      url: '/calendar/startRegistration/'
      data:
        date: date
      success: (data) ->
        # show it in an overlay
        overlay(data)
   else
     alert 'please select a day to start registration on'


# bring up the end registration group form
endRegistration = () ->
  # grab the selected day
  date =  $('.selectedDay').eq(0).attr 'id'
  # get the form from the server
  if date
    $.ajax
      url: '/calendar/endRegistration/'
      data:
        date: date
      success: (data) ->
        # show it in an overlay
        overlay(data)
   else
     alert 'please select a day to end registration on'
  

# create the beginning of a registration group (submit the form)
createRegistration = (date) ->
  $.ajax
    url: '/calendar/createRegistration/'
    type: 'POST'
    data:
      date: date
      name: $('#name').val()
      term: $('#term').val()
    success: (data) ->
      refreshCalendar()
      closeOverlay()


# set the end of the registration period for a given group
setEndRegistrationDate = (date) ->
  # submit the form to the server
  $.ajax
    url: '/calendar/endRegistration/'
    type: 'POST'
    data:
      date: date
      id: $('#id').val()
      term: $('#term').val()
    # if it succeeds
    success: (data) ->
      refreshCalendar()
      closeOverlay()

# when the document loads
$(document).ready ->
  # display the current calendar
  refreshCalendar()

  # refresh the calendar every 5 minutes
  setInterval ->
    'refreshCalendar()'
  , 300000  

