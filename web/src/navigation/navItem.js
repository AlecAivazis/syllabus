// the navigation item for the syllabus frontend

// react: https://github.com/facebook/react
import React from 'react'

'use strict'

class NavItem extends React.Component {
    render() {
        return (
            <div>
                {this.props.message}
            </div>
        )
    }
}

// export the class
module.exports = NavItem;

// end of file
