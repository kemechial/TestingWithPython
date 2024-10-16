from unittest import TestCase
from blog.blog import Blog

class BlogTest(TestCase):
  def test_create_post_in_blog(self):
    b = Blog('test', 'author')
    b.create_post('test post','test content')
    self.assertEqual(len(b.posts),1)
    self.assertDictEqual({'title':'test post','content':'test content'},b.posts[0].json())

  def test_json_no_posts(self):
    b = Blog('test', 'author')
    expected = {'title': 'test',
                'author': 'author',
                'posts':[]
                }
    self.assertDictEqual(expected, b.json())

  def test_json(self):
    b = Blog('test', 'author')
    b.create_post('test post','test content')
    b.create_post('test post2','test content2')

    expected = {'title':'test',
                'author':'author',
                'posts' :
                  [{'title':'test post',
                    'content':'test content'},
                   {'title':'test post2',
                    'content':'test content2'}]}

    self.assertDictEqual(expected, b.json())
