from google.appengine.ext import db

from bloghandler import BlogHandler
from newpost import blog_key
from models.liked_person import LikedPerson

class Like(BlogHandler):
    def post(self):
        post_id = self.request.get('post_id')
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        if post.author != self.user:
            liked = LikedPerson.by_person_post(self.user, post)
            if liked:
                post.liked_num -= 1
                post.put()
                db.delete(liked.key())
            else:
                post.liked_num += 1
                post.put()
                x = LikedPerson(parent = blog_key(), person = self.user, post = post)
                x.put()
            self.redirect('/blog')
        else:
            self.error(403)
            return
