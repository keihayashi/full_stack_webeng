from google.appengine.ext import db

from bloghandler import BlogHandler
from models.post import Post

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

class NewPost(BlogHandler):
    def get(self):
        self.render("newpost.html")

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            p = Post(parent = blog_key(), subject = subject, content = content, author = self.user.key(), liked_num = 0)
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content, error=error, edit = False)
