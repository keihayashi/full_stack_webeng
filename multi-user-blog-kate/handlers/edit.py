from google.appengine.ext import db

from bloghandler import BlogHandler
from newpost import blog_key


# edit a post
class Edit(BlogHandler):
    def post(self, post_id):
        if self.user:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)

            if self.user.key() != post.author.key():
                self.error(403)
                return
            else:
                subject = self.request.get('subject')
                content = self.request.get('content')

                if subject and content:
                    post.subject = subject
                    post.content = content
                    post.put()
                    self.redirect('/blog/%s' % str(post.key().id()))
                else:
                    error = "subject and content, please!"
                    self.render("newpost.html", subject=subject,
                                content=content, error=error, edit=True)
        else:
            self.redirect('/login')

    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        if post.subject and post.content:
            self.render("newpost.html", subject=post.subject,
                        content=post.content, edit=True,
                        post_id=post_id, p=post)
