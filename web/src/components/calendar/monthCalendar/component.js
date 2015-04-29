// the month calendar used by syllabus

// react: https://github.com/facebook/react
import React from 'react';
// momentjs: https://github.com/moment/momentjs.com
import moment from 'moment';
// local imports
import MonthlyDay from '../monthlyDay/component'

'use strict'

// the navigation bar component
class MonthCalendar extends React.Component {

    constructor(props){
        // instantiate this
        super(props);
        // set initial state
        this.state = {
            currentDate: moment(props.defaultDate)
        };
        // bind the various functions
        this.getElements = this.getElements.bind(this);
    }

    render() {
        console.log(this.refs.calendar);
        return (
            <div ref="calendar">
                {this.getElements()}
            </div>
        )
    }

    getElements() {
        // keep the elements in a list
        let elements = [];
        // the start of the week that begins the desired month
        let start = this.state.currentDate.clone().startOf('month').startOf('week')
        // the end of the week that ends the desired month
        let end = this.state.currentDate.clone().endOf('month').endOf('week')
        // for each day in the range
        for (let day = start.clone(); day.isBefore(end) ; day.add(1, 'days')) {
            // add a day element
            elements.push(
                <MonthlyDay day={day}/>
            )
        }
        // return the list of days
        return elements;
    }

}



// prop types
MonthCalendar.propTypes = {
    defaultDate: React.PropTypes.string
};


// default props
MonthCalendar.defaultProps = {
    // the default is today
    defaultDate: moment().format()
};


// export the component
export default MonthCalendar;

// end of file
