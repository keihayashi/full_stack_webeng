from bloghandler import BlogHandler
# logout
class Logout(BlogHandler):
    def get(self):
        self.logout()
        self.redirect('/signup')
