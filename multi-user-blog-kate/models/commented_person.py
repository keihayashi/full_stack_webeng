from google.appengine.ext import db
from user import User
from post import Post

# comment a post
class CommentedPerson(db.Model):
    person = db.ReferenceProperty(User) #not useful?
    post = db.ReferenceProperty(Post)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    @classmethod
    def by_post(cls, post):
        cp = LikedPerson.all().filter('post =', post).get()
        return cp
