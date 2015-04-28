// the component used for navigation branding

// react: https://github.com/facebook/react
import React from 'react';
// lodash: https://github.com/lodash/lodash
import _ from 'lodash';
// local imports
import {list_container_style, 
        menu_toolbar_style, 
        header_style,
        container_style,
        tab_style,
        menu_element_style,
        menu_element_active_style, 
        menu_element_text_style,
        menu_element_left_edge_style,
        menu_element_left_edge_active_style,
        menu_element_right_edge_style,
        menu_element_right_edge_active_style,
        menu_element_center_style,
        menu_element_center_active_style } from './styles';

require('styles/clearfix.styl');
    

'use strict'

// the navbranding component
class TabContainer extends React.Component {

    constructor(props){
        // instantiate this
        super(props);
        // bind various functions to the class instance
        this.getMenu = this.getMenu.bind(this);
        this.getSelectedTab = this.getSelectedTab.bind(this);
        this.selectTab = this.selectTab.bind(this);
        // set initial state
        this.state = {
            selectedTab: props.defaultTab
        };
    }


    render() {
        return (
            <div style={container_style}>
                {this.getMenu()}
                {this.getSelectedTab()}
            </div> 
        )
    }


    // called immediately before the initial rendering occurs
    componentWillMount(){
        // if the user did not specify any children
        if (!this.props.children){
            // throw an error
            throw new Error('TabContainer must contain at least one Tab');
        }
    }


    // return the menu that toggles the selected panel  
    getMenu(){

        // create list elements for each tab child
        let index = 0;
        let list_elements = _.map(this.props.children, (tab) => {
            // increment the counter and use that as the element key
            let element_key = ++index;
            // define variables for the styles
            let left_edge_style, center_style, right_edge_style, element_style;

            // highlight the appropriate tab
            if(index == this.state.selectedTab){
                // this is the active tab so give it the active styles
                element_style = menu_element_active_style;
                left_edge_style = menu_element_left_edge_active_style;
                right_edge_style = menu_element_right_edge_active_style;
                center_style = menu_element_center_active_style;
            // otherwise this is not the current tab
            } else {
                // so give it the inactive styles
                element_style = menu_element_style;
                left_edge_style = menu_element_left_edge_style;
                right_edge_style = menu_element_right_edge_style;
                center_style = menu_element_center_style;
            }

            // make sure each tab can select a panel
            return (
                <li onClick={this.selectTab.bind(this, element_key)} key={element_key} style={element_style}> 
                    <span style={left_edge_style}>&nbsp;</span>
                    <span style={center_style}>
                        {tab.props.title}
                    </span>
                    <span style={right_edge_style}>&nbsp;</span>
                </li>
            )
        });

        // return the navigation element
        return (
            <div style={header_style}  className="clearfix">
                <ul ref="menu" style={list_container_style}>
                    {list_elements}
                </ul>
                <span style={menu_toolbar_style}>
                    {this.props.header}
                </span>
            </div>
        )
    }


    // return the selected panel
    getSelectedTab(){
        // figure out the selected tab
        let index = this.state.selectedTab-1;
        // return the appropriate tab
        return this.props.children[index]
    }


    // select the tab specified by the index
    selectTab(index){
        // set the state variable
        this.setState({
            selectedTab: index
        });
    }
}


// prop types
TabContainer.propTypes = {
    defaultTab: React.PropTypes.number
};


// default props
TabContainer.defaultProps = {
    defaultTab: 1
};


// export the component
export default TabContainer;

// end of file
