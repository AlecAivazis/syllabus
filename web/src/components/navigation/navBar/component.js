// the navigation bar used by syllabus

// react: https://github.com/facebook/react
import React from 'react';
// lodash: https://github.com/lodash/lodash
import _ from 'lodash';
// react-style-normalizer: https://github.com/radubrehar/react-style-normalizer
import normalize from 'react-style-normalizer';
// local imports
import NavItem from '../navItem/component';
import nav_routes from '../../../routes';
import stylesheet from './style';

'use strict'

// the navigation bar component
class NavBar extends React.Component {

    render() {
        // normalize the stylesheet
        let style = normalize(stylesheet);

        return (
            <div style={style}>
                { _.map( nav_routes, function(item) {
                    if(item.show_in_nav){
                        return <NavItem message={item.name} key={item.name}/>
                    }
                    
                })}
            </div>
        )
    }
}

// export the component
export default NavBar;

// end of file
