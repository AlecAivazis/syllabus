# the calendar angular application for the syllabus web app
# used by professors to manage when their assignments are due
# author: alec aivazis

# create the angular module
app = angular.module('calendar-app', ['ngCookies', 'calendar'])

# add csrf tokens for proper ajax support
app.run ['$http', '$cookies', ($http, $cookies) -> 
  $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
  $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
]

