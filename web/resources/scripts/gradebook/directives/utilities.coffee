# an angular dropdown menu providing a few utilities for the syllabus gradebook
# author: alec aivazis

# add a shortcut to underscore
_ = window._

# the gradebook module
angular.module('utilities', [])

# grading scale window directive
.directive 'utilities', () ->
  restrict : 'AE',
  templateUrl: '../templates/gradebook/utilities.html',
  controller: 'utilitiesCtrl'
# grading scale controller
.controller 'utilitiesCtrl', [ '$scope', '$http', '$rootScope', ($scope, $http, $rootScope) ->

]
      
