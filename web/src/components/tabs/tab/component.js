// the component used for navigation branding

// react: https://github.com/facebook/react
import React from 'react';
// local imports
import {tab_style} from './styles';
require('styles/clearfix.styl');

'use strict'

// the navbranding component
class Tab extends React.Component {

    render() {
        // return the image
        return (
            <div style={tab_style} className="clearfix">
                {this.props.children}
            </div> 
        )
    }
}

// export the component
export default Tab;

// end of file