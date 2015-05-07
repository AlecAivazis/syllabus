// this store is responsible for maintaining the list of users we are aware of

// reflux: https://github.com/spoike/refluxjs
import Reflux from 'reflux'
// local imports
import userActions from '../actions/userActions'

let count = 0


let users = [
    {
        name: 'alec aivazis',
        id: 1
    }
]


// create the actual store component
let UserStore = Reflux.createStore({
    init: function() {
        // add listeners for the user actions
        this.listenTo(userActions.loadUsersInClass, this.loadUsersInClass)
    },


    loadUsersInClass: function(class_id) {
        // once we're done loading, let the component know
        this.trigger()
    },


    getUsers: function() {
        return users
    },
})

// export the store
module.exports = UserStore

// end of file
