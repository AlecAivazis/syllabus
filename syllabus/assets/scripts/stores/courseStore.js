// this store is responsible for maintaining the list of users we are aware of

// reflux: https://github.com/spoike/refluxjs
import Reflux from 'reflux'
// lodash: https://github.com/lodash/lodash
import _ from 'lodash'
// local imports
import courseActions from '../actions/courseActions'


let courses = [
    {
        name: 'Phys 20',
        id: 1,
        professor: 1
    }
]


// create the actual store component
let courseStore = Reflux.createStore({
    init: function() {
        // add listeners for the user actions
        this.listenTo(courseActions.loadCoursesTaughtBy, this.loadCoursesTaughtBy)
    },


    loadCoursesTaughtBy: function(user_id) {
        // once we're done loading, let the component know
        this.trigger(courses)
    },


    getCourseById: function(course_id) {
        // return the course with a matching id
        return _.first(_.filter(courses, {id: course_id}))
    }
})

// export the store
module.exports = courseStore

// end of file
