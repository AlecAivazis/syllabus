# the calendar directive
# author: alec aivazis

# add shortcut to underscore
_ = window._

# the calendar module
angular.module 'calendar', ['ui.calendar']

# add the directive
.directive 'calendar', () ->
  restrict: 'AE',
  templateUrl: '../templates/calendar/calendar.html',
  controller: 'calendarCtrl'

# the calendar controller
.controller 'calendarCtrl', ['$scope', '$http', ($scope, $http, angularMoment) ->

  date = new Date()
  d = date.getDate()
  m = date.getMonth()
  y = date.getFullYear()

  # fullCalendar stores the events as a list of lists
  $scope.events = []
  
  # load each class taught by me
  $http.get('/api/user/me/calendar/').success (result) ->
    $scope.assigned = []
    # for each event that i assigned
    angular.forEach result.assigned, (event) ->
      # add it to the list of events
      item = 
        title: event.title,
        id: event.id,
        start: moment(event.date + ' ' + event.time).toDate()
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
      # when an event is dropped, change the date
      eventDrop: (event, dayDelta, minuteDelta) ->
        # save the old date so we can revert back if it fails
        old = moment(event.start).add('days', -dayDelta)
        # change the date
        $scope.changeEventDate event, old

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

]


