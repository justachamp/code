
//    $('.typeahead, #typeahead-website').typeahead({
//        name:'countries',
//        local:[
//            {
//                "value":"New York",
//                "country":"USA"
//            },
//            {
//                "value":"aaaaa",
//                "country":"Australia"
//            },
//            {
//                "value":"aabb",
//                "country":"Australia"
//            },
//            {
//                "value":"Toronto",
//                "country":"Canada"
//            },
//            {
//                "value":"Wroclaw",
//                "country":"Poland"
//            }
//        ],
//        template:[
//            '<p class="tt-value">{{value}}</p>',
//            '<p class="tt-helper">{{country}}</p>'
//        ].join(''),
//        limit:10,
//        engine:Hogan
//    });
//
//    $('.typeahead').on('typeahead:selected', function (e, value) {
//        console.log(e, value);
//    });

$(document).delegate('.switcher', 'click', function () {
    $(this).toggleClass('on');
    return false;
});

$(document).delegate('.checkbox', 'click', function () {
    $(this).toggleClass('checked');
    return false;
});

var scrollViewport = $(sidebar).find('.sidebar-viewport'),
    contentSelector = '.sidebar-content',
    scrollContent = $(scrollViewport).find(contentSelector);
if ((scrollViewport.length == 0) || (scrollContent.length == 0)) {
    throw 'Sidebar view does\` have correct structure.' +
        ' Scrolling is disabled.';
} else {
    $(scrollViewport).niceScroll([contentSelector, {}]);
}


$("#content").niceScroll();

$('[data-toggle="modal"]').click(function () {
    $('#sample-modal').toggleClass('in');
})

$('[data-toggle="overlay"]').click(function () {
    $('#overlay').toggleClass('in');
})

$('[data-toggle="toast-message"]').click(function () {
    $('#sample-message').toggleClass('in');
})

$('[data-toggle="tray"]').click(function () {
    var target = $(this).data('target');
    $(target).toggleClass('in');
})

$('[data-toggle="tooltip"]').tooltip('show');

$('[data-toggle="popover"]').popover();


var today = Date.create('today');

$('#datepicker').daterangepicker();

$('#datepicker2').daterangepicker();

$('#datepicker-sidebar').daterangepicker();

$('#daterange-picker').daterangepicker(
{
    ranges:{
        'Today':['today', 'today'],
        'Yesterday':['yesterday', 'yesterday'],
        'Last 7 Days':[Date.create('today').addDays(-6), Date.create('today')],
        'Last 30 Days':[Date.create('today').addDays(-29), today],
        'This Month':[Date.create('today').beginningOfMonth(), Date.create('today').endOfMonth()],
        'Last Month':[Date.create('today').beginningOfMonth().rewind({ months:1 }), Date.create('today').beginningOfMonth().addDays(-1)]
    },
    opens:'left',
    format:'{MM}/{dd}/{yyyy}',
    separator:' to ',
    startDate:Date.create('today').addDays(-29),
    endDate:Date.create('today'),
    minDate:'01/01/2012',
    maxDate:'12/31/2013',
    locale:{
        applyLabel:'Submit',
        fromLabel:'From',
        toLabel:'To',
        customRangeLabel:'Custom Range',
        daysOfWeek:['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'],
        monthNames:['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        firstDay:1
    },
    showWeekNumbers:false
},
function (start, end) {
    $('#reportrange span').html(start.short() + ' - ' + end.short());
}
);

$('.timepicker-input').timepicker({showMeridian:false});

$('.range-slider').empty().each(function () {

    var slider = $(this),
    infobox = $('<span class="infoBox" />');

    var startValue = slider.data('value'),
    scale = slider.data('scale');

    slider
    .noUiSlider('init', {
        handles:1,
        scale:scale,
        start:startValue,
        change:function () {

            var newValue = $(this).noUiSlider('value');

            infobox.text(newValue[1]);
        }
    })
    .find('.noUi-handle div')
    .append(infobox.text(startValue));
});
