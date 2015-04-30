// the month calendar used by syllabus

// react: https://github.com/facebook/react
import React from 'react'
// momentjs: https://github.com/moment/momentjs.com
import moment from 'moment'
// local imports
import CalendarHeader from '../calendarHeader/component'
import CalendarDay from '../calendarDay/component'
import {calendar_container_style} from '../monthCalendar/styles'

'use strict'

// the navigation bar component
class WeeklyCalendar extends React.Component {

    constructor(props){
        // instantiate this
        super(props)
        // set initial state
        this.state = {
            currentDate: moment(props.defaultDate)
        }
        // bind the various functions
        this.getElements = this.getElements.bind(this)
        this.getDayLabels = this.getDayLabels.bind(this)
        this.nextWeek = this.nextWeek.bind(this)
        this.peviousWeek = this.peviousWeek.bind(this)
    }


    render() {
        // the title of the calendar
        let title = this.state.currentDate.format('MMMM YYYY');
        // render the component
        return (
            <div style={calendar_container_style}>
                <CalendarHeader title={title} previous={this.peviousWeek} 
                                              next={this.nextWeek} />
                <article>
                    {this.getElements()}
                </article>
            </div>
        )
    }

    // focus the calendar on the next week
    nextWeek() {
        this.setState({
            currentDate: this.state.currentDate.add('1', 'week')
        })
    }

    // focus the calendar on the previous week
    peviousWeek(){
        this.setState({
            currentDate: this.state.currentDate.subtract('1', 'week')
        })
    }

    // get the element that make up the calendar
    getElements() {
        // the start of the week to show
        let start = this.state.currentDate.clone().startOf('week');
        // the end of the week to show
        let end = this.state.currentDate.clone().endOf('week');
        // keep the elements in a list
        let elements = []
        // for every day in between the start and end of the week
        for(let day = week.clone() ; day.isBefore(end) ; day.add(1,'days')){
            // add the appropriate component for the day
            element.push(

            )
        }

        return <span>hello</span> 
    }


    getDayLabels(){
        let count = 0;
        return _.map(['sunday', 'monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday'], (day) => {
                return <span className="weeklyCalendarHeader" key={count++}>{day}</span>
        })
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
