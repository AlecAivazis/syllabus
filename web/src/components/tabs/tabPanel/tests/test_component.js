// test various functionalities of the TabPanel component 
// uses mocha and chai

// react
import React from 'react';
// facebook test utils
import TestUtils from 'react/lib/ReactTestUtils';
// local imports
import TabPanel from '../component';
import Tab from '../../tab/component';

describe("Tab Panel", () => {

    // define the components to be rendered to the dom
    let tab1 = <Tab title="tab1">tab1</Tab>;
    let tab2 = <Tab title="tab2">tab2</Tab>
    let panel_component = (
        <TabPanel>
            {tab1}
            {tab2}
        </TabPanel>
    )


    it('renders to the DOM', function() {
        // render the component to the DOM
        let rendered_component = TestUtils.renderIntoDocument(panel_component);
        // check that it worked
        expect(rendered_component).to.exist;
    });


    it('fails if no tabs are given', function(){

    });


    it('shows the first tab if no default set', function(){

    });


    it('allows for a default tab to be set', function(){

    });


    it('can switch between views', function() {

    });
});


// end of file
