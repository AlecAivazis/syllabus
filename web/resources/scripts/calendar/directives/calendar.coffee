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

    # save the classes that i teach
    $scope.myClasses = result.classes

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
        # select it
        $scope.selectedEvent = event
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
    console.log $scope.selectedEvent.start

]
