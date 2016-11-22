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

def render_post(response, post):
    response.out.write('<b>' + post.subject + '</b><br>')
    response.out.write(post.content)

def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name)

# register stuff
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

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
