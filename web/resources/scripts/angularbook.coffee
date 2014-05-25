gradebook = angular.module 'gradebook', []

# class select controller
gradebook.controller 'ClassSelect', ($scope) ->
  $scope.message = "hello"
  
  # load the class list from the server
  data = $http.get "/academia/api/classes"
