// the gradebook component used by the syllabus front end

// react: https://github.com/facebook/react
import React from 'react'
// local imports
import Gradebook from './component'
// local flux imports
import UserStore from 'stores/userStore'
import UserActions from 'actions/userActions'


'use strict'

class GradebookContainer extends React.Component {

    constructor(props) {
        // instantiate this
        super(props)
        // bind various functions
        this.getUserList = this.getUserList.bind(this)
        
        // initial state
        this.state = {
            users = []
        }
    }


    getUserList(){
        this.setState({
            users: UserStore.getUsers()
        })
    }


    componentDidMount(){
        // when the user store updates we need to refetch the list of users
        this.unsubscribe = UserStore.listen(this.getUserList)
        // load the users for the specified class
        UserActions.loadUsersInClass(this.props.identifier)
    }


    componentWillUnmount(){
        // unsubscribe from the listener
        this.unsubscribe()
    }


    render() {

        return (
            <div>
                <div>
                    hello
                    {this.state.users}
                </div>
                <Gradebook identifier={this.props.identifier} />
            </div>
        )
    }
}


// export the class
export default GradebookContainer

// end of file
