/**
    Modify bootstrap-button API to use btn-radio class.
*/
$(document).on('click.bs.button.data-api', '[data-toggle^=button]', function (e) {
    var $btn = $(e.target)
    if (!$btn.hasClass('btn-radio')) $btn = $btn.closest('.btn-radio')
    $btn.button('toggle')
    e.preventDefault()
})