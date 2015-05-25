// the GradingScaleControl component used by the syllabus front end

// react: https://github.com/facebook/react
import React from 'react'
// locla imports
import Icon from 'components/misc/icon'

'use strict'

class GradingScaleControl extends React.Component {

    constructor() {
        // instantiate this
        super()
        // bind various functions
        this.get_control_elements = this.get_control_elements.bind(this)
    }


    render() {
        // render the component
        return (
            <div>
                {this.get_control_elements()}
            </div>
        )
    }


    get_control_elements(){
        // keep the elements to add in a list
        let elements = []
        // create an array out of the keys of the scale
        let bounds = Array.from(this.props.course.gradingScale.keys()).sort()
        // go over the array in the old school way since we need an index
        for (let index = 0; index < bounds.length ; index++){
            // this categories bounds
            let lower_bound = bounds[index]
            let upper_bound = index != bounds.length - 1 ? bounds[index + 1] : 100
            // the grade corresponding to this category
            let grade = this.props.course.gradingScale.get(lower_bound)
            // add the category to the list
            elements.push(
                <div key={index} style={{whiteSpace: "nowrap"}}>
                    <span>

                    </span>
                    <span>
                        {lower_bound} to {upper_bound} <Icon name="right-arrow-fat" /> {grade}
                    </span>
                    <span>

                    </span>
                </div>
            )
        }

        // return the elements
        return elements.reverse()
    }
}

GradingScaleControl.propTypes = {
    course: React.PropTypes.object.isRequired
}


// export the class
export default GradingScaleControl

// end of file
