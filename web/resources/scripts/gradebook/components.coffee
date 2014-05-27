# Directives
components = angular.module 'components', []

components.directive 'gsc', () ->
    restrict : "A",
    replace : 'true',
    templateUrl : "'../templates/gradebook/gradingScale.html'"
