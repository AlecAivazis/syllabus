// a day for the syllabus monthly calendar

// react: https://github.com/facebook/react
import React from 'react'
// momentjs: https://github.com/moment/momentjs.com
import moment from 'moment'
// lodash: https://github.com/lodash/lodash
import _ from 'lodash';
// local imports
import {day_style, day_header_style} from './styles'
require('./dayStyle.styl')


'use strict'

// the navigation bar component
class CalendarDay extends React.Component {

    constructor(props) {
        // instantiate this
        super()
        // set initial state
        this.state = {
            day: moment(props.day),
        }
    }

    render() {
        // the style for the day element (not sure why a list isn't working)
        let style = _.merge(day_style, this.props.style)
        // the title of the day
        let title =  this.props.show_title && (
            <div style={day_header_style}>
                {this.state.day.format('ddd Do').replace(' ', String.fromCharCode(160))}
            </div>
        )
        // render the day
        return (
            <div style={style} className="syllabusCalendarDay">
                {title}
            </div>
        )
    }
}


// prop types
CalendarDay.propTypes = {
    day: React.PropTypes.string,
    style: React.PropTypes.object
};


// export the component
export default CalendarDay

// end of file
