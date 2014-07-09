# the grading scale as an angularjs directive
# author: alec aivazis

# add a shortcut to underscore
_ = window._

# the gradebook module
angular.module('gsc', [])

# grading scale window directive
.directive 'gsc', () ->
  restrict : 'AE',
  templateUrl: '/templates/gradebook/gradingScale.html',
  controller: 'gscCtrl'
# grading scale controller
.controller 'gscCtrl', [ '$scope', '$http', '$rootScope', ($scope, $http, $rootScope) ->

  # compute the letter grade corresponding to a score
  $scope.computeGrade = (score_obj) ->
    # turn the given argument into a float
    score = parseFloat(score_obj)
    # alert the console
    console.log 'computing grade for ' + score
    # check if the grading scale exists
    if not $scope.gradingScale      
      console.log 'need to refresh gradingScale'
      $scope.loadGradingScale().success (result) ->
        console.log 'loaded scale'
        grade = _.sortBy(_.filter($scope.gradingScale.categories, (category) ->
          return category.lower < parseFloat(score)
        ), (num) ->
          return num.lower
        ).reverse()[0].value

        console.log 'computed grade as ' + grade.value
        return grade
    else
       console.log 'gradingScale is good'         
       grade = _.sortBy(_.filter($scope.gradingScale.categories, (category) ->
          return category.lower < parseFloat(score)
        ), (num) ->
          return num.lower
        ).reverse()[0]
        
       return grade


  # load the grading scale from the syllabus api
  $scope.loadGradingScale = () ->
    return $http.get('/api/classes/' + $rootScope.gradebook_id + '/gradingScale/')
                .success (result) ->
        # load the scale into the view
        $scope.gradingScale = result
        # fill in the upper bounds (defined in grading scale control directive)
        $scope.updateUppers()

  # when an lower is changed, go make the uppers reflect it
  $scope.updateUppers = () ->
    # go over each category
    angular.forEach $scope.gradingScale.categories, (category, key) ->
      # check if it made it past the first category
      cont = true
      # if its the first one
      if key == 0
        # set the upper to the maximum: 100 %
        category.upper = 100
        # move on to the next category
        cont= false

      # cont will be false for only the first category
      if cont
        # grab the previous category
        prev = $scope.gradingScale.categories[key-1]    
        # my upper is its lower
        category.upper = prev.lower

  # when an upper is changed, go make the lowers reflect it
  $scope.updateLowers = () ->
    # go over each category
    angular.forEach $scope.gradingScale.categories, (category, key) ->
      # check if it made it past the first category
      cont = true
      # if its the last one
      if key == $scope.gradingScale.categories.length - 1
        # set the lower to the minimum: 0 %
        category.lower = 0
        # move on to the next category
        cont = false
      
      # cont will be false for only the first category
      if cont
        # grab the next category
        next = $scope.gradingScale.categories[key+1]    
        # my lower is its upper
        category.lower = next.upper

  # remove a category from the grading scale
  $scope.deleteGradingScaleCategory = (lower) ->
    # find the category we care about
    cat = _.findWhere($scope.gradingScale.categories, {lower: lower})
    # remove it from the categories list
    $scope.gradingScale.categories.splice _.indexOf($scope.gradingScale.categories, cat), 1
    # update the uppers to fill the hole
    $scope.updateUppers()

  # add the category in place in grading scale
  $scope.addGradingScaleCategory = (upper) ->
    # find the category we care about
    cat = _.findWhere $scope.gradingScale.categories, {upper: upper} 
    # and its index
    index = _.indexOf $scope.gradingScale.categories, cat  
    # grab the category after it
    next = $scope.gradingScale.categories[index - 1]
    # create a category that splits it and the next one and uses cats value
    additional =
      upper: (next.upper + cat.upper)/2
      value: cat.value
    # add it to the categories
    $scope.gradingScale.categories.splice index, 0, additional
    # update the lowers to fill the hole
    $scope.updateLowers()

  # apply the grading scale
  $scope.applyGradingScale = () ->
    # post the grading scale to the database
    $http.post('/gradebook/gradingScale/setScale/',
      gradingScale: $scope.gradingScale,
      classId: $rootScope.gradebook_id
    ).success (result) ->
      # tell the gradebook directive to recalculate the grades
      $rootScope.$broadcast 'recalculateGrades'
      # close the control element
      $scope.toggleGradingScale()
]
      
