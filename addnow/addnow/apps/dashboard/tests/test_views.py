from django.core.urlresolvers import reverse
from django.test import override_settings
from django.test.client import RequestFactory
from django.test.testcases import TestCase

from addnow.apps.accounts.factories import UserFactory
from addnow.apps.dashboard import views


class TestViews(TestCase):

    @override_settings(DEBUG=True)
    def test_login(self):
        """
        Login and logout
        """
        user = UserFactory()
        login_url = reverse('dashboard:login')
        response = self.client.post(login_url, data={'user': user.email, 'password': user.password})
        self.assertEqual(response.status_code, 302)
        logout_url = reverse('dashboard:logout_start')
        response = self.client.get(logout_url)
        self.assertEqual(response.status_code, 302)

    def test_report(self):
        """
        Though dashboard.views.report is a view for test_api, it should be tested
        because a change here it could affect another test module
        """
        self.factory = RequestFactory()
        # site_id: 1
        # event_source_all
        request = self.factory.get('report', data={'site_id': 1, 'collection': 'event_source_all'})
        response = views.reports(request)
        json_response = '[{"clicks": 1234, "shares": 3000, "label": "googlePlus"}, ' \
                        '{"clicks": 650, "shares": 12300, "label": "facebook"}, ' \
                        '{"clicks": 123, "shares": 1456, "label": "twitter"}, ' \
                        '{"clicks": 12, "shares": 102, "label": "pinterest"}, ' \
                        '{"clicks": 345, "shares": 2345, "label": "linkedin"}, ' \
                        '{"clicks": 5, "shares": 45, "label": "other"}]'
        self.assertEqual(response.content, json_response)
        # event_tool_all
        self.factory = RequestFactory()
        request = self.factory.get('report', data={'site_id': 1,
                                                   'collection': 'event_tool_all'})
        response = views.reports(request)
        json_response = '[{"clicks": 123, "shares": 2345, "label": "copy-paste"}, ' \
                        '{"clicks": 1234, "shares": 5432, "label": "sharing-buttons"}, ' \
                        '{"clicks": 12, "shares": 878, "label": "address-bar"}]'
        self.assertEqual(response.content, json_response)
        # event_month
        request = self.factory.get('report', data={'site_id': 1,
                                                   'collection': 'event_month'})
        response = views.reports(request)
        json_response = '[{"clicks": 234, "shares": 134, "month": 1401}, ' \
                        '{"clicks": 256, "shares": 178, "month": 1402}, ' \
                        '{"clicks": 345, "shares": 190, "month": 1403}, ' \
                        '{"clicks": 456, "shares": 185, "month": 1404}, ' \
                        '{"clicks": 256, "shares": 155, "month": 1405}, ' \
                        '{"clicks": 700, "shares": 256, "month": 1406}, ' \
                        '{"clicks": 987, "shares": 356, "month": 1407}, ' \
                        '{"clicks": 1056, "shares": 98, "month": 1408}, ' \
                        '{"clicks": 965, "shares": 15, "month": 1409}, ' \
                        '{"clicks": 865, "shares": 5, "month": 1410}, ' \
                        '{"clicks": 545, "shares": 1, "month": 1411}, ' \
                        '{"clicks": 325, "shares": 10, "month": 1412}, ' \
                        '{"clicks": 487, "shares": 0, "month": 1501}, ' \
                        '{"clicks": 65, "shares": 5, "month": 1502}]'
        self.assertEqual(response.content, json_response)
        # event_url_all
        request = self.factory.get('report', data={'site_id': 1, 'collection': 'event_url_all'})

        response = views.reports(request)
        json_response = '[{"url": "http://gravity4.com/contact/", ' \
                        '"clicks": 2343, "shares": 1343, "title": "Contact"}, ' \
                        '{"url": "http://gravity4.com/g4team/", "clicks": 234, ' \
                        '"shares": 345, "title": "Team"}, ' \
                        '{"url": "http://gravity4.com/labs/", "clicks": 334, ' \
                        '"shares": 675, "title": "Labs"}, ' \
                        '{"url": "http://gravity4.com/app-center/", ' \
                        '"clicks": 6334, "shares": 4675, ' \
                        '"title": "App Center"}, ' \
                        '{"url": "http://gravity4.com/product/", ' \
                        '"clicks": 12334, "shares": 8675, ' \
                        '"title": "Product"}, ' \
                        '{"url": "http://gravity4.com/vision/", ' \
                        '"clicks": 334, "shares": 675, "title": "Vision"}, ' \
                        '{"url": "http://gravity4.com/blog/introducing-belimitless/", ' \
                        '"clicks": 7834, "shares": 1275, ' \
                        '"title": "Introducing #Belimitless"}, ' \
                        '{"url": "http://gravity4.com/blog/tom-brady-super-bowl-sunday-doesnt-rely-on-luck-why-do-you/", ' \
                        '"clicks": 3334, "shares": 7512, ' \
                        '"title": "Tom Brady Doesn\'t Rely on Luck. Why Do You?"}, ' \
                        '{"url": "http://gravity4.com/blog/imagination-by-gravity4/", ' \
                        '"clicks": 8753, "shares": 7125, "title": "Imagination by Gravity4"}, ' \
                        '{"url": "http://gravity4.com/blog/ibeacon/", "clicks": 33124, ' \
                        '"shares": 23675, "title": "iBeacon. Shop Smarter"}, ' \
                        '{"url": "http://gravity4.com/blog/g4labs/", ' \
                        '"clicks": 3334, "shares": 1675, ' \
                        '"title": "Introducing, Gravity4 Labs."}, ' \
                        '{"url": "http://gravity4.com/opt-out/", ' \
                        '"clicks": 0, "shares": 0, "title": "Opt-out"}]'
        self.assertEqual(response.content, json_response)
        # referring_domains
        request = self.factory.get('report', data={'site_id': 1, 'collection': 'referring_domains'})
        response = views.reports(request)
        json_response = '[{"url": "http://addnow.com/2014/09/piwik-piwik-pro-trustradius-buyers-guide/", ' \
                        '"shares": 58}, {"url": "http://addnow.com/2014/10/clearcode-featured-agency-post/", ' \
                        '"shares": 11273}, ' \
                        '{"url": "http://addnow.com/2014/07/target-engaged-customers/", ' \
                        '"shares": 3235}, ' \
                        '{"url": "http://addnow.com/2014/07/rejoiner-ecommerce-solution-cart-abandonment/", ' \
                        '"shares": 612}, ' \
                        '{"url": "http://addnow.com/2014/08/hire-right-app-developers/", ' \
                        '"shares": 23}, {"url": "http://addnow.com/2014/12/agile-vs-waterfall-method/", ' \
                        '"shares": 725}, {"url": "http://addnow.com/2014/12/importance-of-branding-ux-ui-software-development/", ' \
                        '"shares": 8236}, {"url": "http://addnow.com/2014/10/programmers/", "shares": 826}, ' \
                        '{"url": "http://addnow.com/2014/10/hiring-process/", "shares": 269}, ' \
                        '{"url": "http://addnow.com/2014/09/computers/", "shares": 1252}]'
        self.assertEqual(response.content, json_response)
        # referring_searches
        request = self.factory.get('report', data={'site_id': 1, 'collection': 'referring_searches'})
        response = views.reports(request)
        json_response = '[{"searches": 58, "query": "Development"}, ' \
                        '{"searches": 612, "query": "Clearcode"}, ' \
                        '{"searches": 23, "query": "Software House"}, ' \
                        '{"searches": 11273, "query": "Interactive agency"}, ' \
                        '{"searches": 3235, "query": "Carrer in IT"}, ' \
                        '{"searches": 8236, "query": "PHP Developer"}, ' \
                        '{"searches": 725, "query": "Programming"}, ' \
                        '{"searches": 8236, "query": "PHP Developer"}, ' \
                        '{"searches": 826, "query": "SEO"}, ' \
                        '{"searches": 269, "query": "UX Design"}, ' \
                        '{"searches": 1252, "query": "Continuos integration"}]'
        self.assertEqual(response.content, json_response)
        # copied_keywords
        request = self.factory.get('report', data={'site_id': 1, 'collection': 'copied_keywords'})

        response = views.reports(request)
        json_response = '[{"keywords": "Development", "times": 58}, ' \
                        '{"keywords": "Interactive agency", "times": 11273}, ' \
                        '{"keywords": "Carrer in IT", "times": 3235}, ' \
                        '{"keywords": "Coding service", "times": 612}, ' \
                        '{"keywords": "Software House", "times": 23}, ' \
                        '{"keywords": "Programming", "times": 725}, ' \
                        '{"keywords": "PHP Developer", "times": 8236}, ' \
                        '{"keywords": "SEO", "times": 826}, ' \
                        '{"keywords": "UX Design", "times": 269}, ' \
                        '{"keywords": "Continuos integration", "times": 1252}]'
        self.assertEqual(response.content, json_response)
        # top_countries
        request = self.factory.get('report', data={'site_id': 1, 'collection': 'top_countries'})
        response = views.reports(request)
        json_response = '[{"id": "NZ", "viral": 2, "clicks": 826, ' \
                        '"shares": 58, "country": "New Zealand"}, ' \
                        '{"id": "US", "viral": 62, "clicks": 25273, ' \
                        '"shares": 11273, "country": "United States"}, ' \
                        '{"id": "AU", "viral": 9, "clicks": 10264, ' \
                        '"shares": 3235, "country": "Australia"}, ' \
                        '{"id": "UK", "viral": 5, "clicks": 2746, ' \
                        '"shares": 612, "country": "United Kingdom"}, ' \
                        '{"id": "UK", "viral": 1, "clicks": 127, ' \
                        '"shares": 23, "country": "United Kingdom"}, ' \
                        '{"id": "BR", "viral": 7, "clicks": 5273, ' \
                        '"shares": 725, "country": "Brazil"}, ' \
                        '{"id": "CA", "viral": 21, "clicks": 17274, ' \
                        '"shares": 8236, "country": "Canada"}, ' \
                        '{"id": "AR", "viral": 3, "clicks": 1742, ' \
                        '"shares": 826, "country": "Argentina"}, ' \
                        '{"id": "MX", "viral": 4, "clicks": 742, ' \
                        '"shares": 269, "country": "Mexico"}, ' \
                        '{"id": "IN", "viral": 12, "clicks": 4242, ' \
                        '"shares": 1252, "country": "India"}]'
        self.assertEqual(response.content, json_response)
        # the same but for site_id=2
        # event_source_all
        request = self.factory.get('report', data={'site_id': 2, 'collection': 'event_source_all'})

        response = views.reports(request)
        json_response = '[{"clicks": 34, "shares": 789, "label": "googlePlus"}, ' \
                        '{"clicks": 206, "shares": 1200, "label": "facebook"}, ' \
                        '{"clicks": 93, "shares": 543, "label": "twitter"}, ' \
                        '{"clicks": 57, "shares": 123, "label": "pinterest"}, ' \
                        '{"clicks": 38, "shares": 235, "label": "linkedin"}, ' \
                        '{"clicks": 0, "shares": 5, "label": "other"}]'
        self.assertEqual(response.content, json_response)
        # event_tool_all
        request = self.factory.get('report', data={'site_id': 2, 'collection': 'event_tool_all'})

        response = views.reports(request)
        json_response = '[{"clicks": 765, "shares": 345, "label": "copy-paste"}, ' \
                        '{"clicks": 871, "shares": 45, "label": "sharing-buttons"}, ' \
                        '{"clicks": 91, "shares": 5, "label": "address-bar"}]'
        self.assertEqual(response.content, json_response)
        # event_month
        request = self.factory.get('report', data={'site_id': 2, 'collection': 'event_month'})

        response = views.reports(request)
        json_response = '[{"clicks": 34, "shares": 13, "month": 1401}, ' \
                        '{"clicks": 56, "shares": 17, "month": 1402}, ' \
                        '{"clicks": 45, "shares": 19, "month": 1403}, ' \
                        '{"clicks": 56, "shares": 18, "month": 1404}, ' \
                        '{"clicks": 56, "shares": 15, "month": 1405}, ' \
                        '{"clicks": 30, "shares": 25, "month": 1406}, ' \
                        '{"clicks": 87, "shares": 35, "month": 1407}, ' \
                        '{"clicks": 56, "shares": 98, "month": 1408}, ' \
                        '{"clicks": 65, "shares": 1, "month": 1409}, ' \
                        '{"clicks": 65, "shares": 5, "month": 1410}, ' \
                        '{"clicks": 45, "shares": 1, "month": 1411}, ' \
                        '{"clicks": 25, "shares": 1, "month": 1412}, ' \
                        '{"clicks": 87, "shares": 0, "month": 1501}, ' \
                        '{"clicks": 5, "shares": 5, "month": 1502}]'
        self.assertEqual(response.content, json_response)
        # event_url_all
        request = self.factory.get('report', data={'site_id': 2, 'collection': 'event_url_all'})

        response = views.reports(request)
        json_response = '[{"url": "http://demo.com/contact/", "clicks": 343, "shares": 343, "title": "Contact"}, ' \
                        '{"url": "http://demo.com/team/", "clicks": 234, "shares": 345, "title": "Team"}, ' \
                        '{"url": "http://demo.com/labs/", "clicks": 34, "shares": 75, "title": "Labs"}, ' \
                        '{"url": "http://demo.com/pricing/", "clicks": 633, "shares": 467, "title": "Pricing"}, ' \
                        '{"url": "http://demo.com/product/", "clicks": 34, "shares": 675, "title": "Product"}, ' \
                        '{"url": "http://demo.com/vision/", "clicks": 34, "shares": 75, "title": "Vision"}, ' \
                        '{"url": "http://demo.com/blog/title1/", "clicks": 834, "shares": 275, "title": "Title 1"}, ' \
                        '{"url": "http://demo.com/blog/title2/", "clicks": 34, "shares": 12, "title": "Tile 2"}, ' \
                        '{"url": "http://demo.com/blog/title3/", "clicks": 53, "shares": 25, "title": "Title 3"}, ' \
                        '{"url": "http://demo.com/blog/title4/", "clicks": 3324, "shares": 2375, "title": "Title 4"}, ' \
                        '{"url": "http://demo.com/blog/title4/", "clicks": 334, "shares": 675, "title": "Title 5"}, ' \
                        '{"url": "http://demo.com/opt-out/", "clicks": 0, "shares": 0, "title": "Opt-out"}]'
        self.assertEqual(response.content, json_response)
        # referring_domains
        request = self.factory.get('report', data={'site_id': 2, 'collection': 'referring_domains'})

        response = views.reports(request)
        json_response = '[{"url": "http://addnow.com/2014/09/piwik-piwik-pro-trustradius-buyers-guide/", "shares": 581}, ' \
                        '{"url": "http://addnow.com/2014/10/clearcode-featured-agency-post/", "shares": 1273}, ' \
                        '{"url": "http://addnow.com/2014/07/target-engaged-customers/", "shares": 335}, ' \
                        '{"url": "http://addnow.com/2014/07/rejoiner-ecommerce-solution-cart-abandonment/", "shares": 1612}, ' \
                        '{"url": "http://addnow.com/2014/08/hire-right-app-developers/", "shares": 223}, ' \
                        '{"url": "http://addnow.com/2014/12/agile-vs-waterfall-method/", "shares": 75}, ' \
                        '{"url": "http://addnow.com/2014/12/importance-of-branding-ux-ui-software-development/", "shares": 836}, ' \
                        '{"url": "http://addnow.com/2014/10/programmers/", "shares": 8426}, ' \
                        '{"url": "http://addnow.com/2014/10/hiring-process/", "shares": 2619}, ' \
                        '{"url": "http://addnow.com/2014/09/computers/", "shares": 12}]'
        self.assertEqual(response.content, json_response)
        # referring_searches
        request = self.factory.get('report', data={'site_id': 2, 'collection': 'referring_searches'})

        response = views.reports(request)
        json_response = '[{"searches": 158, "query": "Development"}, ' \
                        '{"searches": 2612, "query": "Clearcode"}, ' \
                        '{"searches": 230, "query": "Software House"}, ' \
                        '{"searches": 1273, "query": "Interactive agency"}, ' \
                        '{"searches": 13235, "query": "Carrer in IT"}, ' \
                        '{"searches": 823, "query": "PHP Developer"}, ' \
                        '{"searches": 1725, "query": "Programming"}, ' \
                        '{"searches": 836, "query": "PHP Developer"}, ' \
                        '{"searches": 8426, "query": "SEO"}, ' \
                        '{"searches": 2619, "query": "UX Design"}, ' \
                        '{"searches": 12, "query": "Continuos integration"}]'
        self.assertEqual(response.content, json_response)
        # copied_keywords
        request = self.factory.get('report', data={'site_id': 2, 'collection': 'copied_keywords'})
        response = views.reports(request)
        json_response = '[{"keywords": "Development", "times": 581}, ' \
                        '{"keywords": "Interactive agency", "times": 1273}, ' \
                        '{"keywords": "Carrer in IT", "times": 335}, ' \
                        '{"keywords": "Coding service", "times": 1612}, ' \
                        '{"keywords": "Software House", "times": 223}, ' \
                        '{"keywords": "Programming", "times": 75}, ' \
                        '{"keywords": "PHP Developer", "times": 836}, ' \
                        '{"keywords": "SEO", "times": 8426}, ' \
                        '{"keywords": "UX Design", "times": 2619}, ' \
                        '{"keywords": "Continuos integration", "times": 12}]'
        self.assertEqual(response.content, json_response)
        # top_countries
        request = self.factory.get('report', data={'site_id': 2, 'collection': 'top_countries'})

        response = views.reports(request)
        json_response = '[{"id": "NZ", "viral": 3, "clicks": 2826, "shares": 581, "country": "New Zealand"}, ' \
                        '{"id": "US", "viral": 26, "clicks": 5273, "shares": 1273, "country": "United States"}, ' \
                        '{"id": "AU", "viral": 11, "clicks": 1264, "shares": 335, "country": "Australia"}, ' \
                        '{"id": "UK", "viral": 5, "clicks": 2746, "shares": 1612, "country": "United Kingdom"}, ' \
                        '{"id": "UK", "viral": 1, "clicks": 1127, "shares": 223, "country": "United Kingdom"}, ' \
                        '{"id": "BR", "viral": 7, "clicks": 273, "shares": 75, "country": "Brazil"}, ' \
                        '{"id": "CA", "viral": 21, "clicks": 1274, "shares": 836, "country": "Canada"}, ' \
                        '{"id": "AR", "viral": 3, "clicks": 11742, "shares": 8326, "country": "Argentina"}, ' \
                        '{"id": "MX", "viral": 4, "clicks": 6742, "shares": 2619, "country": "Mexico"}, ' \
                        '{"id": "IN", "viral": 12, "clicks": 242, "shares": 12, "country": "India"}]'
        self.assertEqual(response.content, json_response)
