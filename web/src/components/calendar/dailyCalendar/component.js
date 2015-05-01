// the month calendar used by syllabus

// react: https://github.com/facebook/react
import React from 'react'
// momentjs: https://github.com/moment/momentjs.com
import moment from 'moment'
// local imports
import CalendarContainer from '../calendarContainer/component'
import CalendarDay from '../calendarDay/component'
import {day_style, timeline_style} from './styles'

'use strict'

// the navigation bar component
class DailyCalendar extends React.Component {

    constructor(props){
        // instantiate this
        super(props )
        // set initial state
        this.state = {
            currentDate: moment(props.defaultDate)
        }
        // bind the various functions
        this.getElements = this.getElements.bind(this)
        this.getTimeline = this.getTimeline.bind(this)
        this.getTitle = this.getTitle.bind(this)
        this.nextDay = this.nextDay.bind(this)
        this.previousDay = this.previousDay.bind(this)
    }


    render() {
        // the title of the calendar
        let title = this.state.currentDate.format('MMMM YYYY');
        // render the component
        return (
            <CalendarContainer title={this.getTitle()} previous={this.previousDay} next={this.nextDay} >
                <article>
                    {this.getTimeline()}
                    {this.getElements()}
                </article>
            </CalendarContainer>
        )
    }


    // focus the calendar on the next day
    nextDay() {
        this.setState({
            currentDate: this.state.currentDate.add('1', 'day')
        })
    }


    // focus the calendar on the previous day
    previousDay(){
        this.setState({
            currentDate: this.state.currentDate.subtract('1', 'day')
        })
    }


    getTimeline() {
        return <div style={timeline_style}>&nbsp;</div>
    }


    // get the element that make up the calendar
    getElements() {
        let day = this.state.currentDate
        // the start of the week to show
        return <CalendarDay day={day.format()} key={day.format()} style={day_style} show_title={false}/>
    }


    // get the title of calendar
    getTitle(){
        return this.state.currentDate.format('dddd MMMM D, YYYY')
    }

}


// prop types
DailyCalendar.propTypes = {
    defaultDate: React.PropTypes.string
};


// default props
DailyCalendar.defaultProps = {
    // the default is today
    defaultDate: moment().format()
};


// export the component
export default DailyCalendar;

// end of file
