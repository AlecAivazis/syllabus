# this file implements the weekly schedule of a user based off of class objects that are
# retrieved from the syllabus api
# author: alec aivazis

# create a shortcut to underscore
_ = window._

# create the angular module
angular.module 'mySchedule', []
# add the module
.directive 'mySchedule', () ->
  restrict: 'AE'
  templateUrl: '/templates/myClasses/mySchedule.html'
  controller: 'myScheduleCtrl'
# controller for mySchedule
.controller 'myScheduleCtrl', [ '$scope', '$http', ($scope, $http) ->
  # grab the users current schedule
  $http.get '/api/users/me/schedule/'
  # if it was successful
  .success (result) ->
    # save the result
    $scope.classes = result.classes
    $scope.sections = result.sections
    # group the terms by year
    $scope.termList = _.groupBy result.terms, (term) ->
      return moment(term.start).year()

    console.log $scope.terms

]

