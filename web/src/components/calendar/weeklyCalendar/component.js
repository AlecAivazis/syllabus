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
class WeeklyCalendar extends React.Component {

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
        this.nextWeek = this.nextWeek.bind(this)
        this.peviousWeek = this.peviousWeek.bind(this)
    }


    render() {
        // the title of the calendar
        let title = this.state.currentDate.format('MMMM YYYY');
        // render the component
        return (
            <CalendarContainer title={this.getTitle()} previous={this.peviousWeek} next={this.nextWeek} >
                <article>
                    {this.getTimeline()}
                    {this.getElements()}
                </article>
            </CalendarContainer>
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


    getTimeline() {
        return <div style={timeline_style}>&nbsp;</div>
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
        for(let day = start.clone() ; day.isBefore(end) ; day.add(1,'days')){
            // add the appropriate component for the day
            elements.push(
                <CalendarDay day={day.format()} key={day.format()} style={day_style} show_title={true}/>
            )
        }

        return elements
    }


    // return the title for the calendar
    getTitle(){
        // the start of the week to show
        let start = this.state.currentDate.clone().startOf('week')
        // the end of the week to show
        let end = this.state.currentDate.clone().endOf('week')
        let start_title, end_title
        // if the start and end are not in the same year
        if (start.format('YYYY') != end.format('YYYY')){
            // show full dates on both side
            start_title = start.format('MMM D')
            end_title = end.format('MMM D, YYYY')
        // otherwise the start and end time have the same year
        // if the months are not the same
        } else if (start.format('M') != end.format('M')) {
            start_title = start.format('MMM D')
            end_title = end.format('MMM D YYYY')
        // otherwise the start and end time are in the same month and year
        } else {
            start_title = start.format('D')
            end_title = end.format('D MMMM YYYY')
        }

        // return the title
        return `${start_title} ${String.fromCharCode(8212)} ${end_title}`

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
