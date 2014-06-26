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

    # get the appropriate dates from the server
    $http.get '/api/users/me/homework/', data
    # if it suceeded
    .success (result) ->
      # set the local variable
      $rootScope.assignments = _.groupBy result, (num) ->
        # return the various classes that this event belongs to
        return num.classes
      console.log $rootScope.assignments

    
]
