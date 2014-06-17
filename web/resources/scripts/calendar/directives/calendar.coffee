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
.controller 'calendarCtrl', ['$scope', ($scope) ->

  date = new Date()
  d = date.getDate()
  m = date.getMonth()
  y = date.getFullYear()

  $scope.events = []
  $scope.events.push [{title: 'All Day Event',start: new Date(y, m, 1)},
    {title: 'Long Event',start: new Date(y, m, d - 5),end: new Date(y, m, d - 2)},
    {id: 999,title: 'Repeating Event',start: new Date(y, m, d - 3, 16, 0),allDay: false},
    {id: 999,title: 'Repeating Event',start: new Date(y, m, d + 4, 16, 0),allDay: false},
    {title: 'Birthday Party',start: new Date(y, m, d + 1, 19, 0),end: new Date(y, m, d + 1, 22, 30),allDay: false}
  ]

  # configuration for the user interface
  $scope.uiConfig =
    calendar:
      editable: true,
      header:
        left: 'title',
        center: '',
        right: 'today prev,next'

]


