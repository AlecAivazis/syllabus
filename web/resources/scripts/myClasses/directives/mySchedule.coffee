# this file implements the weekly schedule of a user based off of class objects that are
# retrieved from the syllabus api
# author: alec aivazis

# create the angular module
angular.module 'mySchedule', []
# add the module
.directive 'mySchedule', () ->
  restrict: 'AE'
  templateUrl: '/templates/myClasses/mySchedule.html'
  controller: 'myScheduleCtrl'
# controller for mySchedule
.controller 'myScheduleCtrl', [ '$scope', ($scope) ->
  console.log 'starting mySchedule control'
]

