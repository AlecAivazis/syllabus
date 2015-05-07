// the gradebook component used by the syllabus front end

// react: https://github.com/facebook/react
import React from 'react'
// local imports
import TabContainer from 'components/tabs/tabContainer/component'
import Tab from 'components/tabs/tab/component'
import {header_style,
        gradebook_container_style,
        gradebook_body_style } from './styles'


'use strict'

class Gradebook extends React.Component {

    render() {

        return (

            <div style={gradebook_container_style}>
                <div style={header_style}> 
                    Class 
                </div>
                <div style={gradebook_body_style}>
                    <TabContainer>
                        <Tab title="Grades">
                            hello1
                        </Tab>
                        <Tab title="Histogram">
                            hello2
                        </Tab>
                        <Tab title="Performance">
                            hello3
                        </Tab>
                    </TabContainer>
                </div>
            </div>
        )
    }
}


// export the class
export default Gradebook

// end of file
