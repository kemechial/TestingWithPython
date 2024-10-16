from unittest import TestCase
from blog.blog import Blog
from blog.post import Post

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('title', 'author')
        self.assertEqual('title', b.title)
        self.assertEqual('author', b.author)
        self.assertListEqual([], b.posts)
        self.assertEqual(0, len(b.posts))

    def test_repr(self):
        b = Blog('title', 'author')
        #self.assertEqual(b.__repr__(), \
        #f"{b.title} by {b.author}" + " (" + str(len(b.posts)) + " posts)")
        self.assertEqual(b.__repr__(), "title by author (0 posts)")

    def test_repr_multiple_posts(self):
        b=Blog('test', 'author')
        b.posts = ['test1','test2']
        b2 = Blog("test2","author2")
        b2.posts = ["one"]
        self.assertEqual(b.__repr__(),\
                "test by author (2 posts)")
        self.assertEqual(b2.__repr__(), "test2 by author2 (1 post)")
