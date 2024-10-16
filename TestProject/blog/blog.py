from blog.post import Post
#from post import Post

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
       # return f"{self.title} by {self.author}" + \
       #    " (" + str(len(self.posts)) + " posts)"
       return "{} by {} ({} post{})".format(self.title,self.author, len(self.posts), 's' if len(self.posts)!=1 else '')

    def create_post(self, title, content):
       self.posts.append(Post(title,content))

    def json(self):
      return {
                'title': self.title,
                'author': self.author,  # can leave a comma here
                'posts': [post.json() for post in self.posts]
             }