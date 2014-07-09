# the gradebook table as an angularjs directive
# author: alec aivazis

# add a shortcut to underscore
_ = window._

# the gradebook module
angular.module('gradebook', [])

# the gradebook directive
.directive 'gradebook', () ->
  restrict: 'AE',
  templateUrl: '/templates/gradebook/gradebook.html',
  controller: 'gradebookCtrl'

# the gradebook controller
.controller 'gradebookCtrl' , [ '$scope', '$http', '$rootScope', ($scope, $http, $rootScope) ->

  # listen for when the weights need to be recalcualted
  $rootScope.$on 'recalculateWeights', () ->
    $scope.recalculateWeights()

  # listen for when the grades need to be recalcualted
  $rootScope.$on 'recalculateAverages', () ->
    $scope.recalculateAverages()

  # listen for when the averages need to be recalcualted
  $rootScope.$on 'recalculateGrades', () ->
    $scope.recalculateGrades()

  # user interface functions

  # toggle the gradebook
  $scope.toggleGradebook = () ->
    $scope.hideGradebook = !$scope.hideGradebook

  # update the event category in the database with its current value
  $scope.updateEventCategory = (eventId) ->
    # get the event we care about
    event = _.where($scope.events, {id: eventId})[0]
    #  update its category on the database
    $http.post('/gradebook/changeCategory/', 
      id: event.id, 
      value: event.category
    ).success (result) ->
      $scope.recalculateWeights()
      $scope.recalculateGrades()
  
  # update the event possible points on the database with its current value in the model
  $scope.updatePossiblePoints = (eventId) ->
    # get the event we care about
    event = _.where($scope.events, {id: eventId})[0]
    #  update its possiblePossible on the database
    $http.post('/gradebook/changePossiblePoints/', 
      id: event.id, 
      value: event.possiblePoints
    ).success (result) ->
      $scope.recalculateGrades()

  # update the grade for a student/event on the database   
  $scope.updateGrade = (studentId, eventId) ->
    # get the grade we care about
    grade = $scope.gradebook[studentId][eventId].grade
    # update the grade on the server
    $http.post('/gradebook/addgrade/', 
      student: studentId,
      event: eventId,
      score: grade,
    ).success (result) ->
      $scope.recalculateGrades()
      $scope.recalculateAverages()

  # compute the average of each event
  $scope.recalculateAverages = () ->
    # save the number of students so it only has to be computed one
    nStudents = $scope.students.length
    # go over each event
    angular.forEach $scope.events, (event) ->
      # compute the sum of the grades for each student
      total =  _.reduce $scope.students, (memo, student) ->
        return memo += $scope.gradebook[student.id][event.id].grade
      , 0
      # set the average
      event.average = total/nStudents
    # compute the average student grade
    total = _.reduce $scope.students, (memo, student) ->
      return memo += parseFloat(student.totalGrade.score)
    , 0
    # set the $scope variable
    $scope.totalAverage = total/nStudents

  $scope.computeWeights = () ->
    # grab a list of the unique categories
    categories = _.uniq _.pluck($scope.events, 'category')
    # loop over the categories
    angular.forEach categories, (category) ->
      # calculate the total number of possible points for this category
      totalPoints = _.reduce _.where($scope.events, {category:category}), (memo, event) ->
        return memo + parseInt(event.possiblePoints)
      , 0
      # get the weight for the entire group
      weight = _.where($scope.weights.categories, {category: category})[0].percentage
      # calculate the weight per point
      weightPerPoint = weight/totalPoints
      # go over every event in the category
      angular.forEach _.where($scope.events, {category: category}), (category) ->
        # set its weight
        category.weight = Math.round(category.possiblePoints * weightPerPoint)

  # load the weights if necessary before calculating
  $scope.recalculateWeights = () ->
    # if the weights are already loaded
    if not $scope.weights
      # load the weights from the syllabus api
      $scope.loadWeights().success (result) ->
        # prevent the weights from loading again
        refreshWeights = false
        # recalculate the weights
        $scope.computeWeights()
    # otherwise
    else
      # recalculate the weights
      $scope.computeWeights()

  # compute the grades of each user
  $scope.computeGrades = () ->
    # loop over each student
    angular.forEach $scope.students, (student) ->
      # store the total score for this student
      totalScore = 0
      # for each event
      angular.forEach $scope.events, (event) ->
        # grab the score for this student
        grade = $scope.gradebook[student.id][event.id].grade
        # add the weighted grade to the totalScore
        totalScore += parseFloat((grade/parseInt(event.possiblePoints)) * event.weight)

      # set the students grade
      # the letter is given by the grading scale control
      # the score is totalScore rounded to 1 decimal place
      student.totalGrade =
        letter: $scope.computeGrade(totalScore).value
        score: totalScore.toFixed(1)

  # recalculate the grade of each student
  $scope.recalculateGrades = () ->
    # check if the gradingScale has loaded yet
    if not $scope.gradingScale
      # load the grading scale from the syllabus api
      $scope.loadGradingScale().success (result) ->
        # prevent the regradingScale from refreshing
        refreshGradingScale = false
        # compute the grades
        $scope.computeGrades()
    # otherwise
    else
      # compute the grades
      $scope.computeGrades()
]
