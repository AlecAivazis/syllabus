// this store is responsible for maintaining the list of grades we are aware of

// reflux: https://github.com/spoike/refluxjs
import Reflux from 'reflux'
// local imports
import gradeActions from '../actions/gradeActions'

let count = 0


let grades = [
    {
        student: 1,
        assignment: 1,
        score: 90
    },
    {
        student: 1, 
        assignment: 2,
        score: 95
    }
]


// create the actual store component
let GradeStore = Reflux.createStore({
    init: function() {
        // add listeners for the user actions
        this.listenTo(gradeActions.submitGrade, this.submitGrade)
    },


    submitGrade: function(class_id) {
        // once we're done loading, let the component know
        this.trigger(users)
    },
})

// export the store
module.exports = GradeStore

// end of file
