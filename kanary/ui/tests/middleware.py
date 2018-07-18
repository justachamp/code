from time import sleep


class ArtificialDelay:
    """
    Artificial delay for tests browser.
    """

    def __init__(self):
        self.sleep_time = 0.5

    def process_request(self, request):
        """
        Delayed only XMLHttpRequest requests. So we can emulate saucelabs on
        developer's environment. Yeah, it is hack...
        """
        if request.is_ajax():
            sleep(self.sleep_time)

    def process_response(self, request, response):
        response['X-Chrome-Exponential-Throttling'] = 'disable'
        return response
