// the root component for the calendar view

// react: https://github.com/facebook/react
import React from 'react';
// local imports
import TabPanel from 'components/tabs/tabPanel/component';
import Tab from 'components/tabs/tab/component';


'use strict'

class CalendarRoot extends React.Component {
    render() {
        return (
            <TabPanel>
                <Tab>Hello</Tab>
                <Tab>Goodbye</Tab>
            </TabPanel>
        )
    }
}

// export the class
export default CalendarRoot;

// end of file
