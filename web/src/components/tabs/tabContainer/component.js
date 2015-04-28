// the component used for navigation branding

// react: https://github.com/facebook/react
import React from 'react';
// lodash: https://github.com/lodash/lodash
import _ from 'lodash';
// local imports
import {menuElementStyle, 
        listContainerStyle, 
        menuToolbarStyle, 
        headerStyle,
        containerStyle} from './styles';

require('styles/clearfix.styl');
require('styles/tabs.css');
    

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
            <div style={containerStyle}>
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
            let element_key = ++index;
            // make sure each tab can select a panel
            return (
                <li onClick={this.selectTab.bind(this, element_key)} key={element_key} style={menuElementStyle}> 
                    <a>
                        {tab.props.title} 
                    </a>
                </li>
            )
        });
        // return the navigation element
        return (
            <div style={headerStyle}  className="clearfix">
                <ul ref="menu" style={listContainerStyle} className="tabs group">
                    {list_elements}
                </ul>
                <span style={menuToolbarStyle}>
                    {this.props.header}
                </span>
            </div>
        )
    }


    // return the selected panel
    getSelectedTab(){
        // figure out the selected tab
        let index = this.state.selectedTab-1;
        // render the selected tab in a semantic container
        return (
            <article ref='container'>
                {this.props.children[index]}
            </article> 
        )
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
