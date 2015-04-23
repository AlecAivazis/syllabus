// the navigation bar used by syllabus

// imports
import React from 'react';
import _ from 'lodash';

// local imports
import NavItem from './navItem';
import {nav_routes} from '../routes';

'use strict'

// the current user's role (for now)
let roles = ['teacher'];

// the navigation bar component
class NavBar extends React.Component {

    render() {
        // get the current user's role

        return (
            <div>
                { _.map( nav_routes, function(item) {
                    return <NavItem message={item.name} key={item.name}/>
                })}
            </div>
        )
    }
}

// export the class
module.exports = NavBar;

// end of file
