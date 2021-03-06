// the main entry point for the syllabus frontend
 
'use strict'
 
// babel es6 polyfill: https://babeljs.io/docs/usage/polyfill/
import 'babel/polyfill';
// react: https://github.com/facebook/react
import React from 'react';
// react-router: https://github.com/rackt/react-router
import Router, {Route} from 'react-router';
 // local imports
import {route_elements} from './routes';
require('styles/default.styl')
 
// run the application with the appropriate routes based on the user
Router.run(route_elements, Router.HistoryLocation, Handler => {
    React.render(<Handler />, document.body);
});

// end of file
