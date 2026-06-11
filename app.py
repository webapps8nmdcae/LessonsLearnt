from myproject import app
from flask import Flask, redirect
class PrefixMiddleware(object):

    def __init__(self, app, *prefix):
        self.app = app
        self.prefixes = []

        for i in prefix:
            self.prefixes.append(i)

    def __call__(self, environ, start_response):
        for i in self.prefixes:
            if environ['PATH_INFO'].startswith(i):
                environ['PATH_INFO'] = environ['PATH_INFO'][len(i):]
                environ['SCRIPT_NAME'] = i
                return self.app(environ, start_response)

        # Instead of a strict 404, let Flask handle the original request
        return self.app(environ, start_response)


app.wsgi_app = PrefixMiddleware(app.wsgi_app, '/LessonsLearnt')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
