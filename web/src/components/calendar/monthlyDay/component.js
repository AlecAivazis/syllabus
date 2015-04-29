// a day for the syllabus monthly calendar

// react: https://github.com/facebook/react
import React from 'react';
// eq.js: https://github.com/snugug/eq.js
require('eq.js');
// local imports
import {day_style} from './styles';

'use strict'

// the navigation bar component
class MonthlyDay extends React.Component {

    render() {
        // render the icon
        return (
            /* use eq.js for element queries */
            <div style={day_style}>
                {this.props.day}
            </div>
        )
    }
}

// export the component
export default MonthlyDay;

// end of file
