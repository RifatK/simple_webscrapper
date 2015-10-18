import unittest
import simple_web_scrapper as sw

class TestWebScrapper(unittest.TestCase):

    def setUp(self):
        self.html_string="""<html>
        <body>
        <li>hello1</li>
        <li>hello2</li>
        <li>hello3</li>
        </body></html>
        """



    def test_tag_numbers(self):

        tag_list = sw.get_all_tags_from_html(self.html_string)
        count_summary = sw.get_count_of_each_tag(tag_list)
        assert count_summary['html'] == 1
        assert count_summary['body'] == 1
        assert count_summary['li'] == 3




if __name__ == '__main__':
    unittest.main()
