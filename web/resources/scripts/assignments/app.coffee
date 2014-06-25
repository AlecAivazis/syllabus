app = angular.module 'assignments', []

app.controller 'DateSelect', [ '$scope', ($scope) ->
  console.log 'launching date select'

  # store the current date
  now = moment()

  $scope.dates = 
    today: 
      end: now
    tomorrow:
      end: now.add(1, 'day')

  console.log $scope.dates
]
