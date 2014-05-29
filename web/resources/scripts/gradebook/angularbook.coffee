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

  class_id = 

  $rootScope.$watch 'gradebook_id', () ->
    # check that its not null
    if not $rootScope.gradebook_id
      return

    # load the homework events 
    $http.get('/api/classes/' + $rootScope.gradebook_id + '/gradebook/').success (result)-> 
      $scope.breadcrumb = result.breadcrumb
      $scope.events = result.events
      $scope.gradebook = result.gradebook
      $scope.students = result.students

    class_id = $rootScope.gradebook_id

  # track if the grading scale needs to be refreshed
  refreshGradingScale = true

  # hide/show the grading scale
  $scope.toggleGradingScale = () ->
    # if the grading scale needs to be refreshed
    if refreshGradingScale
      # load the grading scale from the syllabus api
      $http.get('/api/classes/' + class_id + '/gradingScale/').success (result) ->
        console.log result
        # load the scale into the view
        $scope.gradingScale = result

        $scope.updateUppers()

      # prevent the gradingScale from refreshing
      refreshGradingScale = false

    $scope.showGradingScale = !$scope.showGradingScale

# grading scale window directive
gradebook.directive 'gsc', () ->
  restrict : 'AE',
  templateUrl: '../templates/gradebook/gradingScale.html',
  link: (scope, elem, attrs) ->

    # when an upper is changed, go make the lowers reflect it
    scope.updateUppers = () ->
      console.log "Updating uppers"
      # go over each category
      angular.forEach scope.gradingScale.categories, (category, key) ->
        # check if it made it past the first category
        cont = true
        # if its the first one
        if key == 0
          # set the upper to the maximum: 100 %
          category.upper = 100
          console.log "updated the first one"
          # move on to the next one
          cont= false
        if cont
          prev = scope.gradingScale.categories[key-1]    
          category.upper = prev.lower

    # when an upper is changed, go make the lowers reflect it
    scope.updateLowers = () ->
      console.log "Updating lower"
      # go over each category
      angular.forEach scope.gradingScale.categories, (category, key) ->
        # check if it made it past the first category
        cont = true
        # if its the last one
        if key == scope.gradingScale.categories.length - 1
          # set the lower to the minimum: 0 %
          category.lower = 0
          console.log "updated the last one"
          # move on to the next one
          cont= false

        if cont
          prev = scope.gradingScale.categories[key+1]    
          category.lower = prev.upper
