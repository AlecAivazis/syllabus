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

    # safely load the grading scale in order to compute the histogram
    scope.histogram = () ->

      # set the figure title
      scope.figureTitle = 'Histogram'
      # hide the utilities ui element
      scope.showUtilities = false

      # if the grading scale does not exist
      if not scope.gradingScale
         # load it      
         scope.loadGradingScale().success (result) ->
           # and then compute the histograms
           scope.computeHistograms()
      # otherwise
      else
         # compute the histograms
         scope.computeHistograms()
    
    # display a histogram to organize the frequency of grades
    scope.computeHistograms = () ->
    
      # counter for the student output
      i = 0
      # build a histogram
      data = _.countBy scope.students, (student) ->
        # based on the letter grade
        grade = scope.computeGrade student.totalGrade.score
        # binned by the lower value
        return grade.lower

      # set the maximum value for the plot
      max = 100
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

      # hide the gradebook / show the stats
      scope.hideGradebook = true

    # plot the averages of each event
    scope.timeline = () ->

      # set the figure title
      scope.figureTitle = 'Timeline'
      # hide the utilities ui element
      scope.showUtilities = false

      # store the data in a list
      data = []
      # keep the index of the loop iteration
      index = 0
      angular.forEach scope.events, (event) ->
        # add the necessary data to the list
        data.push([index, event.average])
        # increment index
        index++

      # draw the histogram using flot
      $.plot $("#figure"),

       [
         {
           label: null, 
           data: data
         }
       ] 
       , series: 
         lines: 
           show: true,
           fill: false
         , points:
           show: true,
           fill: false
         , color: '#00a8ff'
       , xaxis: 
           ticks: 10,
           min: 0,
       , grid:
           backgroundColor: 
             colors: ["#fff", "#f8f8f8"]
           , hoverable: true
 
      # hide the gradebook / show the stats
      scope.hideGradebook = true

      # tooltips are implemented in the old gradebook.js

    # track the grade as a function of time by event
    scope.performance = () ->
      console.log 'you want to look at the classes performance'

      

# the view to be used by different utilities
.directive 'utilityView', () ->
  restrict : 'AE',
  templateUrl: '../templates/gradebook/figure.html',

        
