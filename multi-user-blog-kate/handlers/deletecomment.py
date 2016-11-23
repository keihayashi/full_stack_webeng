from google.appengine.ext import db

from bloghandler import BlogHandler
from newpost import blog_key
# delete a comment
class DeleteComment(BlogHandler):
    def post(self):
        if not self.user:
            self.redirect('/login')
        else:
            post_id = self.request.get('post_id')
            key_p = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key_p)
            comment_id = self.request.get('comment_id')
            key_c = db.Key.from_path('CommentedPerson', int(comment_id), parent=post.key())
            comment = db.get(key_c)
            if self.user.key() != comment.person.key():
                self.error(403)
                return
            else:
                comment.delete()
                self.redirect('/blog')
