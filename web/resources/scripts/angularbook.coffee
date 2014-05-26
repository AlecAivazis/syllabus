gradebook = angular.module 'gradebook-app', []

# class select controller
gradebook.controller 'ClassSelect', ($scope, $http) ->

  $scope.classes = []

  # load the classes
  $http.get('/api/classes/taughtByMe/').success (result)->
    # loop over the result
    angular.forEach result, (item) ->
      console.log item
      # add them to the list
      $scope.classes.push item
