// the component used for navigation branding

// react: https://github.com/facebook/react
import React from 'react';

'use strict'

// the navbranding component
class Tab extends React.Component {

    render() {
        // return the image
        return (
            <div>
                {this.props.children}
            </div> 
        )
    }
}

// export the component
export default Tab;

// end of file