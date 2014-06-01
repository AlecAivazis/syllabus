// Generated by CoffeeScript 1.7.1
(function() {
  var gradebook;

  gradebook = angular.module('gradebook-app', ['ngCookies']);

  gradebook.run([
    '$http', '$cookies', function($http, $cookies) {
      $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
      return $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
    }
  ]);

  gradebook.controller('ClassSelect', function($scope, $http, $rootScope) {
    $scope.classes = [];
    $http.get('/api/classes/taughtByMe/').success(function(result) {
      return angular.forEach(result, function(item) {
        return $scope.classes.push(item);
      });
    });
    return $scope.loadGradeBook = function(id) {
      return $rootScope.gradebook_id = id;
    };
  });

  gradebook.controller('gradebook-view', function($scope, $rootScope, $http) {
    var class_id, refreshGradingScale, refreshWeights;
    class_id = $rootScope.$watch('gradebook_id', function() {
      if (!$rootScope.gradebook_id) {
        return;
      }
      $http.get('/api/classes/' + $rootScope.gradebook_id + '/gradebook/').success(function(result) {
        $scope.breadcrumb = result.breadcrumb;
        $scope.events = result.events;
        $scope.gradebook = result.gradebook;
        return $scope.students = result.students;
      });
      return class_id = $rootScope.gradebook_id;
    });
    refreshWeights = true;
    $scope.toggleWeightControl = function() {
      if (refreshWeights) {
        $http.get('/api/classes/' + class_id + '/weights/').success(function(result) {
          $scope.weights = result;
          return refreshWeights = false;
        });
      }
      return $scope.displayWeightControl = !$scope.displayWeightControl;
    };
    refreshGradingScale = true;
    return $scope.toggleGradingScale = function() {
      if (refreshGradingScale) {
        $http.get('/api/classes/' + class_id + '/gradingScale/').success(function(result) {
          $scope.gradingScale = result;
          return $scope.updateUppers();
        });
        refreshGradingScale = false;
      }
      return $scope.showGradingScale = !$scope.showGradingScale;
    };
  });

  gradebook.directive('wc', function() {
    return {
      restrict: 'AE',
      templateUrl: '../templates/gradebook/weights.html',
      link: function(scope, elem, attrs) {
        scope.addCategory = function() {
          if (scope.newCategory && scope.newPercentage) {
            scope.weights.categories.push({
              category: scope.newCategory,
              percentage: scope.newPercentage
            });
            scope.newCategory = null;
            scope.newPercentage = null;
          } else {

          }
          return scope.canSubmitWidget = scope.canSubmit();
        };
        return scope.canSubmit = function() {
          var percentages, sum, _;
          _ = window._;
          if (!scope.weights) {
            return true;
          }
          percentages = _.pluck(scope.weights.categories, 'percentage');
          sum = _.reduce(percentages, function(memo, num) {
            return memo + parseInt(num);
          }, 0);
          if (sum === 100) {
            return true;
          } else {
            return false;
          }
        };
      }
    };
  });

  gradebook.directive('gsc', function() {
    return {
      restrict: 'AE',
      templateUrl: '../templates/gradebook/gradingScale.html',
      link: function(scope, elem, attrs) {
        scope.updateUppers = function() {
          return angular.forEach(scope.gradingScale.categories, function(category, key) {
            var cont, prev;
            cont = true;
            if (key === 0) {
              category.upper = 100;
              cont = false;
            }
            if (cont) {
              prev = scope.gradingScale.categories[key - 1];
              return category.upper = prev.lower;
            }
          });
        };
        return scope.updateLowers = function() {
          return angular.forEach(scope.gradingScale.categories, function(category, key) {
            var cont, next;
            cont = true;
            if (key === scope.gradingScale.categories.length - 1) {
              category.lower = 0;
              cont = false;
            }
            if (cont) {
              next = scope.gradingScale.categories[key + 1];
              return category.lower = next.upper;
            }
          });
        };
      }
    };
  });

  gradebook.directive('gradebook', [
    '$http', function($http) {
      return {
        restrict: 'AE',
        templateUrl: '../templates/gradebook/gradebook.html',
        link: function(scope, elem, attrs) {
          var _;
          _ = window._;
          scope.updateEventCategory = function(eventId) {
            var event;
            event = _.where(scope.events, {
              id: eventId
            })[0];
            return $http.post('/gradebook/changeCategory/', {
              id: event.id,
              value: event.category
            }).success(function(result) {
              return $scope.weights = result;
            });
          };
          scope.updatePossiblePoints = function(eventId) {
            var event;
            event = _.where(scope.events, {
              id: eventId
            })[0];
            return $http.post('/gradebook/changePossiblePoints/', {
              id: event.id,
              value: event.possiblePoints
            });
          };
          return scope.updateGrade = function(studentId, eventId) {
            var grade;
            grade = scope.gradebook[studentId][eventId].grade;
            return $http.post('/gradebook/addgrade/', {
              student: studentId,
              event: eventId,
              score: grade
            });
          };
        }
      };
    }
  ]);

}).call(this);
