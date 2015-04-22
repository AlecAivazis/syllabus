// the navigation bar used by syllabus

// imports
import NavItem from './navItem'
import _ from 'lodash'

'use strict'

// the current user's role (for now)
let roles = ['admin'];

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

        // define the possible routes 
        let all_routes = new Map([
            ['registrar', [
                {
                    name: 'hello',
                    test: 'hello',
                }

            ]],
            ['teacher', [
                {
                    name: 'hello',
                    test: 'hello',
                }

            ]],
            ['student', [
                {
                    name: 'hello',
                    test: 'hello',
                }
            
            ]]
        ]);

        for (var [key, value] of all_routes.entries()){
            console.log(key);
        }

        // the routes the user can visit
        let routes = [];
        // for each role of the user        
        _.each(roles, role => {
            // add the routes for this role to the list
            routes = _.union(routes, all_routes.get(role));
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
