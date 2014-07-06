# this file implements the weekly schedule of a user based off of class objects that are
# retrieved from the syllabus api
# author: alec aivazis

# create a shortcut to underscore
_ = window._

# create the angular module
angular.module 'mySchedule', ['ui.directives']
# add the module
.controller 'myScheduleCtrl', [ '$scope', '$http',  ($scope, $http) ->

  # store the events to be displayed by the schedule
  $scope.events = []
        
  # load a specific terms calendar for the user
  $scope.selectTerm = (name, year) ->
    # clear the current list of events
    $scope.events = []
    # prepare the request data if its empty 
    data =
      name: name
      year: year
    # get the data from the database
    $http.get '/api/users/me/schedule/', params: data
    # if it was successful
    .success (result) ->
      # load the events into the user interface
      $scope.events.push serializeClasses result.classes
      $scope.events.push serializeClasses result.sections
      # set the title of the schedule
      $scope.title = result.terms.selected
      # group the terms by year
      $scope.termList = _.groupBy result.terms.list, (term) ->
        # use moment to get the year from the string // overkill??
        return moment(term.start).year()

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
      # build the start and end days
      # add the day string to the time and parse it in moment
      start = moment day.format('YYYY-MM-DD:Z') + ' ' + event.start , 'YYYY-MM-DD:Z H:mm:ss'
      end = moment day.format('YYYY-MM-DD:Z') + ' ' + event.end , 'YYYY-MM-DD:Z H:mm:ss'
      # add the appropriate data to the list
      data.push
        title: event.name
        start: start.format()
        end: end.format()
        allDay: false

    # return the serialized data
    return data
        

  # configure the weekly calendar
  $scope.weeklyCalendar =
    defaultView: 'agendaWeek'
    minTime: '8:00 am'
    maxTime: '8:00 pm'
    header:
      left: ''
      center: ''
      right: ''
    height: 600
    weekMode: 'liquid'
    editable: false    

]


# end of file
