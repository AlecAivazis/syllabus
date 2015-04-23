// the root component for the front end application

'use strict';

// react: https://github.com/facebook/react
import React from 'react';
// react-router: https://github.com/rackt/react-router
import {RouteHandler} from 'react-router';
// local imports
import NavBar from './navigation/navBar';

// the base application component for the frontend
class Index extends React.Component{

    // render the application
    render() {
        return (
            <div>
                <NavBar/>
                <RouteHandler/>
            </div>
        )
    }
}

// export the component
export default Index;

// end of file
