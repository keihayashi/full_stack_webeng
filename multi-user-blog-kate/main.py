import os
import re
import random
import hashlib
import hmac
from string import letters

import webapp2
import jinja2

from google.appengine.ext import db

# import models
from models.commented_person import CommentedPerson
from models.liked_person import LikedPerson
from models.post import Post
from models.user import User

# import handlers
from handlers.blogfront import BlogFront
from handlers.comment import Comment
from handlers.delete import Delete
from handlers.edit import Edit
from handlers.like import Like
from handlers.login import Login
from handlers.logout import Logout
from handlers.newpost import NewPost
from handlers.postpage import PostPage
from handlers.register import Register
from handlers.signup import Signup
from handlers.welcome import Welcome

app = webapp2.WSGIApplication([
    ('/blog/?', BlogFront),
    ('/blog/([0-9]+)', PostPage),
    ('/blog/newpost', NewPost),
    ('/signup', Register),
    ('/welcome', Welcome),
    ('/login', Login),
    ('/logout', Logout),
    ('/like', Like),
    ('/delete', Delete),
    ('/edit/([0-9]+)', Edit),
    ('/comment', Comment)
], debug=True)
