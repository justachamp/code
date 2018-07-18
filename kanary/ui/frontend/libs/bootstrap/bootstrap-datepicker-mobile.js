/* =========================================================
 * Mobile-friendly version of bootstrap-datepicker
 * Which is always displayed aligned to left of input
 * ========================================================= */
 
!function( $ ) {
	
	var Datepicker = $.fn.datepicker.Constructor;

	var DatepickerMobile = function(element, options){
		Datepicker.apply(this, arguments);
	};
	
	DatepickerMobile.prototype = _.extend(_.clone(Datepicker.prototype), {
		constructor: DatepickerMobile,

		place: function(){
            var offsetLeft = this.element.offset().left;
            var offsetTop = (this.component ? this.component.offset() : this.element.offset()).top;
			this.picker.css({
				top: offsetTop + this.height,
				left: offsetLeft
			});
		}

	});
	
	$.fn.datepickermobile = function ( option, val ) {
		return this.each(function () {
			var $this = $(this),
				data = $this.data('datepicker'),
				options = typeof option === 'object' && option;
			if (!data) {
				$this.data('datepicker', (data = new DatepickerMobile(this, $.extend({}, $.fn.datepicker.defaults,options))));
			}
			if (typeof option === 'string') data[option](val);
		});
	};

	$.fn.datepickermobile.defaults = _.extend(
		_.clone($.fn.datepicker.defaults),
		{}	
	)
	$.fn.datepickermobile.Constructor = DatepickerMobile;
}( window.jQuery );