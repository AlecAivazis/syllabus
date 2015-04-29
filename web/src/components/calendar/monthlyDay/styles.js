// styles used by the monthly day component

// lodash: https://github.com/lodash/lodash
import _ from 'lodash';
// local imports
import colors from 'styles/colors'

export let day_style = {
    overflow: 'hidden',
    verticalAlign: 'top',
    padding: '1%',
};

export let day_off_month_style = _.assign({}, day_style,{
    color: colors.lightGrey,
});


// end of file
