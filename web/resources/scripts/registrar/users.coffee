# this is the coffee script front end for the user list 

$(document).ready ->

  # add watermarks to filters
  $('#name').watermark 'Enter Name...'
  $('#perm').watermark 'Enter Perm Number...'

  # show the tools on mouseover
  $('.user').on 'mouseenter', ->
    $(this).children('.userTools').eq(0).children().show()
  # hide on mouseleave
  .on 'mouseleave', ->
    $(this).children('.userTools').eq(0).children().hide()
    

# open the users profile
userProfile = (id) ->
  # get it from the server
  $.ajax
    url: '/registrar/users/userProfile/',
    data:
      id: id
    success: (data) ->
      overlay(data)

# update the courses of an interest
updateInterestCourses = (id) ->
  $.ajax
    url: '/registrar/getInterestClasses/'
    data:
      id: id
    success: (data) ->
      alert 'hello'


# refresh the user list off of the database
refreshUserList = () ->
  $.ajax
    url: '/registrar/users/list/'
    success: (data) ->
      # remove the users from the list
      $('.user').remove()
      $('tr:first-child').after(data);

      # show the tools on mouseover
      $('.user').on 'mouseenter', ->
        $(this).children('.userTools').eq(0).children().show()
      # hide on mouseleave
      .on 'mouseleave', ->
        $(this).children('.userTools').eq(0).children().hide()
    

# filter the list of users based on the sidebar parameters
filterList = () ->
  # show all of the users
  $('.user').show()

  # remove the users that dont match

  # filter by name
  name = $('#name').val()
  #if they supplied a name
  if name
    # go over every user
    $('.user').each ->
      # check if the string is not in the html of the element
      if $(this).children().eq(0).html().indexOf(name) == -1
        # if it isnt hide it
        $(this).hide()

  # filter by id
  id = $('#perm').val()
  # if they supplied an id
  if id
    $('.user').each ->
      if $(this).children().eq(1).html().indexOf(id) == -1
        $(this).hide()

  # filter by role
  role = $('#role').val()
  # if they supplied a role
  if role
    $('.user').each ->
      if $(this).children().eq(2).html().indexOf(role) == -1 
        $(this).hide();

# remove a user from the database
deleteUser = (id) ->
  # verify with the user
  if confirm 'Are you sure you want to delete this user from the database?'
    # tell the database
    $.ajax
      url: '/registrar/users/delete/',
      data:
        id: id
      # if it succeeded
      success: (data) ->
        # remove the ui element
        $('#' + id).remove()

# open the new user form
newUser = () ->
  $.ajax
    url: '/registrar/users/new/',
    success: (data) ->
      overlay data
    
# create a new user by submitting the form
createUser = () ->
  # check that both of the passwords match
  if $('#pass1').val() != $('#pass2').val()
    return
  # save the designated password
  pass = $('#pass1').val()
  # submit the form data
  $.ajax
    url: '/registrar/users/create/'
    type: 'POST'
    data:
      firstName : $('#firstName').val()
      lastName: $('#lastName').val()
      username: $('#username').val()
      password : pass
      email: $('#email').val()
      role: $('#roleSelect').val()
    success: (data) ->
      closeOverlay()
      refreshUserList()

# bring up the edit user form
editUser = (id) ->
  $.ajax
    url: '/registrar/users/edit/'
    data:
      id: id
    success: (data) ->
      overlay data


#  view the class profile
viewProfile = (id) ->
  $.ajax
    url: '/registrar/classes/profile/'
    data:
      id: id
    success: (data) ->
      $('#classes').empty().append data


# get the course numbers in a given interest
getInterestCoruseNumbers = (id, self) ->
  $.ajax
    url: '/registrar/users/getInterestCourseNumbers'
    data:
      id: id
    success: (data) ->
      $(this).parent().siblings('.courseNumbers').empty().append data


# bring up the exemption form for a particular user
newExemption = (id) ->
  $.ajax
    url: '/registrar/users/addExemption/'
    data:
      id: id
    success: (data) ->
      $('#userInfo').hide()
      $('#exemptionForm').empty().append(data).show()

# return the possible classes for a given exemption
getPossibleClasses = (id) ->
  $.ajax
    url: '/registrar/users/getPossibleClassesForExemption/',
    data:
      id: id
    success: (data) ->
      console.log data 
