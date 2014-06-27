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
    $http.post '/myHomework/updateEventState/',
      eventId: id
      status: 'turned-in'
    # if it succedes
    .success (result) ->
       # grab the appropriate event
      event = _.findWhere $rootScope.assignmentsRaw, id: id
      # remove it from the raw list of assignments
      $rootScope.assignmentsRaw = _.without $rootScope.assignmentsRaw, event
      # add it to the raw list of turned in events
      $rootScope.turnedInRaw.push event
      # refresh the user interface
      $rootScope.buildLists()

  $scope.revoke = (id) ->
    # post the request to the server
    $http.post '/myHomework/updateEventState/',
      eventId: id
      status: 'revoked'
    # if it succedes
    .success (result) ->
      # grab the appropriate event
      event = _.findWhere $rootScope.turnedInRaw, id: id
      # remove it from the raw list of turned in events
      $rootScope.turnedInRaw = _.without $rootScope.turnedInRaw, event
      # add it to the raw list of assignments
      $rootScope.assignmentsRaw.push event
      # refresh the user interface
      $rootScope.buildLists()

]

