from google.appengine.ext import db

from bloghandler import BlogHandler
from newpost import blog_key
from models.commented_person import CommentedPerson


class Comment(BlogHandler):
    def post(self):
        if not self.user:
            self.redirect('/login')
        else:
            post_id = self.request.get('post_id')
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            comment = self.request.get('comment_content')
            if comment:
                c = CommentedPerson(parent=post.key(), person=self.user,
                                    post=post, content=comment)
                c.put()
            self.redirect('/blog')
