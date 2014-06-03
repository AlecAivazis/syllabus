# the weight control as an angularjs directive
# author: alec aivazis

# add a shortcut to underscore
_ = window._

# the gradebook module
angular.module('wc', [])

# grading scale window directive
.directive 'wc', () -> 
  restrict : 'AE',
  templateUrl: '../templates/gradebook/weights.html',
  controller: 'wcCtrl'
# grading scale controller
.controller 'wcCtrl', [ '$scope' ,'$http', '$rootScope', ($scope, $http, $rootScope) ->

  # load the weights from the syllabus api
  $scope.loadWeights = () ->
    return $http.get('/api/classes/' + $rootScope.gradebook_id + '/weights/')
                .success (result) ->
        # load the result
        $scope.weights = result

  # check if a new category needs to be added
  $scope.addCategory = () ->
    if $scope.newCategory && $scope.newPercentage 
      # add the new weight
      $scope.weights.categories.push
        category: $scope.newCategory,
        percentage: $scope.newPercentage
      # wipe the containers for the new ones
      $scope.newCategory = null
      $scope.newPercentage = null
    else
    # update the submit button        
    $scope.canSubmitWidget = $scope.canSubmit()
        
  # return if the widget can be submitted ie the percentages add up to 100
  $scope.canSubmit = () ->
    # if there are no weights you can submit to remove
    if ! $scope.weights 
      return true

    # grab the percentage of each category
    percentages = _.pluck($scope.weights.categories, 'percentage')
    # compute their sum
    sum = _.reduce(percentages, (memo, num) ->
      memo + parseInt(num)
    , 0)
    # if they add up to 100
    if sum == 100
      # then you can submit the widget
      return true
    # otherwise
    else
      # you cannot
      return false
      
    # remove a given index from the weights
    $scope.removeCategory = (index) ->
      # remove the index
      $scope.weights.categories.splice(index, 1)
      # update the submit button
      $scope.canSubmitWidget = $scope.canSubmit()

  # update the weights on the database and recalculate the grades
  $scope.updateWeights = () ->
    # check that this is allowed
    if not $scope.canSubmitWidget
      # if its not, get out
      return
    # otherwise set the weights
    $http.post('/gradebook/weights/set/',
      'classId' : $rootScope.gradebook_id,
      'weights' : $scope.weights
    ).success (result) ->
      $scope.toggleWeightControl()
      # tell the gradebook directive to recalculate the necessary quantities
      $rootScope.$broadcast 'recalculateWeights'
      $rootScope.$broadcast 'recalculateGrades'
      $rootScope.$broadcast 'recalculateAverages'
]      
