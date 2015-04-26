// the navigation bar used by syllabus

// react: https://github.com/facebook/react
import React from 'react';
// lodash: https://github.com/lodash/lodash
import _ from 'lodash';
// react-style-normalizer: https://github.com/radubrehar/react-style-normalizer
import normalize from 'react-style-normalizer';
// local imports
import NavItem from '../navItem/component';
import NavBranding from '../navBranding/component';
import nav_routes from 'src/routes';
import stylesheet from './style';

// make sure the noise stylesheet is loaded
require('styles/noise.css');

'use strict'

// the navigation bar component
class NavBar extends React.Component {

    render() {
        // normalize the stylesheet
        let style = normalize(stylesheet);

        return (
            <nav style={style} className="noise-005">
                <NavBranding />
                <ul style={list_style}>
                    { _.map( nav_routes, function(item) {
                        if(item.show_in_nav){
                            return <NavItem name={item.name} route={item.route} 
                                            key={item.name} icon={item.icon}/>
                        }
                        
                    })}
                </ul>
            </nav>
        )
    }
}

// remove unncessary styling on lists
let list_style = {
    padding: "0px",
    margin: "0px",
    display: "inline-block",
    height: '100%',
    marginLeft: '20px',
}

// export the component
export default NavBar;

// end of file
