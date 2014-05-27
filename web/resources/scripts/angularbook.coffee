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
        $scope.gradingScale = result

      # prevent the gradingScale from refreshing
      refreshGradingScale = false

    $scope.showGradingScale = !$scope.showGradingScale

  # show the grading scale window
  $scope.showGradingScale = () ->

    #start    
    dataString = ''

    if $('#gradeBookBreadCrumbs').attr('class')
        $http(
          url: '/gradebook/gradingScale/view/',
          method: 'GET',
          params: {
            'section' : $('#gradeBookBreadCrumbs').attr('section'),
            'class' : $('#gradeBookBreadCrumbs').attr('class')
          }
        ).success (result) ->
          $('#gradingScaleSelect').remove();
          $('<div/>').attr({
            id: 'gradingScaleSelect'	
	  }).css('position','absolute').html(result).appendTo('#gutter');
	    
	  updateCategoryUppers();
	  updateCategoryLowers();

updateCategoryUppers = () ->
  $('.category').not(':first').each () ->
    $(this).find('.categoryUpper').val(parseFloat($(this).parent().children().eq($(this).index()-1).find('.categoryLower').val()))
  
  $('#closeGradingScaleSelect').unbind('click').bind 'click', () ->
    closeGradingScaleSelect(false)

updateCategoryLowers = () ->
  $('.category').not(':last').each () ->
    $(this).find('.categoryLower').val(parseFloat($(this).parent().children().eq($(this).index()+1).find('.categoryUpper').val()))

  $('#closeGradingScaleSelect').unbind('click').bind 'click', () ->
    closeGradingScaleSelect(false)
