# the application module for the my assignments page in syllabus
# this module shows a detailed view of the gradable assignments that are due
# author: alec aivazis

# add a shortcut to underscore
_ = window._

# create the module
app = angular.module 'assignments', []
# add the controller
app.controller 'DateSelect', [ '$scope', '$http', '$rootScope' , ($scope, $http, $rootScope) ->

  # select the appropriate range 
  $scope.selectHomeworkRange = (start, end) ->
             
    # build the empty data object
    data = {}

    # if they specified a start to the range
    if start
       # add it to the object
       data['start'] = start

    # if they specified an end
    if end
       # add it to the object
       data['end'] = end

    # get the appropriate events from the server
    $http.get '/api/users/me/homework/', data
    # if it suceeds
    .success (result) ->
      # store the results grouped by
      $rootScope.assignments =  _.groupBy result, (event) ->
        # their class 
        return event.classes
    
]
