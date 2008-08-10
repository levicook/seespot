from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class Index(webapp.RequestHandler):
    def get(self):
        self.redirect("/public/index.html")

def main():
    application = webapp.WSGIApplication([('/', Index)], debug=True)
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
