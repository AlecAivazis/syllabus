// styles used by the monthly day component

// lodash: https://github.com/lodash/lodash
import _ from 'lodash';
// local imports
import colors from 'styles/colors'

export let day_style = {
    height: '100%',
    float: 'left',
    display: 'inline-block',
    MozBoxSizing: 'border-box',
    WebkitBoxSizing: 'border-box',
    textAlign: 'center',
}

export let day_header_style = {
    borderTop: `1px solid ${colors.blue}`,
    borderBottom: `1px solid ${colors.blue}`,
    padding: '10px 0',
    overflow: 'hidden',
}

// end of file
