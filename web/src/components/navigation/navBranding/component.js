// the component used for navigation branding

// react: https://github.com/facebook/react
import React from 'react';

'use strict'

import image from 'images/branding.png';

// the navbranding component
class NavBranding extends React.Component {

    render() {
        // return the image
        return <img src={image} style={{float: 'left'}}/>
    }
}

// export the component
export default NavBranding;

// end of file
