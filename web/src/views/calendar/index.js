// the root component for the calendar view

// react: https://github.com/facebook/react
import React from 'react';
// local imports
import TabContainer from 'components/tabs/TabContainer/component';
import Tab from 'components/tabs/tab/component';


'use strict'

class CalendarRoot extends React.Component {
    render() {
        return (
            <TabContainer>
                <Tab title="hello">
                    Hello
                </Tab>
                <Tab title="goodbye">
                    Goodbye
                </Tab>
            </TabContainer>
        )
    }
}

// export the class
export default CalendarRoot;

// end of file
