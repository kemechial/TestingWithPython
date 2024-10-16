from unittest import TestCase
from blog.post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('test','test content')
        self.assertEqual('test', p.title)
        self.assertEqual('test content', p.content)

    def test_json(self):
        p = Post('test','test content')
        #self.assertEqual('test', p.json()['title'])
        #self.assertEqual('test content', p.json()['content'])
        expected = {'title' : 'test','content': 'test content'}
        self.assertDictEqual(expected, p.json())