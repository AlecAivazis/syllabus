// launch the application

'use strict';

// react: https://github.com/facebook/react
import React from 'react'
// lodash: https://github.com/lodash/lodash
import _ from 'lodash'
// local imports
import CalendarRoot from './calendar/index'

// the current user's role (for now)
let roles = ['admin'];

// the potential routes for each role (actual routes are defined in index.js)
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

// return the posible navigation items for the current user
let get_routes_for_user = function(){

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


module.exports = {
    nav_routes: get_routes_for_user()
}


// end of file
