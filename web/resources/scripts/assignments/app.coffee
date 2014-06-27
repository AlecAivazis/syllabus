# the application module for the my assignments page in syllabus
# this module shows a detailed view of the gradable assignments that are due
# author: alec aivazis

# add a shortcut to underscore
_ = window._

# create the module
app = angular.module 'assignments', ['ngCookies', 'homeworkItemList']

# add csrf tokens for proper ajax support
app.run ['$http', '$cookies', ($http, $cookies) -> 
  $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
  $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
]

# add the controller
app.controller 'DateSelect', [ '$scope', '$http', '$rootScope', ($scope, $http, $rootScope) ->

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
    $http.get '/api/users/me/homework/', params: data
    # if it suceeds
    .success (result) ->
      # separate the data if it
      dataSplit = _.partition result, (event) ->
        # has been turned in already
        isTurnedIn = event.status is 'turned-in'
        # return the result (this is some coffeescript weirdness i think
        return isTurnedIn

      # store the two lists
      $rootScope.turnedIn = _.groupBy dataSplit[0], (event) ->
        return event.classes
      $rootScope.assignments = _.groupBy dataSplit[1], (event) ->
        return event.classes
      
      
  # the initial state of this page is to display todays homework
  $scope.selectHomeworkRange 'today', 'today'
]