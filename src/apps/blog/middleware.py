class AmpMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.es_amp = False
        if '/amp/' in request.path:
            request.es_amp = True
        response = self.get_response(request)
        return response
