var signupModule = (function() {
    $.fn.serializeForm = function() {
        var data = {},
            items = this.serializeArray();
        $.each(items, function(i,item) {
            data[item['name']]=item['value'];
        });
        return data;
    }  
  
    function initCheckboxes() {

        $(document).ready(function() {
            var $checkbox = $('.checkbox');
            if ($checkbox.hasClass('checked')) {
                $checkbox.find('input').prop('checked', true);
            }
        });

        $(document).delegate('.checkbox', 'click', function() {
            var $checkboxInput = $(this).find('input');

            $(this).toggleClass('checked');
            $checkboxInput.prop('checked', $(this).hasClass('checked'));

            return false;
        });
    };

    function initStatesSelect() {
        var $countrySelect = $('select[name="country"]');

        $countrySelect.on('change', fetchStates);
    };

    function fetchStates() {
        var $stateSelect = $('select[name="province"]'),
            countryCode = $(this).val(),
            fetchUrl = Urls.fetch_states(),
            token = $('input[name="csrfmiddlewaretoken"]').val();

        $stateSelect.html('');

        $.ajax({
            url: fetchUrl,
            type: 'POST',
            data: {
                code: countryCode
            },
            headers: {
                'X-CSRFToken': token
            },
            success: function(response) {
               $.each(response.states, function(index, state) {
                  option = document.createElement('option');
                  option.text = state[0];
                  option.value = state[1];
                  $stateSelect.append(option);
               });
            }
        });
    };

    function initErrorInputs() {
        $(document).ready(function() {
            $('.input-error').on('click', clearErrorClass);
        });
    };

    function clearErrorClass() {
        $(this).removeClass('input-error');
    };
  
    function saveBeforeLogout() {
        $('.link-logout').on('click', function(e){
            var self = $(this),
                form = $('.create-profile-form'),
                items = form.serializeForm(),
                url = form.attr('action'); console.log('*** ', items);
          
            e.preventDefault();
            $.post(url, items, function(){
                window.location = self.attr('href');
            });
        });
    }

    return {
        initCheckboxes: initCheckboxes,
        initStatesSelect: initStatesSelect,
        initErrorInputs: initErrorInputs,
        saveBeforeLogout: saveBeforeLogout
    };

})();

signupModule.initCheckboxes();
signupModule.initStatesSelect();
signupModule.initErrorInputs();
signupModule.saveBeforeLogout();
