// a container for sidebar elements which link to subsequent views

// react: https://github.com/facebook/react
import React from 'react'
// react-style-normalizer: https://github.com/radubrehar/react-style-normalizer
import normalize from 'react-style-normalizer';
// local imports
import {tier1_style, tier2_style} from './styles'

'use strict'

class SidebarElement extends React.Component {
    render() {
        // figure out the right style to apply to the element
        let style = this.props.tier == 1 ? tier1_style  : tier2_style
        // render the component
        return (
            <li style={normalize(style)}>
                {this.props.children}
            </li>
        )
    }
}


// prop types
SidebarElement.propTypes = {
    tier: React.PropTypes.number
}


// default properties
SidebarElement.defaultProps = {
    tier: 2
}


// export the class
export default SidebarElement

// end of file
