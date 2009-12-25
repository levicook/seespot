_DEBUG = True

import os

from mako.template import Template
from mako.lookup import TemplateLookup

from google.appengine.ext import webapp
import wsgiref.handlers


class BaseHandler(webapp.RequestHandler):

  def base_path(self):
    return self.request.path[:-len(self.__class__.PATH)]

  def render(self, template_name, request_values={}):
    home = os.path.dirname(__file__) 
    lookup = TemplateLookup(directories=[os.path.join(home, 'templates')])
    template = lookup.get_template('%s.mako.html' % template_name)
    template_values = {
      'application_name': self.request.environ['APPLICATION_ID'],
      'base_path': self.base_path(),
      'request': self.request,
      }
    template_values.update(request_values)
    self.response.out.write(template.render(**template_values))


class DefaultHandler(BaseHandler):
  PATH = '/'
  def get(self):
    self.render('helloworld', { 'user': 'Levi' })


if __name__ == '__main__':
  handlers = []
  handlers.append(('.*', DefaultHandler))
  wsgiref.handlers.CGIHandler().run(webapp.WSGIApplication(handlers, debug=_DEBUG))
