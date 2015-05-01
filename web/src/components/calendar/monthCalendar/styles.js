// local imports
import colors from 'styles/colors'

export let calendar_style = {
    width: '100%',
    height: '100%',
};


export let day_labels_style = {
    height: '22px',
    fontSize: '14px',
    textTransform: 'capitalize',
    padding: '10px 0',
    color: colors.darkGrey,
    fontWeight: 'normal',
    borderBottom: `1px solid ${colors.blue}`,
}

export let calendar_container_style = {
    position: 'absolute',
    top: '55px',
    left: '20px',
    right: '20px',
    bottom: '20px',
    background: colors.white,
    overflow: 'hidden',
}

// end of file
