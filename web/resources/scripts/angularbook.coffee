gradebook = angular.module 'gradebook-app', []

# class select controller
gradebook.controller 'ClassSelect', ($scope, $http, $rootScope) ->

  # store a list of the classes the user teaches
  $scope.classes = []

  # load the classes
  $http.get('/api/classes/taughtByMe/').success (result)->
    # loop over the result
    angular.forEach result, (item) ->
      # add them to the list
      $scope.classes.push item

  # event handler for class select
  $scope.loadGradeBook = (id) ->
    # change the id of the current gradebook
    $rootScope.gradebook_id = id

gradebook.controller 'gradebook-view', ($scope, $rootScope, $http) ->

  $rootScope.$watch 'gradebook_id', () ->
    # check that its not null
    if not $rootScope.gradebook_id
      return

    # load the homework events 
    $http.get('/api/events/homeworkByClass/' + $rootScope.gradebook_id).success (result)->
      $scope.events = []
      angular.forEach result, (item) ->
        $scope.events.push item

    # load the students in this class
    $http.get('/api/users/studentsbyClass/' + $rootScope.gradebook_id).success (result)->
      #keep a list of the students in this class
      $scope.students = []
      # loop over the response and add them to the list
      angular.forEach result (item) ->
        $scope.students.push item
