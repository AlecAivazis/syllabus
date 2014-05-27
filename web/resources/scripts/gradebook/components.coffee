# Directives
components = angular.module 'components', []

components.directive 'gsc', () ->
    restrict : "AE",
    replace : 'true',
    templateUrl : "../templates/gradebook/gradingScale.html"
