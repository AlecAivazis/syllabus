// the styles used by the TabContainer component

// lodash: https://github.com/lodash/lodash
import _ from 'lodash';
// tab images
import left_edge_image from './images/left.png';
import right_edge_image from './images/right.png';
import center_image from './images/center.png';
// active tab images
import left_edge_active_image from './images/left_active.png';
import right_edge_active_image from './images/right_active.png';
import center_active_image from './images/center_active.png';

let menu_element_height = '35px';
let menu_element_edge_width = '25px';

export let menu_element_style = {
    display: 'inline-block',
    height: menu_element_height,
    cursor: 'pointer',
    marginLeft: '-7.5%',
    lineHeight: menu_element_height,
    zIndex: 1,
    position: 'relative',
};

// "inherit" from the non active case
export let menu_element_active_style = _.assign({}, menu_element_style, {
    zIndex: 2
});

export let menu_element_left_edge_style = {
    backgroundImage: `url('${left_edge_image}')`,
    width: menu_element_edge_width,
    height: menu_element_height,
    backgroundSize: 'cover',
    display: 'inline-block',
}

export let table_container_style = {
}

// "inherit" from the non active case
export let menu_element_left_edge_active_style = _.assign({}, menu_element_left_edge_style, {
    backgroundImage: `url('${left_edge_active_image}')`,
});

export let menu_element_right_edge_style = {
    backgroundImage: `url('${right_edge_image}')`,
    width: menu_element_edge_width,
    height: menu_element_height,
    backgroundSize: 'cover',
    display: 'inline-block',
}

// "inherit" from the non active case
export let menu_element_right_edge_active_style = _.assign({}, menu_element_right_edge_style, {
    backgroundImage: `url('${right_edge_active_image}')`,
});

export let menu_element_center_style = {
    backgroundImage: `url('${center_image}')`,
    height: menu_element_height,
    display: 'inline-block',
}

// "inherit" from the non active case
export let menu_element_center_active_style = _.assign({}, menu_element_center_style, {
    backgroundImage: `url('${center_active_image}')`,
});

export let list_container_style = {
    padding: '0',
    margin: '0',
    display: 'inline-block',
};

export let menu_toolbar_style = {
    float: 'right',
};

export let header_style = {
    padding: '0px 40px 0px 40px',
};

export let container_style = {
    padding: '20px',
    position: 'absolute',
    top: 0,
    right: 0,
    bottom: 0,
    left: 0,
};

// end of file