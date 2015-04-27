// test various functionalities of the TabContainer component 
// uses mocha and chai

// react
import React from 'react';
// facebook test utils
import TestUtils from 'react/lib/ReactTestUtils';
// local imports
import TabContainer from '../component';
import Tab from '../../tab/component';

describe("Tab Panel", () => {

    // define the common component needed for the test suite
    let panel_component = (
        <TabContainer>
            <Tab title="tab1">tab1</Tab>
            <Tab title="tab2">tab2</Tab>
        </TabContainer>
    )

    
    // after each test
    afterEach(function(done) {
        // remove any react components that are mounted at the body
        React.unmountComponentAtNode(document.body)
        // double check
        document.body.innerHTML = "" 
        // we're finished
        setTimeout(done)
    })


    it('renders to the DOM', function() {
        // render the component to the DOM
        let rendered_component = TestUtils.renderIntoDocument(panel_component);
        // check that it worked
        expect(rendered_component).to.exist;
    });


    it('throws if no tabs are given', function(){
        // check that the component throws if rendered without tabs
        expect(function(){TestUtils.renderIntoDocument(<TabContainer/>)})
            .to.throw(Error);
    });


    it('shows the first tab if no default set', function(){

    });


    it('shows the second tab when `defaultTab` is 2', function(){

    });


    it('can switch between views', function() {

    });
});


// end of file
