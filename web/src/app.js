// launch the application

'use strict';

// react:
import React from 'react';
// react-router:
import {RouteHandler} from 'react-router';
// lodash: https://github.com/lodash/lodash
import _ from 'lodash';
// local imports
import NavBar from './navigation/navBar';

// the base application component for syllabus
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

export default SyllabusRoot;
// end of file
