// the main entry point for the gradebook view

// react: https://github.com/facebook/react
import React from 'react'
// react-router: https://github.com/rackt/react-router/blob/master/docs/api/components/Link.md
import {Link, RouteHandler} from 'react-router';
// local imports
import SidebarContainer from 'components/sidebar/sidebarContainer/component'
import SidebarElement from 'components/sidebar/sidebarElement/component'
import Gradebook from 'components/gradebook/component'
import {empty_gradebook_style} from './styles'
// local flux imports
import UserStore from 'stores/userStore'
import UserActions from 'actions/userActions'

'use strict'

class GradebookRoot extends React.Component {

    constructor() {
        // instanstiate this
        super()
        // bind various functions
        this.getSidebarElements = this.getSidebarElements.bind(this)
        this.getGradebookElement = this.getGradebookElement.bind(this)
        this.getUserList = this.getUserList.bind(this)
        this.state = {
            users: []
        }
    }


    render() {
        return (   
            <SidebarContainer menuElements={this.getSidebarElements()} tier={2}>
                {this.getGradebookElement()}
            </SidebarContainer>
        )
    }


    componentDidMount(){
        // when the user store updates we need to refetch the list of users
        this.unsubscribe = UserStore.listen(this.getUserList)
    }


    componentWillUnmount(){
        // unsubscribe from the listener
        this.unsubscribe()
    }


    getUserList() {
        this.setState({
            users: UserStore.getUsers()
        })
    }


    getSidebarElements(){
        // store the sidebar elements in a list
        let elements = []
        elements.push(
            <Link to="gradebook" params={{identifier: 1}}>
                <SidebarElement>
                    Class with id 1
                </SidebarElement>
            </Link>
        )
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
        // otherwise the use specified an identifier for the gradebook
        } else {
            return <Gradebook identifier={identifier} />
        }

    }
}

GradebookRoot.contextTypes = {
  router: React.PropTypes.func
}

// export the class
export default GradebookRoot


// end of file
