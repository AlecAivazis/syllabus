// the navigation bar used by syllabus

'use strict'

class NavBar extends React.Component {

    render() {
        // get the current user's role

        return (
            <div>
                {this.props.children}
            </div>
        )
    }
}

// export the class
module.exports = NavBar;

// end of file
