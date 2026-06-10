import os
import webbrowser
from threading import Timer
from myproject import app


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
        start_response('404', [('Content-Type', 'text/plain')])
        return ["The url does not belong to the app.".encode()]

app.wsgi_app = PrefixMiddleware(app.wsgi_app, '/lessonslearnt')

# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    
# def open_browser():
#     webbrowser.open_new("http://127.0.0.1:5000/")

# if __name__ == '__main__':
#     if not os.environ.get("WERKZEUG_RUN_MAIN"):
#         Timer(1, open_browser).start()
#     app.run(debug=True, port=5000)
