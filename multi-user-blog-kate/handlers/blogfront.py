import os
import re
import random
import hashlib
import hmac
from string import letters

import webapp2
import jinja2

from models.user import User
from bloghandler import BlogHandler
from models.post import Post
from models.commented_person import CommentedPerson

template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

secret = 'kate'

class BlogFront(BlogHandler):
    def get(self):
        if self.user:
            posts = Post.all().order('-created')
            comment = CommentedPerson.all().order('-created')
            self.render('front.html', posts = posts, comment = comment)
        else:
            self.redirect('/signup')
