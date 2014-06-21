# the calendar directive
# author: alec aivazis

# add shortcut to underscore
_ = window._

# the calendar module
calendar = angular.module 'calendar', ['ui.directives', 'ngModal', 'ngQuickDate']

# add the directive
.directive 'calendar', () ->
  restrict: 'AE',
  templateUrl: '../templates/calendar/calendar.html',
  controller: 'calendarCtrl'

# the calendar controller
.controller 'calendarCtrl', ['$scope', '$http', ($scope, $http) ->

  # fullCalendar stores the events as a list of lists
  $scope.events = []
  
  # load my calendar
  $http.get('/api/users/me/calendar/').success (result) ->
    # save the events from classes that i teach
    $scope.assigned = []
    # for each event that i assigned
    angular.forEach result.assigned, (event) ->
      # add it to the list of events
      item = 
        title: event.title,
        id: event.id,
        start: moment(event.date + ' ' + event.time).toDate(),
        description: event.description,
        type: event.type
        possiblePoints: event.possiblePoints
        class: event.classes[0]
        
      # add it to the list of assigned events
      $scope.assigned.push(item)

    # add the assigned events to the list of events shown by the calendar
    $scope.events.push($scope.assigned)

  # configuration for the user interface
  $scope.uiConfig =
    calendar:        
      editable: true,
      header:
        left: 'title',
        center: '',
        right: 'today prev,next'
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
          possiblePoints: event.possiblePoints
          start: event.start
          description: event.description
        # apply the selection
        $scope.$apply()
        
      # when an event gets rendered 
      eventRender: (event, element) ->
        # load the template
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

    # prepare the data for the server
    data =
      title: $scope.selectedEvent.title
      category: $scope.selectedEvent.type
      date: moment($scope.selectedEvent.start).format('YYYY-M-D')
      time: moment($scope.selectedEvent.start).format('HH:mm:ss')
      description: $scope.selectedEvent.description
      possiblePoints: $scope.selectedEvent.possiblePoints

    # check if the selectedEvent is a copy of an event to be updated
    if $scope.selectedEvent.id
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
        event.start = $scope.selectedEvent.start
        event.description = $scope.selectedEvent.description
        event.possiblePoints = $scope.selectedEvent.possiblePoints
        # refresh the calendar ui
        $('#syll_calendar').fullCalendar('rerenderEvents')

        # notify the user
        $scope.alert = 
          type: 'notification',
          message: 'successfully moved event ' + event.id  + ' to ' + event.start

        # deselect the event
        $scope.selectedEvent = null

      # if it fails
      .error (result) ->
        console.log result
        # notify the user
        $scope.alert =
          type: 'warning'
          message: 'There was a problem while trying to update ' + $scope.selectedEvent.title

    # if no event was selected before
    else
      console.log 'making a new event'

    # this is to prevent angular from thinking we're accessing a DOM node
    return

  # deselect the selectedEvent
  $scope.deselectEvent = () ->
    $scope.selectedEvent = null

]
