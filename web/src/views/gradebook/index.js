// the main entry point for the gradebook view

// react: https://github.com/facebook/react
import React from 'react'
// local imports
import SidebarContainer from 'components/sidebar/sidebarContainer/component'

'use strict'

class GradebookRoot extends React.Component {
    render() {
        return (   
            <SidebarContainer />
        )
    }
}

// export the class
export default GradebookRoot


// end of file
