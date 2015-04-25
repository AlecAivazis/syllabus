// the root component for the front end application

'use strict';

// react: https://github.com/facebook/react
import React from 'react';
// react-router: https://github.com/rackt/react-router
import {RouteHandler} from 'react-router';
// normalize.css: http://necolas.github.io/normalize.css/
import 'normalize.css'
// local imports
import NavBar from './components/navigation/navBar/component';


// the base application component for the frontend
class SyllabusRoot extends React.Component{

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
export default SyllabusRoot;

// end of file
