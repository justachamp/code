define(['./helpers/_helpers_'], function(Helpers) {

	var ViewTemplate = function(parent, viewTemplate) {
		this.createView(parent, viewTemplate);
	};

	ViewTemplate.prototype.getJQueryElement = function() {
		return this.jQueryElement;
	};

	ViewTemplate.prototype.getDomElement = function() {
		return this.jQueryElement.get(0);
	};

	ViewTemplate.prototype.appendTo = function(parent) {
		this.jQueryElement.appendTo(parent);
	};

	ViewTemplate.prototype.remove = function() {
		this.jQueryElement.remove();
	};

	ViewTemplate.prototype.hide = function() {
		this.jQueryElement.hide();
	};

	ViewTemplate.prototype.show = function() {
		this.jQueryElement.show();
	};

	ViewTemplate.prototype.createView = function(parentElement, viewText) {
		this.jQueryElement = $(viewText);

		if (parentElement) {
			parentElement.append(this.jQueryElement);
		}
	};

	return ViewTemplate;
});
