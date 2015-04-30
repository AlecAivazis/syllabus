// the header for the calendar used by syllabus

// react: https://github.com/facebook/react
import React from 'react';
// local imports
import {header_style} from './styles';
import Icon from 'src/components/misc/icon';

'use strict'

// the navigation bar component
class CalendarHeader extends React.Component {

    render() {
        // render the icon
        return (
            <div style={header_style}>
                <Icon name="arrow-left" color="#bebc9f" onClick={this.props.previous}/>
                <span style={{padding: '0px 20px'}}> {this.props.title} </span>
                <Icon name="arrow-right" color="#bebc9f" onClick={this.props.next}/>
            </div>
        )
    }
}

// prop types
CalendarHeader.propTypes = {
    title: React.PropTypes.string,
};

// export the component
export default CalendarHeader

// end of file
