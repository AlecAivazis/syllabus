// the main entry point for the syllabus front end

'use strict'

// react: https://github.com/facebook/react
import React from 'react';
// react-router: https://github.com/facebook/react
import Router, {Route} from 'react-router'
// local imports
import {nav_routes} from './routes';
import SyllabusRoot from './app'

// lodash: https://github.com/lodash/lodash
import _ from 'lodash'

// the application routes 
// done here to avoid circular dependence... I thought es6 took care of this?
let route_elements = (
    <Route handler={SyllabusRoot} path="/">
        { _.map( nav_routes, function(item) {
            return <Route name={item.name} path={item.path} handler={item.handler} />
        })}
    </Route>
)

// run the application with the appropriate routes based on the user
Router.run(route_elements, Handler => {
    React.render(<Handler />, document.body);
});
