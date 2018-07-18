!function ($) {

    "use strict"; // jshint ;_;


    var ExTables = function (element, options) {
        this.$element = $(element)
        this.options = $.extend({}, $.fn.extables.defaults, options);
        this.dropdownContainer = $(this.$element.data('target'));
        this.init();
    }

    ExTables.prototype = {
        constructor:ExTables,

        addCollapse:function () {
            var self = this,
                toggleHandler = this.$element.find('[data-toggle="table-row"]');

            toggleHandler.bind('click', function () {
                var tableRow = $(this).parents('tr'),
                    isCollapsed = tableRow.hasClass('collapsed'),
                    level = +tableRow.data('level');

                if (isCollapsed)
                    tableRow
                        .nextUntil('tr[data-level!="'+(++level) +'"]')
                        .show();
                else
                    tableRow
                        .nextUntil('tr[data-level="'+level+'"]')
                        .addClass('collapsed')
                        .filter(function(index){
                            return $(this).data('level') > level;
                        })
                        .hide();

                tableRow.toggleClass('collapsed');

                return false;
            });
        },

        addDropdown:function (tableHeaders) {

            var table = this.$element,
                tableHeaders = this.$element.find("th"),
                checkboxList = '';

            tableHeaders.each(function (i) {
                var th = $(this);
                if (!th.is('.persist')) {
                    checkboxList += '<li><label class="checkbox checked"><input checked="checked" data-toggle="responsive-cols" type="checkbox" data-colId="' + i + '" class="toggleColCheckbox" />' + th.text() + '</label></li>';
                }
            })

            this.dropdownContainer[0].innerHTML = checkboxList;

            this.dropdownContainer.find("input").each(function () {
                var input = $(this),
                    colId = parseInt(input.attr('data-colId')) + 1,
                    cols = table.find('tr > :nth-child(' + (colId ) + ')');

                input
                    .change(function () {
                        (input.is(":checked")) ? cols.show() : cols.hide();

                    }).bind("updateCheck",function () {
                        (cols.is(":visible")) ? $(this).prop("checked", true).trigger('change') : $(this).prop("checked", false).trigger('change');

                    }).trigger("updateCheck");
            })


            $(window).on("resize", function () {
                $('[data-toggle="responsive-cols"]').trigger("updateCheck");
            })


        }, init:function () {

            var self = this,
                table = this.$element;

            if (table.is('.toggle-col'))
                self.addDropdown()

            if (table.is('.collapse-col'))
                self.addCollapse()

        }
    }

    var old = $.fn.extables

    $.fn.extables = function (option) {
        return this.each(function () {
            var $this = $(this)
                , data = $this.data('extables')
                , options = typeof option == 'object' && option
            if (!data) $this.data('extables', (data = new ExTables(this, options)))
            if (typeof option == 'string') data[option]()
        })
    }

    $.fn.extables.Constructor = ExTables

    $.fn.extables.noConflict = function () {
        $.fn.extables = old
        return this
    }

    $(window).on('load', function () {
        $('[data-tables="extables"]').each(function () {
            $(this).extables();
        })
    })

}(window.jQuery);