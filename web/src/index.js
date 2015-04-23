// the main entry point for the syllabus frontend

'use strict'

// react: https://github.com/facebook/react
import React from 'react';
// react-router: https://github.com/rackt/react-router
import Router, {Route} from 'react-router'
// local imports
import {route_elements} from './routes';

// run the application with the appropriate routes based on the user
Router.run(route_elements, Handler => {
    React.render(<Handler />, document.body);
});

// end of file
