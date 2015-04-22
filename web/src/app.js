// launch the application

'use strict';

import NavBar from './navigation/navBar'
import NavItem from './navigation/navItem'
import _ from 'lodash'

// the base application component for syllabus

// the current user's role (for now)
let role = 'admin';

class SyllabusRoot extends React.Component{

    constructor(){
        // create this
        super();
        // bind the various functions
        this.getNavItems = this.getNavItems.bind(this);
    }

    // return the posible navigation items for the current user
    getNavItems(){
        return [
            {
                test: "hello"
            }
        ]
    }

    // render the application
    render() {
        return (
            <NavBar>
                { _.map( this.getNavItems(), function(item) {
                    return <NavItem message={item.test}/>
                })}
            </NavBar>
        )
    }
}

// render the application to the body 
React.render(<SyllabusRoot/>, document.body)

// end of file
