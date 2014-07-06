# this file implements the weekly schedule of a user based off of class objects that are
# retrieved from the syllabus api
# author: alec aivazis

# create a shortcut to underscore
_ = window._

# create the angular module
angular.module 'myGrades', []
# add the module
.controller 'myGrades', [ '$scope', '$http',  ($scope, $http) ->
  console.log 'starting up my grades'
  # get the data from the database
  $http.get '/api/users/me/grades/'
  # if it was successful
  .success (result) ->
    # group the grades by the year of the term
    console.log result
    $scope.canGraduate = result.canGraduate
    $scope.unitsCompleted = result.unitsCompleted
    $scope.grades = _.groupBy result.grades, (classGrade) ->
      return moment(classGrade.term.start).format 'YYYY'

]


# end of file
