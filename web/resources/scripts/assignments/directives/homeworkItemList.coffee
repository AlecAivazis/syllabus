# the loop over a specific list of homework assignments
# author: alec aivazis

# add a shortcut to underscore
_ = window._

# the gradebook module
angular.module('homeworkItemList', [])

# the gradebook directive
.directive 'homeworkItemList', () ->
  restrict: 'AE'
  templateUrl: '../templates/myhomework/homeworkItemList.html'
  controller: 'homeworkItemListCtrl'
  scope:
    container: '='
    buttonText: '='
    buttonClass: '='

# the gradebook controller
.controller 'homeworkItemListCtrl' , [ '$scope', '$http', '$rootScope', ($scope, $http, $rootScope) ->

  # figure out the right js function to call
  $scope.eventAction = (text, id)->
    switch text
      when 'submit' then $scope.turnIn id
      when 'revoke' then $scope.revoke id
  
  # turn in an assignment
  $scope.turnIn = (id) ->
    # post the request to the server
    $http.post '/myHomework/turnIn/', eventId: id
    # if it succedes
    .success (result) ->
      # grab the appropriate javascript event
      event = _.findWhere $rootScope.assignments, id: id
      console.log event

  $scope.revoke = (id) ->
    console.log $rootScope.turnedIn
    console.log 'you want to revoke this event'
    # grab the appropriate javascript event
    event = _.findWhere $rootScope.turnedIn, id: id
    console.log event
    

]

