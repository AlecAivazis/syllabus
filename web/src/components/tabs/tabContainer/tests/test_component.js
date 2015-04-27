// test various functionalities of the TabContainer component 
// uses mocha and chai

// react
import React from 'react';
// facebook test utils
import TestUtils from 'react/lib/ReactTestUtils';
// local imports
import TabContainer from '../component';
import Tab from '../../tab/component';

describe("TabPanel", () => {

    // define the common component needed for the test suite
    let panel_component = (
        <TabContainer>
            <Tab title="tab1">tab1</Tab>
            <Tab title="tab2">tab2</Tab>
        </TabContainer>
    )

   
    // return a boolean depending on wether the indicated tab is active
    function isTabActive(container, tabNumber){
        // get the tab that is actually rendered by the container
        let rendered_tab = TestUtils.findRenderedDOMComponentWithTag(container, 'article');
        let rendered_content = rendered_tab.getDOMNode().children[0].innerHTML;
        // get the tab that we are checking against
        let requested_tab = container.props.children[tabNumber-1];
        let requested_content = requested_tab.props.children;
        // check that the rendered content is equal to that of the requested tab
        return requested_content === rendered_content
    }


    // after each test
    afterEach(function(done) {
        // remove any react components that are mounted at the body
        React.unmountComponentAtNode(document.body);
        // double check
        document.body.innerHTML = "" ;
        // we're finished
        setTimeout(done);
    });


    it('renders to the DOM', function() {
        // render the component to the DOM
        let rendered_component = TestUtils.renderIntoDocument(panel_component);
        // check that it worked
        expect(rendered_component).to.exist;
    });


    it('barfs if no tabs are given', function(){
        // check that the component throws if rendered without tabs
        expect(function(){TestUtils.renderIntoDocument(<TabContainer/>)})
            .to.throw(Error);
    });


    it('shows the first tab if no default set', function(){
        // render the component to the DOM
        let rendered_component = TestUtils.renderIntoDocument(panel_component);
        // check if the first tab is active
        expect(isTabActive(rendered_component, 1)).to.be.true;
    });


    it('shows the second tab when `defaultTab` is 2', function(){
        // create a container whose default tab is 2
        let component = (
            <TabContainer defaultTab={2}>
                <Tab title="tab1">tab1</Tab>
                <Tab title="tab2">tab2</Tab>
            </TabContainer>
        )
        // render the component to the DOM
        let rendered_component = TestUtils.renderIntoDocument(component);
        // check if the second tab is active
        expect(isTabActive(rendered_component, 2)).to.be.true;
    });


    it('can switch between tabs', function() {
        // render the component to the DOM
        let rendered_component = TestUtils.renderIntoDocument(panel_component);
        // save a reference to the second nav element
        let navElement = TestUtils.findRenderedDOMComponentWithTag(rendered_component, 'ul');
        let navItem = navElement.getDOMNode().children[1];
        // click on the navigation element
        TestUtils.Simulate.click(navItem);
        // check if the second tab is active
        expect(isTabActive(rendered_component, 2)).to.be.true;
    });
});


// end of file
