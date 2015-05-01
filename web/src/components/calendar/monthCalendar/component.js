// the month calendar used by syllabus

// react: https://github.com/facebook/react
import React from 'react'
// momentjs: https://github.com/moment/momentjs.com
import moment from 'moment'
// local imports
import MonthlyDay from '../monthlyDay/component'
import CalendarHeader from '../calendarHeader/component'
import {calendar_style, 
        calendar_container_style, 
        day_labels_style} from './styles'
require('./weekStyle.styl')

'use strict'

// the navigation bar component
class MonthCalendar extends React.Component {

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
        this.nextMonth = this.nextMonth.bind(this)
        this.previousMonth = this.previousMonth.bind(this)
    }


    render() {
        // the title of the calendar
        let title = this.state.currentDate.format('MMMM YYYY')
        // render the component
        return (
            <div style={calendar_container_style}>
                <div style={{height:'100%', position: 'relative'}}>
                    <CalendarHeader title={title} previous={this.previousMonth} 
                                                  next={this.nextMonth} />
                    <div style={{position: 'absolute', top: '55px', bottom: '0', height: 'auto', right: '0', left: '0'}}>
                        <table ref="calendar" style={calendar_style}>
                            <thead>
                                {this.getDayLabels()}
                            </thead>
                            <tbody>
                                {this.getElements()}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        )
    }

    // make the calendar show the next month
    nextMonth() {
        this.setState({
            currentDate: this.state.currentDate.add('1', 'month')
        })
    }

    // make the calendar show the previous month
    previousMonth(){
        this.setState({
            currentDate: this.state.currentDate.subtract('1', 'month')
        })
    }

    // get the elements that make up the calendar
    getElements() {
        // keep the elements in a list
        let rows = []
        // the start of the week that begins the desired month
        let start = this.state.currentDate.clone().startOf('month').startOf('week')
        // the end of the week that ends the desired month
        let end = this.state.currentDate.clone().endOf('month').endOf('week')
        // for each week in the range
        for (let week = start.clone(); week.isBefore(end) ; week.add(1, 'week')) {
            // save the days that we need to add to the week element
            let days = []
            // for each day for the week
            for(let dayOfWeek = week.clone() ;
                    dayOfWeek.isBefore(week.clone().endOf('week')) ;
                                               dayOfWeek.add(1,'days')){
                // the day is an off month if it isn't the same month as today
                let offMonth = dayOfWeek.format('M') != this.state.currentDate.format('M')
                // add a day element
                days.push(
                    <MonthlyDay day={dayOfWeek.format()} offMonth={offMonth} key={dayOfWeek.format()}/>
                )
            }

            // return the week as a table row
            rows.push(<tr children={days} className="monthlyCalendarWeek" key={week.format('W')}/>)
        }
        // return the list of weeks
        return rows
    }


    getDayLabels(){
        let count = 0
        return _.map(['sunday', 'monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday'], (day) => {
                return <th className="monthlyCalendarHeader" style={day_labels_style} key={count++}>{day}</th>
        })
    }

}



// prop types
MonthCalendar.propTypes = {
    defaultDate: React.PropTypes.string
}


// default props
MonthCalendar.defaultProps = {
    // the default is today
    defaultDate: moment().format()
}


// export the component
export default MonthCalendar

// end of file
