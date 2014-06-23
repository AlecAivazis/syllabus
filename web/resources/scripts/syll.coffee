# this app handles which links to show the user to navigate the syllabus app
# author: alec aivazis

# create the app
nav = angular.module 'syllabus-nav' , []

nav.controller 'navCtrl', [ '$scope' , ($scope) ->

  # return if the user is an administrator
  $scope.isAdmin = () ->
    return 'admin' in $scope.roles

  # return if the user is a student
  $scope.isStudent = () ->
    return 'student' in $scope.roles

  # return if the user is a teacher
  $scope.isTeacher = () ->
    return 'faculty' in $scope.roles

  # return if the user is a registrar
  $scope.isRegistrar = () ->
    return 'registrar' in $scope.roles

]
