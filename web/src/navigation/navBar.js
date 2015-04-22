// the navigation bar used by syllabus

// imports
import NavItem from './navItem'
import _ from 'lodash'

'use strict'

// the current user's role (for now)
let roles = ['teacher'];

// the navigation bar component
class NavBar extends React.Component {

    constructor(){
        // create this
        super();
        // bind the various functions
        this.get_nav_routes = this.get_nav_routes.bind(this);
    }

    // return the posible navigation items for the current user
    get_nav_routes(){

        // the potential routes for each role
        let all_routes = [
            {
                name: 'hello',
                test: 'hello',
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


    render() {
        // get the current user's role

        return (
            <div>
                { _.map( this.get_nav_routes(), function(item) {
                    return <NavItem message={item.test} key={item.name}/>
                })}
            </div>
        )
    }
}

// export the class
module.exports = NavBar;

// end of file
