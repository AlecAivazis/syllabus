// the navigation bar used by syllabus

// react: https://github.com/facebook/react
import React from 'react';

'use strict'

// the navigation bar component
class Icon extends React.Component {

    render() {
        // figure out the appropriate icon

        // the base icon name
        let icon = 'icon';
        
        // start with the basic icon based on the required name
        let iconName = `${icon} ${icon}-${this.props.name}`;

        // if the user wants a different size
        if (this.props.size){
            iconName += ` ${icon}-${this.props.size}`;
        }

        // render the icon
        return (
            <i className={iconName}>
            </i>
        )
    }
}

// export the component
export default Icon;

// end of file
