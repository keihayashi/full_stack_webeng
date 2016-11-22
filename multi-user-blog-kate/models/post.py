from google.appengine.ext import db
from user import User

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    author = db.ReferenceProperty(User)
    liked_num = db.IntegerProperty()
