// the root component for the front end application

'use strict';

// react: https://github.com/facebook/react
import React from 'react';
// react-router: https://github.com/rackt/react-router
import {RouteHandler} from 'react-router';
// normalize.css: http://necolas.github.io/normalize.css/
require('normalize.css');
// local imports
import NavBar from '../components/navigation/navBar/component';
require('styles/noise.css');


// the base application component for the frontend
class SyllabusRoot extends React.Component{

    // render the application
    render() {
        return (
            <div>
                <NavBar/>
                <div style={mainContainerStyle} className="noise-004">
                    <RouteHandler/>
                </div>
            </div>
        )
    }
}

//// styles ////

let mainContainerStyle = {
    position: 'fixed',
    left: '0px',
    right: '0px',
    bottom: '0px', 
    // make sure we line up with the NavBar component
    top: require('../components/navigation/navBar/styles').nav_style.height,
    background: '#dfddd1'
}


// export the component
export default SyllabusRoot;

// end of file
