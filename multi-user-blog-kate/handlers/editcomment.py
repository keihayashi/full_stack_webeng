from google.appengine.ext import db

from bloghandler import BlogHandler
from newpost import blog_key
# edit a comment
class EditComment(BlogHandler):
    def post(self, post_id, comment_id):
        if self.user:
            key_p = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key_p)
            key_c = db.Key.from_path('CommentedPerson', int(comment_id), parent=post.key())
            comment = db.get(key_c)

            if self.user.key() != comment.person.key():
                self.error(403)
                return
            else:
                content = self.request.get('content')
                if content:
                    comment.content = content
                    comment.put()
                    self.redirect('/blog')
                else:
                    error = "comment content, please!"
                    self.render("editcomment.html", content=content, error=error)
        else:
            self.redirect('/login')

    def get(self, post_id, comment_id):
        key_p = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key_p)
        key_c = db.Key.from_path('CommentedPerson', int(comment_id), parent=post.key())
        comment = db.get(key_c)
        if comment.content:
            self.render("editcomment.html", content = comment.content, edit = True,
                post_id = post_id, comment_id = comment_id, p = post, c = comment)
