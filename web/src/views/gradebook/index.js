// the main entry point for the gradebook view

// react: https://github.com/facebook/react
import React from 'react'
// react-router: https://github.com/rackt/react-router/blob/master/docs/api/components/Link.md
import {Link, RouteHandler} from 'react-router';
// local imports
import SidebarContainer from 'components/sidebar/sidebarContainer/component'
import SidebarElement from 'components/sidebar/sidebarElement/component'

'use strict'

class GradebookRoot extends React.Component {

    constructor() {
        // instanstiate this
        super()
        // bind various functions
        this.getSidebarElements = this.getSidebarElements.bind(this)
    }

    render() {
        return (   
            <SidebarContainer menuElements={this.getSidebarElements()} tier={2}>
                <RouteHandler />
            </SidebarContainer>
        )
    }


    getSidebarElements(){
        // store the sidebar elements in a list
        let elements = []
        elements.push(
            <Link to="view_gradebook" params={{class_id: 1}}>
                <SidebarElement>
                    hello
                </SidebarElement>
            </Link>
        )
        // return the elements
        return elements
    }
}

// export the class
export default GradebookRoot


// end of file
