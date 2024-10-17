import builtins
from unittest import TestCase
import blog.app as app
from unittest.mock import patch
from blog.blog import Blog


class AppTest(TestCase):
    def test_menu_input(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_call_print_blogs(self):
        with patch("blog.app.print_blogs") as mocked_print_blogs:
            with patch('builtins.input', return_value = 'q'):
              app.menu()
              mocked_print_blogs.assert_called()

    def test_print_blogs(self):
        blog = Blog('test', 'author')
        app.blogs = {'test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("name: test - blog: test by author (0 posts)")