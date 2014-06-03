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
  link: (scope, element, attrs) ->

    # display a histogram to organize the frequency of grades
    scope.histogram = () ->
      scope.hideGradebook = true
      console.log 'opening up histogram'
      
