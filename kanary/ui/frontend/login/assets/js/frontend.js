$('#sign-up-modal').modal();

$(document).ready(function() {

    $('.styled').each(function() {
        var this_ = $(this);
        this_.find('input').addClass('hidden');
    });

    $('.styled input').live('click', function() {
        var this_ = $(this);
        var this_checkbox = this_.parent().find('.checkbox');
        this_checkbox.toggleClass('checked', this_.attr('checked'));

    });

    $('.exit').live('click', function() {
        $(this).parent().hide();
    });

});
