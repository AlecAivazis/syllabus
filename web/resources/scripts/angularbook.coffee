gradebook = angular.module 'gradebook-app', []

# class select controller
gradebook.controller 'ClassSelect', ['$scope', '$http', '$rootScope($scope, $http, $rootScope) ->

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

# controller for the actual gradebook
gradebook.controller 'gradebook-view', ['$scope', '$rootScope', ($scope, $rootScope) ->

  # detect changes in rootScope's gradebook_id to switch to the appropriate book
  $rootScope.$watch('gradebook_id', () ->
   
    

    $scope.gradebook_id = $rootScope.gradebook_id
  )
]
