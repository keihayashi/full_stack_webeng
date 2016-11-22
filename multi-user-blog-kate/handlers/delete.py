from google.appengine.ext import db

from bloghandler import BlogHandler
from newpost import blog_key
# delete a post
class Delete(BlogHandler):
    def post(self):
        post_id = self.request.get('post_id')
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        post.delete()
        self.redirect('/blog')
