// the styles used by the TabContainer component

import left_edge_image from './images/left_edge.png';
import right_edge_image from './images/right_edge.png';
import center_image from './images/center.png';

let menu_element_height = '35px';
let menu_element_edge_width = '25px';

export let menu_element_style = {
    display: 'inline-block',
    height: menu_element_height,
    cursor: 'pointer',
    marginLeft: '-10%',
    lineHeight: menu_element_height,
};

export let menu_element_left_edge_style = {
    backgroundImage: `url('${left_edge_image}')`,
    width: menu_element_edge_width,
    height: menu_element_height,
    backgroundSize: 'stretch',
    display: 'inline-block',
}

export let menu_element_right_edge_style = {
    backgroundImage: `url('${right_edge_image}')`,
    width: menu_element_edge_width,
    height: menu_element_height,
    backgroundSize: 'stretch',
    display: 'inline-block',
}

export let menu_element_center_style = {
    backgroundImage: `url('${center_image}')`,
    height: menu_element_height,
    display: 'inline-block',
}

export let active_menu_element_style = {

};

export let list_container_style = {
    padding: '0',
    margin: '0',
    display: 'inline-block',
};

export let menu_toolbar_style = {
    float: 'right',
};

export let header_style = {
    padding: '10px 40px 0px 40px',
};

export let container_style = {
    padding: '20px',
};

export let tab_style = {
    background: 'white',
    zIndex: '5',
    display: 'inline'
};

// end of file