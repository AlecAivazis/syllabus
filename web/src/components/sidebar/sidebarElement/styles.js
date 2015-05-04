// styling for the sidebar elements used by syllabus

export let elemet_style = {
    padding: '15px',
    cursor: 'pointer',
    color: 'black',
    textDecoration: 'none',
}

export let tier1_style = _.assign({}, elemet_style, {
    borderBottom: '1px solid #cac7b7',
    boxShadow:' 0 1px 0 #dcd9c9',
})

export let tier2_style = _.assign({}, elemet_style, {
    borderBottom: '1px solid #cac7b7',
    boxShadow:' 0 1px 0 #dcd9c9',
})

export let text_style = {
    color: 'black',
    textTransform: 'none',
}

// end of file
