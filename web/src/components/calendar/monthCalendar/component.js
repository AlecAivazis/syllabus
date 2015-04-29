// the month calendar used by syllabus

// react: https://github.com/facebook/react
import React from 'react';
// momentjs: https://github.com/moment/momentjs.com
import moment from 'moment';
// local imports
import MonthlyDay from '../monthlyDay/component';
import {calendar_style, calendar_container_style} from './styles';
require('./weekStyle.styl');

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
            <div style={calendar_container_style}>
                <table ref="calendar" style={calendar_style}>
                    {this.getElements()}
                </table>
            </div>
        )
    }


    getElements() {
        // keep the elements in a list
        let rows = [];
        // the start of the week that begins the desired month
        let start = this.state.currentDate.clone().startOf('month').startOf('week')
        // the end of the week that ends the desired month
        let end = this.state.currentDate.clone().endOf('month').endOf('week')
        // for each week in the range
        for (let week = start.clone(); week.isBefore(end) ; week.add(1, 'week')) {
            let days = [];
            for(let dayOfWeek = week.clone(); 
                    dayOfWeek.isBefore(week.clone().endOf('week')); 
                                               dayOfWeek.add(1,'days')){
                // the day is an off month if it isn't the same month as today
                let offMonth = dayOfWeek.format('M') != moment().format('M');
                // add a day element
                days.push(
                    <MonthlyDay day={dayOfWeek.format()} offMonth={offMonth}/>
                )
            }

            // return the week as a table row
            rows.push(<tr children={days} className="monthlyCalendarWeek" />);
        }
        // return the list of weeks
        return rows;
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
