from google.appengine.ext import db

from bloghandler import BlogHandler
from newpost import blog_key
# delete a post
class Delete(BlogHandler):
    def post(self):
        if not self.user:
            self.redirect('/login')
        else:
            post_id = self.request.get('post_id')
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            if self.user.name != post.author.name:
                self.error(403)
                return
            else:
                post.delete()
                self.redirect('/blog')
