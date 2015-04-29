// test various functionalities of the TabContainer component 
// uses mocha and chai

// react
import React from 'react';
// facebook test utils
import TestUtils from 'react/lib/ReactTestUtils';
// local imports
import MonthCalendar from '../component';

describe("MonthCalendar", () => {

    // define the common component needed for the test suite
    let calendar_component = (
        <MonthCalendar/>
    )

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
        let rendered_component = TestUtils.renderIntoDocument(calendar_component);
        // check that it worked
        expect(rendered_component).to.exist;
    });

});


// end of file
