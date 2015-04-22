// the navigation item for the syllabus frontend

'use strict'

class NavItem extends React.Component {
    render() {
        return (
            <div>
                {this.props.message}
            </div>
        )
    }
}

// export the class
module.exports = NavItem;

// end of file
