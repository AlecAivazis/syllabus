// launch the application

'use strict';

import NavBar from './navigation/navBar'
import 'babel/polyfill'

// the base application component for syllabus
class SyllabusRoot extends React.Component{

    // render the application
    render() {
        return (
            <NavBar />
        )
    }
}

// render the application to the body 
React.render(<SyllabusRoot/>, document.body)

// end of file
