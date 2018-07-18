$.mockjax({
    url: '/dashboard/sidebar',
    responseTime: 1,
    proxy: '/static/server/dashboard_sidebar.txt'
});

$.mockjax({
    url: '/api/locations',
    responseTime: 1,
    proxy: '/static/server/targeting_cities.txt'
});
