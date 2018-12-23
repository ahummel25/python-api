class LoggerMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print('---------------')
        print('Request type {0}'.format(environ['REQUEST_METHOD']))
        print('---------------')
        return self.app(environ, start_response)