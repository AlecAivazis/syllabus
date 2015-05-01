// a component responsible for wrapping children around a container used 
// in the container view by syllabus

// react: https://github.com/facebook/react
import React from 'react'
// local imports
import Icon from 'components/misc/icon'
import {calendar_container_style, header_style} from './styles'

'use strict'

// the navigation bar component
class CalendarContainer extends React.Component {
    render() {
        // render the icon
        return (
            <div style={calendar_container_style}>
                <div style={{height:'100%', position: 'relative'}}>
                    <div style={header_style}>
                        <Icon name="arrow-left" color="#bebc9f" onClick={this.props.previous}/>
                        <span style={{padding: '0px 20px'}}> {this.props.title} </span>
                        <Icon name="arrow-right" color="#bebc9f" onClick={this.props.next}/>
                    </div>
                    <div style={{position: 'absolute', top: '55px', bottom: '0', height: 'auto', right: '0', left: '0'}}>
                        {this.props.children}
                    </div>
                </div>
            </div>
        )
    }
}

// export the component
export default CalendarContainer

// end of file
