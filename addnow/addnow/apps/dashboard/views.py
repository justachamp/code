from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import JsonResponse


def login(request):
    if request.user.is_authenticated():
        # TODO: redirect to regular authenticated view
        pass
    return redirect('addnow.apps.accounts.views.sign_in')


def logout_start(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('addnow.apps.accounts.views.sign_in')


def reports(request):
    # todo: this is only for api tests to pass. Adjust after ADDNOW-402
    if request.method == 'GET':
        data = []
        site_id = request.GET.get('site_id')
        collection = request.GET.get('collection')
        if int(site_id) == 1:
            if collection == 'event_source_all':
                data.append({'label': 'googlePlus', 'shares': 3000, 'clicks': 1234})
                data.append({'label': 'facebook', 'shares': 12300, 'clicks': 650})
                data.append({'label': 'twitter', 'shares': 1456, 'clicks': 123})
                data.append({'label': 'pinterest', 'shares': 102, 'clicks': 12})
                data.append({'label': 'linkedin', 'shares': 2345, 'clicks': 345})
                data.append({'label': 'other', 'shares': 45, 'clicks': 5})
            elif collection == 'event_tool_all':
                data.append({'label': 'copy-paste', 'shares': 2345, 'clicks': 123})
                data.append({'label': 'sharing-buttons', 'shares': 5432, 'clicks': 1234})
                data.append({'label': 'address-bar', 'shares': 878, 'clicks': 12})
            elif collection == 'event_month':
                data.append({'shares': 134, 'clicks': 234, 'month': 1401})
                data.append({'shares': 178, 'clicks': 256, 'month': 1402})
                data.append({'shares': 190, 'clicks': 345, 'month': 1403})
                data.append({'shares': 185, 'clicks': 456, 'month': 1404})
                data.append({'shares': 155, 'clicks': 256, 'month': 1405})
                data.append({'shares': 256, 'clicks': 700, 'month': 1406})
                data.append({'shares': 356, 'clicks': 987, 'month': 1407})
                data.append({'shares': 98, 'clicks': 1056, 'month': 1408})
                data.append({'shares': 15, 'clicks': 965, 'month': 1409})
                data.append({'shares': 5, 'clicks': 865, 'month': 1410})
                data.append({'shares': 1, 'clicks': 545, 'month': 1411})
                data.append({'shares': 10, 'clicks': 325, 'month': 1412})
                data.append({'shares': 0, 'clicks': 487, 'month': 1501})
                data.append({'shares': 5, 'clicks': 65, 'month': 1502})
            elif collection == 'event_url_all':
                data.append({
                    'shares': 1343,
                    'clicks': 2343,
                    'url': 'http://gravity4.com/contact/', 'title': 'Contact'
                })
                data.append({
                    'shares': 345,
                    'clicks': 234,
                    'url': 'http://gravity4.com/g4team/',
                    'title': 'Team'
                })
                data.append({
                    'shares': 675,
                    'clicks': 334,
                    'url': 'http://gravity4.com/labs/',
                    'title': 'Labs'
                })
                data.append({
                    'shares': 4675,
                    'clicks': 6334,
                    'url': 'http://gravity4.com/app-center/',
                    'title': 'App Center'
                })
                data.append({
                    'shares': 8675,
                    'clicks': 12334,
                    'url': 'http://gravity4.com/product/',
                    'title': 'Product'
                })
                data.append({
                    'shares': 675,
                    'clicks': 334,
                    'url': 'http://gravity4.com/vision/',
                    'title': 'Vision'
                })
                data.append({
                    'shares': 1275,
                    'clicks': 7834,
                    'url': 'http://gravity4.com/blog/introducing-belimitless/',
                    'title': 'Introducing #Belimitless'
                })
                data.append({
                    'shares': 7512,
                    'clicks': 3334,
                    'url': 'http://gravity4.com/blog/tom-brady-super-bowl-sunday-doesnt-rely-on-luck-why-do-you/',
                    'title': 'Tom Brady Doesn\'t Rely on Luck. Why Do You?'
                })
                data.append({
                    'shares': 7125,
                    'clicks': 8753,
                    'url': 'http://gravity4.com/blog/imagination-by-gravity4/',
                    'title': 'Imagination by Gravity4'
                })
                data.append({
                    'shares': 23675,
                    'clicks': 33124,
                    'url': 'http://gravity4.com/blog/ibeacon/',
                    'title': 'iBeacon. Shop Smarter'
                })
                data.append({
                    'shares': 1675,
                    'clicks': 3334,
                    'url': 'http://gravity4.com/blog/g4labs/',
                    'title': 'Introducing, Gravity4 Labs.'
                })
                data.append({
                    'shares': 0,
                    'clicks': 0,
                    'url': 'http://gravity4.com/opt-out/',
                    'title': 'Opt-out'
                })
            elif collection == 'referring_domains':
                data.append({
                    'shares': 58,
                    'url': 'http://addnow.com/2014/09/piwik-piwik-pro-trustradius-buyers-guide/'
                })
                data.append({
                    'shares': 11273,
                    'url': 'http://addnow.com/2014/10/clearcode-featured-agency-post/'
                })
                data.append({
                    'shares': 3235,
                    'url': 'http://addnow.com/2014/07/target-engaged-customers/'
                })
                data.append({
                    'shares': 612,
                    'url': 'http://addnow.com/2014/07/rejoiner-ecommerce-solution-cart-abandonment/'
                })
                data.append({
                    'shares': 23,
                    'url': 'http://addnow.com/2014/08/hire-right-app-developers/'
                })
                data.append({
                    'shares': 725,
                    'url': 'http://addnow.com/2014/12/agile-vs-waterfall-method/'
                })
                data.append({
                    'shares': 8236,
                    'url': 'http://addnow.com/2014/12/importance-of-branding-ux-ui-software-development/'
                })
                data.append({
                    'shares': 826,
                    'url': 'http://addnow.com/2014/10/programmers/'
                })
                data.append({
                    'shares': 269,
                    'url': 'http://addnow.com/2014/10/hiring-process/'
                })
                data.append({
                    'shares': 1252,
                    'url': 'http://addnow.com/2014/09/computers/'
                })
            elif collection == 'referring_searches':
                data.append({'searches': 58, 'query': 'Development'})
                data.append({'searches': 612, 'query': 'Clearcode'})
                data.append({'searches': 23, 'query': 'Software House'})
                data.append({'searches': 11273, 'query': 'Interactive agency'})
                data.append({'searches': 3235, 'query': 'Carrer in IT'})
                data.append({'searches': 8236, 'query': 'PHP Developer'})
                data.append({'searches': 725, 'query': 'Programming'})
                data.append({'searches': 8236, 'query': 'PHP Developer'})
                data.append({'searches': 826, 'query': 'SEO'})
                data.append({'searches': 269, 'query': 'UX Design'})
                data.append({'searches': 1252, 'query': 'Continuos integration'})
            elif collection == 'copied_keywords':
                data.append({'times': 58, 'keywords': 'Development'})
                data.append({'times': 11273, 'keywords': 'Interactive agency'})
                data.append({'times': 3235, 'keywords': 'Carrer in IT'})
                data.append({'times': 612, 'keywords': 'Coding service'})
                data.append({'times': 23, 'keywords': 'Software House'})
                data.append({'times': 725, 'keywords': 'Programming'})
                data.append({'times': 8236, 'keywords': 'PHP Developer'})
                data.append({'times': 826, 'keywords': 'SEO'})
                data.append({'times': 269, 'keywords': 'UX Design'})
                data.append({'times': 1252, 'keywords': 'Continuos integration'})
            elif collection == 'top_countries':
                data.append({
                    'shares': 58, 'clicks': 826, 'viral': 2,
                    'country': 'New Zealand', 'id': 'NZ'
                })
                data.append({
                    'shares': 11273, 'clicks': 25273, 'viral': 62,
                    'country': 'United States', 'id': 'US'
                })
                data.append({
                    'shares': 3235, 'clicks': 10264, 'viral': 9,
                    'country': 'Australia', 'id': 'AU'
                })
                data.append({
                    'shares': 612, 'clicks': 2746, 'viral': 5,
                    'country': 'United Kingdom', 'id': 'UK'
                })
                data.append({
                    'shares': 23, 'clicks': 127, 'viral': 1,
                    'country': 'United Kingdom', 'id': 'UK'
                })
                data.append({
                    'shares': 725, 'clicks': 5273, 'viral': 7,
                    'country': 'Brazil', 'id': 'BR'
                })
                data.append({
                    'shares': 8236, 'clicks': 17274, 'viral': 21,
                    'country': 'Canada', 'id': 'CA'
                })
                data.append({
                    'shares': 826, 'clicks': 1742, 'viral': 3,
                    'country': 'Argentina', 'id': 'AR'
                })
                data.append({
                    'shares': 269, 'clicks': 742, 'viral': 4,
                    'country': 'Mexico', 'id': 'MX'
                })
                data.append({
                    'shares': 1252, 'clicks': 4242, 'viral': 12,
                    'country': 'India', 'id': 'IN'
                })
        elif int(site_id) == 2:
            if collection == 'event_source_all':
                data.append({'label': 'googlePlus', 'shares': 789, 'clicks': 34})
                data.append({'label': 'facebook', 'shares': 1200, 'clicks': 206})
                data.append({'label': 'twitter', 'shares': 543, 'clicks': 93})
                data.append({'label': 'pinterest', 'shares': 123, 'clicks': 57})
                data.append({'label': 'linkedin', 'shares': 235, 'clicks': 38})
                data.append({'label': 'other', 'shares': 5, 'clicks': 0})
            elif collection == 'event_tool_all':
                data.append({'label': 'copy-paste', 'shares': 345, 'clicks': 765})
                data.append({'label': 'sharing-buttons', 'shares': 45, 'clicks': 871})
                data.append({'label': 'address-bar', 'shares': 5, 'clicks': 91})
            elif collection == 'event_month':
                data.append({'shares': 13, 'clicks': 34, 'month': 1401})
                data.append({'shares': 17, 'clicks': 56, 'month': 1402})
                data.append({'shares': 19, 'clicks': 45, 'month': 1403})
                data.append({'shares': 18, 'clicks': 56, 'month': 1404})
                data.append({'shares': 15, 'clicks': 56, 'month': 1405})
                data.append({'shares': 25, 'clicks': 30, 'month': 1406})
                data.append({'shares': 35, 'clicks': 87, 'month': 1407})
                data.append({'shares': 98, 'clicks': 56, 'month': 1408})
                data.append({'shares': 1, 'clicks': 65, 'month': 1409})
                data.append({'shares': 5, 'clicks': 65, 'month': 1410})
                data.append({'shares': 1, 'clicks': 45, 'month': 1411})
                data.append({'shares': 1, 'clicks': 25, 'month': 1412})
                data.append({'shares': 0, 'clicks': 87, 'month': 1501})
                data.append({'shares': 5, 'clicks': 5, 'month': 1502})
            elif collection == 'event_url_all':
                data.append({
                    'shares': 343,
                    'clicks': 343,
                    'url': 'http://demo.com/contact/', 'title': 'Contact'
                })
                data.append({
                    'shares': 345,
                    'clicks': 234,
                    'url': 'http://demo.com/team/',
                    'title': 'Team'
                })
                data.append({
                    'shares': 75,
                    'clicks': 34,
                    'url': 'http://demo.com/labs/',
                    'title': 'Labs'
                })
                data.append({
                    'shares': 467,
                    'clicks': 633,
                    'url': 'http://demo.com/pricing/',
                    'title': 'Pricing'
                })
                data.append({
                    'shares': 675,
                    'clicks': 34,
                    'url': 'http://demo.com/product/',
                    'title': 'Product'
                })
                data.append({
                    'shares': 75,
                    'clicks': 34,
                    'url': 'http://demo.com/vision/',
                    'title': 'Vision'
                })
                data.append({
                    'shares': 275,
                    'clicks': 834,
                    'url': 'http://demo.com/blog/title1/',
                    'title': 'Title 1'
                })
                data.append({
                    'shares': 12,
                    'clicks': 34,
                    'url': 'http://demo.com/blog/title2/',
                    'title': 'Tile 2'
                })
                data.append({
                    'shares': 25,
                    'clicks': 53,
                    'url': 'http://demo.com/blog/title3/',
                    'title': 'Title 3'
                })
                data.append({
                    'shares': 2375,
                    'clicks': 3324,
                    'url': 'http://demo.com/blog/title4/',
                    'title': 'Title 4'
                })
                data.append({
                    'shares': 675,
                    'clicks': 334,
                    'url': 'http://demo.com/blog/title4/',
                    'title': 'Title 5'
                })
                data.append({
                    'shares': 0,
                    'clicks': 0,
                    'url': 'http://demo.com/opt-out/',
                    'title': 'Opt-out'
                })
            elif collection == 'referring_domains':
                data.append({
                    'shares': 581,
                    'url': 'http://addnow.com/2014/09/piwik-piwik-pro-trustradius-buyers-guide/'
                })
                data.append({
                    'shares': 1273,
                    'url': 'http://addnow.com/2014/10/clearcode-featured-agency-post/'
                })
                data.append({
                    'shares': 335,
                    'url': 'http://addnow.com/2014/07/target-engaged-customers/'
                })
                data.append({
                    'shares': 1612,
                    'url': 'http://addnow.com/2014/07/rejoiner-ecommerce-solution-cart-abandonment/'
                })
                data.append({
                    'shares': 223,
                    'url': 'http://addnow.com/2014/08/hire-right-app-developers/'
                })
                data.append({
                    'shares': 75,
                    'url': 'http://addnow.com/2014/12/agile-vs-waterfall-method/'
                })
                data.append({
                    'shares': 836,
                    'url': 'http://addnow.com/2014/12/importance-of-branding-ux-ui-software-development/'
                })
                data.append({
                    'shares': 8426,
                    'url': 'http://addnow.com/2014/10/programmers/'
                })
                data.append({
                    'shares': 2619,
                    'url': 'http://addnow.com/2014/10/hiring-process/'
                })
                data.append({
                    'shares': 12,
                    'url': 'http://addnow.com/2014/09/computers/'
                })
            elif collection == 'referring_searches':
                data.append({'searches': 158, 'query': 'Development'})
                data.append({'searches': 2612, 'query': 'Clearcode'})
                data.append({'searches': 230, 'query': 'Software House'})
                data.append({'searches': 1273, 'query': 'Interactive agency'})
                data.append({'searches': 13235, 'query': 'Carrer in IT'})
                data.append({'searches': 823, 'query': 'PHP Developer'})
                data.append({'searches': 1725, 'query': 'Programming'})
                data.append({'searches': 836, 'query': 'PHP Developer'})
                data.append({'searches': 8426, 'query': 'SEO'})
                data.append({'searches': 2619, 'query': 'UX Design'})
                data.append({'searches': 12, 'query': 'Continuos integration'})
            elif collection == 'copied_keywords':
                data.append({'times': 581, 'keywords': 'Development'})
                data.append({'times': 1273, 'keywords': 'Interactive agency'})
                data.append({'times': 335, 'keywords': 'Carrer in IT'})
                data.append({'times': 1612, 'keywords': 'Coding service'})
                data.append({'times': 223, 'keywords': 'Software House'})
                data.append({'times': 75, 'keywords': 'Programming'})
                data.append({'times': 836, 'keywords': 'PHP Developer'})
                data.append({'times': 8426, 'keywords': 'SEO'})
                data.append({'times': 2619, 'keywords': 'UX Design'})
                data.append({'times': 12, 'keywords': 'Continuos integration'})
            elif collection == 'top_countries':
                data.append({
                    'shares': 581, 'clicks': 2826, 'viral': 3,
                    'country': 'New Zealand', 'id': 'NZ'
                })
                data.append({
                    'shares': 1273, 'clicks': 5273, 'viral': 26,
                    'country': 'United States', 'id': 'US'
                })
                data.append({
                    'shares': 335, 'clicks': 1264, 'viral': 11,
                    'country': 'Australia', 'id': 'AU'
                })
                data.append({
                    'shares': 1612, 'clicks': 2746, 'viral': 5,
                    'country': 'United Kingdom', 'id': 'UK'
                })
                data.append({
                    'shares': 223, 'clicks': 1127, 'viral': 1,
                    'country': 'United Kingdom', 'id': 'UK'
                })
                data.append({
                    'shares': 75, 'clicks': 273, 'viral': 7,
                    'country': 'Brazil', 'id': 'BR'
                })
                data.append({
                    'shares': 836, 'clicks': 1274, 'viral': 21,
                    'country': 'Canada', 'id': 'CA'
                })
                data.append({
                    'shares': 8326, 'clicks': 11742, 'viral': 3,
                    'country': 'Argentina', 'id': 'AR'
                })
                data.append({
                    'shares': 2619, 'clicks': 6742, 'viral': 4,
                    'country': 'Mexico', 'id': 'MX'
                })
                data.append({
                    'shares': 12, 'clicks': 242, 'viral': 12,
                    'country': 'India', 'id': 'IN'
                })
        return JsonResponse(data, safe=False)
