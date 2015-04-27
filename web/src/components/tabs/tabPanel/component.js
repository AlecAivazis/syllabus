// the component used for navigation branding

// react: https://github.com/facebook/react
import React from 'react';

'use strict'

// the navbranding component
class TabPanel extends React.Component {

    render() {
        console.log(this.props.children);
        // return the image
        return (
            <div>
                {this.props.children}
            </div> 
        )
    }
}

// export the component
export default TabPanel;

// end of file