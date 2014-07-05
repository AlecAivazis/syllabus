# this file implements the weekly schedule of a user based off of class objects that are
# retrieved from the syllabus api
# author: alec aivazis

# create a shortcut to underscore
_ = window._

# create the angular module
angular.module 'mySchedule', []
# add the module
.controller 'myScheduleCtrl', [ '$scope', '$http', '$rootScope',  ($scope, $http, $rootScope) ->

  # load a specific terms calendar for the user
  $scope.selectTerm = (name, year) ->
    # prepare the request data if its empty 
    data =
      name: name
      year: year
    # get the data from the database
    $http.get '/api/users/me/schedule/', params: data
    # if it was successful
    .success (result) ->
      # save the result
      $scope.classes = serializeClasses result.classes
      $scope.sections = serializeClasses result.sections
      # group the terms by year
      $scope.termList = _.groupBy result.terms, (term) ->
        # use moment to get the year from the string // overkill??
        return moment(term.start).year()
      # load the events into the user interface
      $scope.events = [$scope.classes, $scope.sections]

  # default view is to select the current term
  $scope.selectTerm()

  # turn a list of syllabus classes into events approprirate for the ui calendar
  serializeClasses = (list) ->
    data = []

    # center the calendar around this week
    startofWeek = moment().startOf 'week'

    # loop over the list
    angular.forEach list, (event) ->
      # grab the appropriate day
      day = startofWeek.add 'days', event.day
      # add the appropriate data to the list
      data.push
        title: event.name
        # add the day string to the time and parse it in moment
        start: moment day.format('YYYY-MM-DD:Z') + ' ' + event.start , 'YYYY-MM-DD:Z H:mm:ss'
        end: moment day.format('YYYY-MM-DD:Z') + ' ' + event.end , 'YYYY-MM-DD:Z H:mm:ss'

    # return the serialized data
    return data
        

  # configure the weekly calendar
  $scope.weeklyCalendar =
    height: 400
    weekMode: 'liquid'
    editable: false    
       
]


# end of file
