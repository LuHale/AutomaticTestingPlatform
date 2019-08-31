class SaveResultMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print(request)
        response = self.get_response(request)
        print('*'*30, '中间件', response)

        return response