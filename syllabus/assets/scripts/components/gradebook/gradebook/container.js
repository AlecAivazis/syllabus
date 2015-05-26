// the gradebook component used by the syllabus front end

// react: https://github.com/facebook/react
import React from 'react'
// local imports
import Gradebook from './component'

'use strict'

class GradebookContainer extends React.Component {

    constructor(props) {
        // instantiate this
        super(props)
        
        // initial state
        this.state = {
            users: []
        }
    }


    updateUserList(users){
        this.setState({
            users: users
        })
    }


    render() {
        return (
            <div>
                <Gradebook users={this.state.users} course={this.props.course}/>
            </div>
        )
    }
}


// export the class
export default GradebookContainer

// end of file
