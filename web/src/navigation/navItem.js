// the navigation item for the syllabus frontend

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
