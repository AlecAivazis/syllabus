// the navigation bar used by syllabus

// imports
import React from 'react'
import NavItem from './navItem'
import _ from 'lodash'

'use strict'

// the current user's role (for now)
let roles = ['teacher'];

// the navigation bar component
class NavBar extends React.Component {

    render() {
        // get the current user's role

        return (
            <div>
                { this.props.children } 
            </div>
        )
    }
}

// export the class
module.exports = NavBar;

// end of file
