define(
    ['text!./view.html', 'storage', 'brand'],
    function(template, storage, brand) {

        var Component = function(moduleContext) {

            this.template = template;
            this.panel = null;
            this.vm = new brand.Brand();

            this.activate = function(params) {

                if (brand.brands().length === 0) {
                    return storage.init();
                }

                return $.Deferred().resolve();
            };

            this.onUrlChange = function(params) {
                var currentBrand = this.vm;

                // Refresh audiences list and fetch audience based on its id
                return brand.get().done(function() {
                    currentBrand.load(params.id);
                });
            };
        };

        return Component;
    });
