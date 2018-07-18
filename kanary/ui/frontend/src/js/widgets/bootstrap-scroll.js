/**
* A facade to nicescroll plugin that resizes when bootstrap components
* like dropdown, collapse change inside its viewport.
* @this jQuery
* @return {jQuery} this
*/
$.fn.bootstrapScroll = function() {
    var $element = this;
    $element.niceScroll();
    var nicescroll = $element.getNiceScroll();
    var events = 'shown.bs.dropdown hidden.bs.dropdown ' +
        'shown.bs.collapse hidden.bs.collapse';
    $element.on(events, function() {
        nicescroll.resize();
    });
    return this;
};

