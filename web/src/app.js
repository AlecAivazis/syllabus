// launch the application

'use strict';

import React from 'react'
// local imports
import NavBar from './navigation/navBar'
import NavItem from './navigation/navItem'
import CalendarRoot from './calendar/index'
// lodash: https://github.com/lodash/lodash
import _ from 'lodash'
// react-router: https://github.com/rackt/react-router
import Router from 'react-router'
let {RouteHandler, Link, Route} = Router;

// the current user's role (for now)
let roles = ['admin'];

// the base application component for syllabus
class SyllabusRoot extends React.Component{

    // render the application
    render() {
        return (
            <div>
                <NavBar>
                    { _.map( get_nav_routes(), function(item) {
                        return <NavItem message={item.name} key={item.name}/>
                    })}
                </NavBar>

                <RouteHandler/>
            </div>
        )

    }
}

SyllabusRoot.contextTypes = {
  router: React.PropTypes.func,
};

// return the posible navigation items for the current user
let get_nav_routes = function(){

    // the potential routes for each role
    let all_routes = [
        {
            name: 'hello',
            path: 'hello',
            handler: CalendarRoot,
            roles: ['teacher', 'student']
        }, 
        {
            name: 'goodbye',
            test: 'goodbye',
            roles: ['student']
        }
    ];

    // figure out the routes for the user
    let routes = [];
    // for each potential route
    _.each(all_routes, route => {
        // if the user satisfies the role requirement
        if (_.intersection(route.roles, roles).length || _.contains(roles, 'admin') ){
            // add the route to the list
            routes.push(route);
        }
    });

    // return the list of routes
    return routes;
}

// the application routes
let routes = (
    <Route handler={SyllabusRoot} path="/">
        { _.map( get_nav_routes(), function(item) {
            return <Route name={item.name} path={item.path} handler={item.handler} />
        })}
    </Route>
)

// run the application with the specified routes
Router.run(routes, Handler => {
    React.render(<Handler />, document.body);
});

// end of file
