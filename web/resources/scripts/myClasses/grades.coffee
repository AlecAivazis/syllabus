# this file implements the weekly schedule of a user based off of class objects that are
# retrieved from the syllabus api
# author: alec aivazis

# create a shortcut to underscore
_ = window._

# create the angular module
angular.module 'myGrades', ['requirementList']
# add the module
.controller 'myGrades', [ '$scope', '$http',  ($scope, $http) ->
  console.log 'starting up my grades'
  # get the data from the database
  $http.get '/api/users/me/grades/'
  # if it was successful
  .success (result) ->
    # save the result
    $scope.canGraduate = result.canGraduate
    $scope.unitsCompleted = result.unitsCompleted
    # group the grades by the year of the term
    $scope.grades = _.groupBy result.grades, (classGrade) ->
      return moment(classGrade.term.start).format 'YYYY'
    # save the graduation requirements
    $scope.collegeRequirements = result.requirements.college
    $scope.majorRequirements = result.requirements.major
    

]


# end of file
