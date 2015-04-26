// the navigation item for the syllabus frontend

// react: https://github.com/facebook/react
import React from 'react'
// react-style-normalizer: https://github.com/radubrehar/react-style-normalizer
import normalize from 'react-style-normalizer';
// react-router: https://github.com/rackt/react-router/blob/master/docs/api/components/Link.md
import {Link} from 'react-router'
// local imports
import stylesheet from './style'

'use strict'

// the actual component
class NavItem extends React.Component {
    render() {
        // normalize the stylesheet
        let style = normalize(stylesheet);
        return (
            <Link to={this.props.name}>
                <li style={style}>
                    {this.props.name}
                </li>
            </Link>
        )
    }
}

// export the class
export default NavItem;

// end of file
