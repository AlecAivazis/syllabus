// launch the application

'use strict';

import NavBar from './navigation/navBar'
import NavItem from './navigation/navItem'

// the base application component for syllabus

class SyllabusRoot extends React.Component{
    render() {
        return (
            <NavBar>
                <NavItem/>
            </NavBar>
        )
    }
}

// render the application to the body 
React.render(<SyllabusRoot/>, document.body)

// end of file
