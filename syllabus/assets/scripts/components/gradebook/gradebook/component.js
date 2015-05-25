// the gradebook component used by the syllabus front end

// react: https://github.com/facebook/react
import React from 'react'
// react-bootstrap: 
import {OverlayTrigger, Popover} from 'react-bootstrap'
// local imports
import TabContainer from 'components/tabs/tabContainer/component'
import Tab from 'components/tabs/tab/component'
import GradingScaleControl from '../gradingScaleControl/component'
import {header_style,
        gradebook_container_style,
        gradebook_body_style,
        title_style,
        toolbar_style } from './styles'
require('styles/clearfix')

'use strict'

class Gradebook extends React.Component {

    render() {
        return (
            <div style={gradebook_container_style}>
                <div style={header_style}> 
                    <span style={title_style}>
                        {this.props.course.name}
                    </span>
                    <span style={toolbar_style}>
                        <OverlayTrigger trigger="click" placement="bottom" 
                            overlay={
                                <Popover>
                                    <GradingScaleControl course={this.props.course} />
                                </Popover>
                            }
                        >
                            <span> hello </span>
                        </OverlayTrigger>              
                    </span>
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


Gradebook.propTypes = {
    course: React.PropTypes.object.isRequired
}


// export the class
export default Gradebook

// end of file
