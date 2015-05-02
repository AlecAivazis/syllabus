// a container for sidebar elements which link to subsequent views

// react: https://github.com/facebook/react
import React from 'react'
// local imports
import {container_style} from './styles'

'use strict'

class SidebarContainer extends React.Component {


    constructor(props){
        // instantiate this
        super()
        // bind various function
        this.getMenuElements = this.getMenuElements.bind(this)
    }


    render() {
        return (
            <div>
                <ul style={container_style}>
                    {this.getMenuElements()}
                </ul>
                <div>
                    content
                </div>
            </div>
        )
    }


    getMenuElements() {
        return <li>hello</li>
    }
}

// export the class
export default SidebarContainer

// end of file
