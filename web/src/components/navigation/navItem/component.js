// the navigation item for the syllabus frontend

// react: https://github.com/facebook/react
import React from 'react';
// react-style-normalizer: https://github.com/radubrehar/react-style-normalizer
import normalize from 'react-style-normalizer';
// react-router: https://github.com/rackt/react-router/blob/master/docs/api/components/Link.md
import {Link} from 'react-router';
// local imports
import Icon from 'src/components/misc/icon';
// make sure the necessary stylesheets are loaded
require('styles/noise.css');
require('./navItem.styl');

'use strict'

// the actual component
class NavItem extends React.Component {
    render() {
        // normalize the stylesheet
        let style = normalize(stylesheet);
        return (
            <Link to={this.props.route} className="navItem">
                <li style={style}>
                    <Icon name={this.props.icon} size={"2x"} />
                    <br/>
                    {this.props.name}
                </li>
            </Link>
        )
    }
}

//// styles ////

// the component stylesheet
let stylesheet = {
    "display": "inline-block",
    "margin": "15% 10px 0px 10px",
    "textAlign": "center",
    "fontSize": "12px",
    "lineHeight": "28px",
    "textTransform": "capitalize",
    "textShadow": "1px 1px 1px #000000",
}

// export the class
export default NavItem;

// end of file
