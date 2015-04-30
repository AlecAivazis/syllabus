// the month calendar used by syllabus

// react: https://github.com/facebook/react
import React from 'react';
// momentjs: https://github.com/moment/momentjs.com
import moment from 'moment';
// local imports
import CalendarHeader from '../calendarHeader/component';
import {calendar_container_style} from '../monthCalendar/styles'

'use strict'

// the navigation bar component
class WeeklyCalendar extends React.Component {

    constructor(props){
        // instantiate this
        super(props);
        // set initial state
        this.state = {
            currentDate: moment(props.defaultDate)
        };
        // bind the various functions
        this.getElements = this.getElements.bind(this);
        this.getDayLabels = this.getDayLabels.bind(this);
        this.nextMonth = this.nextMonth.bind(this);
        this.previousMonth = this.previousMonth.bind(this);
    }


    render() {
        // the title of the calendar
        let title = this.state.currentDate.format('MMMM YYYY');
        // render the component
        return (
            <div style={calendar_container_style}>
                <CalendarHeader title={title} previous={this.previousMonth} 
                                              next={this.nextMonth} />
                <article>
                    {this.getElements()}
                </article>
            </div>
        )
    }


    nextMonth() {
        this.setState({
            currentDate: this.state.currentDate.add('1', 'month')
        });
    }


    previousMonth(){
        this.setState({
            currentDate: this.state.currentDate.subtract('1', 'month')
        });
    }


    getElements() {
        return <span>hello</span> 
    }


    getDayLabels(){
        let count = 0;
        return _.map(['sunday', 'monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday'], (day) => {
                return <th className="monthlyCalendarHeader" style={day_labels_style} key={count++}>{day}</th>
        });
    }

}



// prop types
WeeklyCalendar.propTypes = {
    defaultDate: React.PropTypes.string
};


// default props
WeeklyCalendar.defaultProps = {
    // the default is today
    defaultDate: moment().format()
};


// export the component
export default WeeklyCalendar;

// end of file
