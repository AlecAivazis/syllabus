// styles used by the sidebar component

// lodash: https://github.com/lodash/lodash
import _ from 'lodash'
// local imports
import colors from 'styles/colors'

export let container_style = {
    float: 'left',
    height: '100%',
    padding: '0',
    margin: '0',
    width: '240px',
    borderRight: '1px solid #cdc8b3',
    boxSizing: 'border-box',
}

// the tier one sidebar is the base style with a different coloring
export let tier1_style = _.assign({}, container_style, {
    background: colors.sidebar_tier1,
})

export let tier2_style = _.assign({}, container_style, {
    background: colors.sidebar_tier2,
})

export let sidebar_content_style = {
    marginLeft: '240px'
}

// end of file
