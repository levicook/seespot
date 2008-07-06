from cgi import escape
from google.appengine.ext import db
from google.appengine.ext import webapp
import random
import wsgiref.handlers


class Blog(db.Model):
  name = db.StringProperty(multiline=False)
  desc = db.StringProperty(multiline=True)


class List(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'
    out = self.response.out
    out.write('<html><body>')
    out.write('<a href="/blogs/new">New<a>')
    out.write('<dl>')
    for blog in db.GqlQuery("SELECT * FROM Blog"):
      out.write('<dt><a href="/blogs/view/%s">%s&nbsp;</a></dt>' % (blog.key(), escape(blog.name)))
      out.write('<dd>%s</dd>' % escape(blog.desc))
    out.write('</dl>')
    out.write('</body></html>')


class New(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write("""
      <html>
        <body>
          <form action="/blogs/save" method="post">
            <input type="text" name="name" value="" /><br/>
            <textarea name="desc" rows="3" cols="60"></textarea><br/>
            <input name="action" type="submit" value="Save">&nbsp;
            <input name="action" type="submit" value="Cancel">
          </form>
        </body>
      </html>""")
    pass


class Save(webapp.RequestHandler):
  def post(self):
    blog = Blog()
    blog.name = self.request.get('name')
    blog.desc = self.request.get('desc')
    blog.put()
    self.redirect('/blogs/view/%s' % blog.key())


class View(webapp.RequestHandler):
  def get(self, key):
    blog = db.get(key)
    self.response.headers['Content-Type'] = 'text/html'
    out = self.response.out
    out.write('<html><body>')
    out.write('<a href="/blogs">List<a>&nbsp;')
    out.write('<a href="/blogs/new">New<a>&nbsp;')
    out.write('<a href="/blogs/delete/%s">Delete<a>' % blog.key())
    out.write('<dl>')
    out.write('<dt><a href="/blogs/view/%s">%s&nbsp;</a></dt>' % (blog.key(), escape(blog.name)))
    out.write('<dd>%s</dd>' % escape(blog.desc))
    out.write('</dl>')
    out.write('</body></html>')


class Delete(webapp.RequestHandler):
  def get(self, key):
    db.get(key).delete()
    self.redirect('/blogs/')


def main():
  application = webapp.WSGIApplication([
    (r'/blogs/?', List),
    (r'/blogs/new', New),
    (r'/blogs/save', Save),
    (r'/blogs/view/(.*)', View),
    (r'/blogs/delete/(.*)', Delete),
    ],debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()


