from google.appengine.ext import db
from user import User
from post import Post
# like a post. each post has data of liked persons.
class LikedPerson(db.Model):
    person = db.ReferenceProperty(User) #not useful?
    post = db.ReferenceProperty(Post)

    @classmethod
    def by_person_post(cls, person, post):
        lp = LikedPerson.all().filter('person =', person).filter('post =', post).get()
        return lp
