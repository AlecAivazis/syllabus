// a container for sidebar elements which link to subsequent views

// react: https://github.com/facebook/react
import React from 'react'
// lodash: https://github.com/lodash/lodash
import _ from 'lodash';
// react-style-normalizer: https://github.com/radubrehar/react-style-normalizer
import normalize from 'react-style-normalizer';
// local imports
import {tier1_style, tier2_style} from './styles'
require('styles/noise.css')

'use strict'

class SidebarContainer extends React.Component {

    constructor() {
        // instantiate this
        super()
    }

    render() {
        // figure out the style to apply to the container
        let style = this.props.tier == 1 ? tier1_style : tier2_style
        // keep track of the number of children
        let count = 0
        let tier = this.props.tier
        // render the component
        return (
            <div>
                <ul style={normalize(style)} className="noise-005">
                    {_.map(this.props.menuElements, function(element){
                        return React.cloneElement(element, {
                            key: count++,
                            tier: tier
                        })   
                    })}
                </ul>
                <div>
                    {this.props.children}
                </div>
            </div>
        )
    }
}


// prop types
SidebarContainer.propTypes = {
    menuElements: React.PropTypes.array,
    tier: React.PropTypes.number
}


// default properties
SidebarContainer.defaultProps = {
    menuElements: [],
    tier: 2
}


// export the class
export default SidebarContainer

// end of file
