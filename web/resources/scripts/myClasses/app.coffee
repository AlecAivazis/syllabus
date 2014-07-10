# the gradebook angular application for the syllabus web app
# author: alec aivazis

# add shortcut to underscore
_ = window._

# create the angular module
app = angular.module('myClasses', ['ngCookies'])

# add csrf tokens for proper ajax support
app.run ['$http', '$cookies', ($http, $cookies) -> 
  $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
  $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
]

app.controller 'sidebarCtrl', ['$scope', '$http', ($scope, $http) ->
  console.log 'started controller'
  # grab the current users current classes to provide links to their class page
  $http.get '/api/users/me/currentClasses/'
  # if it succeeds
  .success (result) ->
     # load the classes to the user interface
    $scope.myClasses = result
        
]
