

"""
tests for the core.py module
"""

import unittest
from core import *
import requests


class TestProcessHtml(unittest.TestCase):
    """
    tests the ProcessHtml class
    """
    def setUp(self):
        self.html = """
        <div>
            <h1>hello ali</h1>
            <h2>mohsen has got a jet</h2>
            <h2>ali</h2>
        </div>
        <body>
        </body>
        <script src=''></script>
        <script src='#'></script>
        """

    def test_numbers_of_all_tags(self):
        """
        tests the number of the all tags
        """
        html = self.html 
        res = ProcessHtml(html)
        self.assertEqual(res.tags_number, 7)

    def test_number_of_each_tag(self):
        """
        test the number of every tag in the code
        """
        html = self.html
        res = ProcessHtml(html)
        self.assertEqual(res.tags, {'div': 1,
                                    'h1': 1,
                                    'h2': 2,
                                    'body': 1,
                                    'script': 2})

    def test_number_of_the_words_in_html(self):
        """
        this tests the number of any word in the html
        """
        html = self.html
        res = ProcessHtml(html)
        self.assertEqual(res.words_number, 7)

    def test_different_words(self):
        """
        this tests word with different size
        to check whether they found or not
        """

        html = """<p>a ab abc my name expectation
        Pseudopseudohypoparathyroidism 
        Pneumonoultramicroscopicsilicovolcanoconiosis
        </p>"""
        res = ProcessHtml(html)
        self.assertEqual(res.words_number, 7)
        
    def test_number_of_the_repetition_of_words(self):
        """
        this test shows the repetition of the words
        in the html code (tags are not included)
        """ 
        html = "<p>ali</p> <a>ali<a><h2> mohsen jack jack</h2>"
        res = ProcessHtml(html)
        self.assertEqual(res.words, {'ali': 2,
                                     'mohsen': 1,
                                     'jack': 2})



    """
    def test_real_website(self):
        html = requests.get('https://english.stackexchange.com/questions/194468/what-is-the-short-form-for-little-is-it-lil-or-lil').text
        res = ProcessHtml(html)
        print(res.words)
    """
        

    def test_all_the_links_of_a_page(self):
        html = """
        <a href="https://google.com"></a>
        <a href="https://facebook.com"></a>
        <a href="/contact"></a>
        """
        res = ProcessHtml(html)
        self.assertEqual(res.links, ["https://google.com",
                                     "https://facebook.com",
                                     "/contact"])


    def test_finding_the_images_in_a_webpage(self):
        html = """
        <img src="http://ab.com/image1_link.png" alt="face image" />
        <img src="http://ab.com/image2_link.png"  />

        """
        res = ProcessHtml(html)
        self.assertEqual(res.images, 
                        {'http://ab.com/image1_link.png': 'face image',
                        'http://ab.com/image2_link.png': None})

    def test_finding_words_in_bold_tags(self):
        pass





if __name__ == '__main__':
    unittest.main()
