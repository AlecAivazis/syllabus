# this directive handles the showing a particular list of requirements
# author: alec aivazis

# create the module
angular.module 'requirementList', []

# add the directive
.directive 'requirementList', () ->
  restrict: 'AE'
  templateUrl: '/templates/myClasses/requirementList.html'
  scope:
    'list' : '='
  replace: true
