function newInput(){
    if ($('input[type="file"]').eq(-1).val() != ''){
        $('<input/>').attr({
            type: 'file',
            name: 'files',
            onchange: 'newInput()'
        }).addClass('multiFileInput').appendTo('#multiFile');
    }
}