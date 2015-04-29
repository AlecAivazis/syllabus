// a day for the syllabus monthly calendar

// react: https://github.com/facebook/react
import React from 'react';
// momentjs: https://github.com/moment/momentjs.com
import moment from 'moment';
// eq.js: https://github.com/snugug/eq.js
require('./monthlyDay.styl');
// local imports
import {day_style, day_off_month_style} from './styles';

'use strict'

// the navigation bar component
class MonthlyDay extends React.Component {

    constructor(props) {
        // instantiate this
        super();
        // set initial state
        this.state = {
            day: moment(props.day),
            offMonth: props.offMonth ? props.offMonth : true
        };
    }

    render() {
        let style;
        // figure out if the day is an off month and apply the right style
        if (this.props.offMonth){
            style = day_off_month_style;
        } else {
            style = day_style;
        }
        // render the icon
        return (
            /* use eq.js for element queries */
            <td style={style} className="monthlyDay">
                {this.state.day.format('D')}
            </td>
        )
    }
}


// prop types
MonthlyDay.propTypes = {
    day: React.PropTypes.string,
    offMonth: React.PropTypes.bool
};


// export the component
export default MonthlyDay;

// end of file
