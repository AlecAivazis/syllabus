# an angular dropdown menu providing a few utilities for the syllabus gradebook
# author: alec aivazis

# add a shortcut to underscore
_ = window._

# the gradebook module
angular.module('utilities', [])

# utilities directive
.directive 'utilities', () ->
  restrict : 'AE',
  templateUrl: '../templates/gradebook/utilities.html',
  link: (scope, element, attrs) ->

    scope.figureTitle = 'Histogram'

    # safely load the grading scale in order to compute the histogram
    scope.histogram = () ->
      # hide the utilities ui element
      scope.showUtilities = false
      console.log 'opening up histogram'
      # if the grading scale does not exist
      if not scope.gradingScale
         # load it      
         scope.loadGradingScale().success (result) ->
           console.log 'loaded grading scale:'
           console.log scope.gradingScale
           # and then compute the histograms
           scope.computeHistograms()
      # otherwise
      else
         console.log 'scale is good'
         # compute the histograms
         scope.computeHistograms()
    
    # display a histogram to organize the frequency of grades
    scope.computeHistograms = () ->
    
      console.log 'computing histograms'    
      console.log 'students:'
      console.log scope.students
      # counter for the student output
      i = 0
      console.log 'starting student loop'
      # build a histogram
      data = _.countBy scope.students, (student) ->
        console.log 'student ' + i + ': '
        console.log student.totalGrade
        # based on the letter grade
        grade = scope.computeGrade student.totalGrade.score
        console.log 'computed letter: ' + grade.value
        return grade.lower

      console.log 'histogram:'              
      console.log data                             
      

      # hide the histogram / show the stats
      scope.hideGradebook = true

      # maximum value to plot is 110
      max = 110
      # draw the histogram using flot
      $.plot $("#figure"),

      [
        {
          label: null, 
          data: _.pairs(data)
        }
      ] 
      , series: 
        bars: 
          show: true,
          barWidth: 10,
        , color: '#00a8ff'
      , xaxis: 
          ticks: 10,
          min: 0,
          max: max
      , yaxis:
          tickSize: 1,
          tickDecimals: 0
      , grid:
          backgroundColor: 
            colors: ["#fff", "#f8f8f8"] 

# the view to be used by different utilities
.directive 'utilityView', () ->
  restrict : 'AE',
  templateUrl: '../templates/gradebook/figure.html'
        
