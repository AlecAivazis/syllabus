// the main entry point for the gradebook view

// react: https://github.com/facebook/react
import React from 'react'
// react-router: https://github.com/rackt/react-router/blob/master/docs/api/components/Link.md
import {Link, RouteHandler} from 'react-router';
// local imports
import SidebarContainer from 'components/sidebar/sidebarContainer/component'
import SidebarElement from 'components/sidebar/sidebarElement/component'
import Gradebook from 'components/gradebook/gradebook/container'
import {empty_gradebook_style} from './styles'

'use strict'

class GradebookRoot extends React.Component {

    constructor() {
        // instanstiate this
        super()
        // bind various functions
        this.getSidebarElements = this.getSidebarElements.bind(this)
        this.getGradebookElement = this.getGradebookElement.bind(this)
        // initial state
        this.state = {
            courses: [
                {
                    name: 'phys 20',
                    id: 1
                },
            ]
        }
    }


    render() {
        return (   
            <SidebarContainer menuElements={this.getSidebarElements()} tier={2}>
                {this.getGradebookElement()}
            </SidebarContainer>
        )
    }


    getSidebarElements(){
        // store the sidebar elements in a list
        let elements = []
        // for each course in the list
        this.state.courses.forEach( course => {
            // add a link to the sidebar that points to the specific gradebook
            elements.push(
                <Link to="gradebook" params={{identifier: course.id}}>
                    <SidebarElement>
                        {course.name}
                    </SidebarElement>
                </Link> 
            ) 
        })
        // return the elements
        return elements
    }


    getGradebookElement() {
        // grab the route from the context
        let {router} = this.context
        // save a reference to the specified identified
        let identifier = router.getCurrentParams().identifier
        // if they did not specify an identifier
        if (!identifier){
            // return a placeholder element
            return (
                <div style={empty_gradebook_style}>
                    Please select a class to view its gradebook       
                </div>
            )
        // otherwise the user specified an identifier for the gradebook
        } else {
            let course = this.state.courses[0]
            // return the gradebook element for that course
            return <Gradebook course={course}/>
        }
    }
}

GradebookRoot.contextTypes = {
    router: React.PropTypes.func
}


// export the class
export default GradebookRoot

// end of file
