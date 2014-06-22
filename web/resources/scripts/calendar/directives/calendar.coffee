# the calendar directive
# author: alec aivazis

# add shortcut to underscore
_ = window._

# the calendar module
calendar = angular.module 'calendar', ['ui.directives', 'ngModal', 'ngQuickDate']

# add the directive
.directive 'calendar', () ->
  restrict: 'AE'
  templateUrl: '../templates/calendar/calendar.html'
  controller: 'calendarCtrl'
  link: (scope, element, attr) ->
    $('.fc-header-right').append 'hello world'

# the calendar controller
.controller 'calendarCtrl', ['$scope', '$http', ($scope, $http) ->

  # collect the events that were created this session
  $scope.created = []
  # save the events from classes that i teach
  $scope.assigned = []

  $scope.events = [$scope.created, $scope.assigned]
  
  # load my calendar
  $http.get('/api/users/me/calendar/').success (result) ->
    # save the list of classes that i teach
    $scope.classes = result.classes
    # for each event that i assigned
    angular.forEach result.assigned, (event) ->
      # build datetime objects
      eventStart = moment(event.date + ' ' + event.time).toDate()
      eventEnd = false
      # add it to the list of events
      item = 
        title: event.title
        id: event.id
        start: eventStart
        end: if eventEnd then eventEnd else eventStart
        description: event.description
        type: event.type
        category: event.category
        possiblePoints: event.possiblePoints
        classes: event.classes[0]

      # add it to the list of assigned events
      $scope.assigned.push(item)

    # add the assigned events to the list of events shown by the calendar
    $scope.events.push($scope.assigned)

  # configuration for the user interface
  $scope.uiConfig =
    calendar:        
      height: 700
      header:
        left: 'month agendaWeek agendaDay'
        center: 'prev title next'
        right: 'newEvent today'
      weekMode: 'liquid'

      editable: true
      selectable: true
      unselectAuto: false

      # when an event is dropped on another date
      eventDrop: (event, dayDelta, minuteDelta) ->
        # change the starting date of the event
        $scope.changeEventDate(event, moment(event.start).add('days', dayDelta)
                                                         .add('minutes', minuteDelta))
      # when an event is clicked 
      eventClick: (event, jsEvent, view) ->
        # load its data into the selected event
        $scope.selectedEvent = 
          id: event.id
          title: event.title
          type: event.type
          category: event.category
          possiblePoints: event.possiblePoints
          start: event.start
          end: event.end
          description: event.description
          classes: event.classes
        # apply the selection
        $scope.$apply()


      # when an event gets rendered 
      eventRender: (event, element) ->
        # load the tooltip template
        source = $('#tooltip-template').html()
        template = Handlebars.compile source
        # define the context for the template
        context =
          title: event.title
          id: event.id
          description: event.description 
          start: moment(event.start).format('ha')
          end: if event.end then moment(event.end).format('ha') else ''
          # i hate this.
          isAssignment: event.type == 'assignment'
          isTest: event.type == 'test'

        # add a tooltip with the rendered template
        element.qtip
          content:
            text: template(context)
          , position: 
            # centered above the element
            my: 'bottom center',
            at: 'top center',
            # force the tooltip to be within the calendar
            viewport: $('#calendar')
          # add a custom class
          , style:
            classes: 'tooltip'

      # when a date/range is selected
      select: (start, end) ->
        # set the local variables
        $scope.selectedDayStart = moment(start)
        $scope.selectedDayEnd = moment(end)
        # show the newEvent button
        $('.fc-button-newEvent').show()
      # when a date/range is unselected
      unselect: () ->
        # hide the newEvent button
        $('.fc-button-newEvent').hide()
        # clear the local variables
        $scope.selectedDayStart = null
        $scope.selectedDayEnd = null
        
      # when the new event button is clicked
      newEvent: () ->
        # select an empty event over the appropriate days
        $scope.selectedEvent =
          start: $scope.selectedDayStart.toDate()
          end: $scope.selectedDayEnd.toDate()
        # apply the change
        $scope.$apply()

  # change the start date of an event
  $scope.changeEventDate = (event, old) ->
    # tell the database
    $http.post '/calendar/moveEvent/',
      id: event.id,
      date: moment(event.start).format('YYYY-M-D')
    # if it fails
    .error ->
      # warn the user
      $scope.alert =
        type: 'warning',
        message: 'could not move event ' + event.id + ' to ' + event.start
      # revert the date
      event.start = new Date(old)
    # if it succeeds
    .success ->
      # notify the user
      $scope.alert =
        type: 'notification',
        message: 'successfully moved event ' + event.id  + ' to ' + event.start

  # apply changes
  $scope.applyChanges = () ->
    # if there was a category given
    if $scope.selectedEvent.category
      # use it
      category = $scope.selectedEvent.category
    # otherwise
    else
      # use the type
      category = $scope.selectedEvent.type
    
    # prepare the data for the server
    data =
      title: $scope.selectedEvent.title
      category: category
      type: $scope.selectedEvent.type
      date: moment($scope.selectedEvent.start).format('YYYY-M-D')
      time: moment($scope.selectedEvent.start).format('HH:mm:ss')
      description: $scope.selectedEvent.description
      possiblePoints: $scope.selectedEvent.possiblePoints
      classes: [$scope.selectedEvent.classes]

    console.log data

    # check if the selectedEvent is a copy of an event to be updated
    if $scope.selectedEvent.id
      console.log 'you are editing an event' + $scope.selectedEvent.id
      # update the database
      $http method:'patch', url: '/api/events/' + $scope.selectedEvent.id + '/', data: data
      # if it succeeds
      .success (result) ->
        # update the event
        # grab the event corresponding to the selected one
        event = _.findWhere _.flatten($scope.events), id: $scope.selectedEvent.id
        # set the event attributes
        event.title = $scope.selectedEvent.title
        event.type = $scope.selectedEvent.type
        event.category = $scope.selectedEvent.category
        event.start = $scope.selectedEvent.start
        event.end = $scope.selectedEvent.end
        event.description = $scope.selectedEvent.description
        event.possiblePoints = $scope.selectedEvent.possiblePoints
        event.classes = $scope.selectedEvent.classes
        # refresh the calendar ui
        $('#syll_calendar').fullCalendar 'rerenderEvents'

        # notify the user
        $scope.alert = 
          type: 'notification',
          message: 'successfully moved event ' + event.id  + ' to ' + event.start

        # deselect the event
        $scope.selectedEvent = null

      # if it fails
      .error (result) ->
        console.log 'ERROR: '
        console.log result
        # notify the user
        $scope.alert =
          type: 'warning'
          message: 'There was a problem while trying to update ' + $scope.selectedEvent.title

    # if no event was selected before
    else
      # create the event on the database
      $http method:'post', url: '/api/events/create/', data: data
      # if it succeeds
      .success (result) ->
        console.log 'created a new event'
        console.log data
        # copy the selected event to the list with the appropriate id
        $scope.created.push $.extend({id:result}, $scope.selectedEvent)
        # deselect the event
        $scope.deselectEvent()
        
      # if there was an error
      .error (result) ->
        console.log result

  # deselect the selectedEvent
  $scope.deselectEvent = () ->
    $scope.selectedEvent = null

  $scope.isSelectedDayRange = () ->
    # if theres no event selected
    if not $scope.selectedEvent
      return false
    # if the selected event has no end
    if not $scope.selectedEvent.end
      return false
    # a range is defined as when the start and end are not the same
    return not moment($scope.selectedEvent.start).isSame($scope.selectedEvent.end)

]
