// styling for the sidebar elements used by syllabus

export let elemet_style = {
    padding: '15px',
}

// the tier one sidebar is the base style with a different coloring
export let tier1_style = _.assign({}, elemet_style, {
    borderBottom: '1px solid #cac7b7',
    boxShadow:' 0 1px 0 #dcd9c9',
})

export let tier2_style = _.assign({}, elemet_style, {
    borderBottom: '1px solid #cac7b7',
    boxShadow:' 0 1px 0 #dcd9c9',
})

// end of file
