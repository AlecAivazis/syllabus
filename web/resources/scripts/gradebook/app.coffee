# the gradebook angular application for the syllabus web app
# author: alec aivazis

# add shortcut to underscore
_ = window._

# create the angular module
gradebook = angular.module('gradebook-app', ['ngCookies', 'gradebook', 'gsc', 'wc',
  'utilities'])

# add csrf tokens for proper ajax support
gradebook.run ['$http', '$cookies', ($http, $cookies) -> 
  $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
  $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
]

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
    # tell the gradebook directive to reload
    $rootScope.$broadcast 'load gradebook'

# gradebook view controller
gradebook.controller 'gradebook-view', ($scope, $rootScope, $http) ->

  class_id = 
  # track wether the controls need to be refrehed
  refreshWeights = true
  refreshGradingScale = true 

  $rootScope.$on 'load gradebook', () ->
    # check that its not null
    if not $rootScope.gradebook_id
      return

    # load the homework events 
    $http.get('/api/classes/' + $rootScope.gradebook_id + '/gradebook/').success (result)-> 
      # set the scope variables
      $scope.breadcrumb = result.breadcrumb
      $scope.events = result.events
      $scope.gradebook = result.gradebook
      $scope.students = result.students
      # register the class for the gradebook
      class_id = $rootScope.gradebook_id
      # compute the averages
      $rootScope.$broadcast 'recalculateAverages'
      # make the gradebook ui element show
      $scope.hideGradebook = false

    # track if the weights need to be reloaded
    refreshWeights = true
    # track if the grading scale need to be reloaded
    refreshGradingScale = true
    # hide the various controls
    $scope.displayWeightControl = false
    $scope.showGradingScale = false

  # hide/show the weights control
  $scope.toggleWeightControl = () ->
    # if the weights need to be refreshed
    if refreshWeights
      # load the weights from the syllabus api
      $scope.loadWeights()
      # prevent the weights from loading again
      refreshWeights = false

    # flip the control variable
    $scope.displayWeightControl = !$scope.displayWeightControl

  # hide/show the grading scale
  $scope.toggleGradingScale = () ->
    # if the grading scale needs to be refreshed
    if refreshGradingScale
      # then load the scale
      $scope.loadGradingScale()
      # prevent the gradingScale from refreshing
      refreshGradingScale = false

    $scope.showGradingScale = !$scope.showGradingScale
