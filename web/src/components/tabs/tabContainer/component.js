// the component used for navigation branding

// react: https://github.com/facebook/react
import React from 'react';

'use strict'

// the navbranding component
class TabContainer extends React.Component {

    constructor(){
        // instantiate this
        super();
        // bind various functions to the class instance
        this.getMenuItems = this.getMenuItems.bind(this);
    }

    render() {

        let menuItems = this.getMenuItems();
        return (
            <div>
                {menuItems}
            </div> 
        )
    }

    // return the menu 
    getMenuItems(){
        // if the user did not specify any children
        if (!this.props.children){
            console.log('is actually throwing error');
            // throw an error
            throw new Error('TabContainer must contain at least one Tab');
        }
        // 
    }
}

// export the component
export default TabContainer;

// end of file