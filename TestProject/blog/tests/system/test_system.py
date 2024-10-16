import builtins
from unittest import TestCase
import blog.app as app
from unittest.mock import patch
from blog.blog import Blog


class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('test', 'author')
        app.blogs = {'test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("name: test - blog: test by author (0 posts)")
