// the root component for the calendar view

// react: https://github.com/facebook/react
import React from 'react'
// local imports
import TabContainer from 'components/tabs/tabContainer/component'
import Tab from 'components/tabs/tab/component'
import MonthCalendar from 'components/calendar/monthCalendar/component'
import WeeklyCalendar from 'components/calendar/weeklyCalendar/component'
import DailyCalendar from 'components/calendar/dailyCalendar/component'

'use strict'

class CalendarRoot extends React.Component {
    render() {
        return (
            <TabContainer>
                <Tab title="Month">
                    <MonthCalendar />
                </Tab>
                <Tab title="Week">
                    <WeeklyCalendar />
                </Tab>
                <Tab title="Day">
                    <DailyCalendar />
                </Tab>
            </TabContainer>
        )
    }
}

// export the class
export default CalendarRoot

// end of file
