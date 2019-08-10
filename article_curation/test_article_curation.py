import unittest
from unittest.mock import Mock
import json

from processor import scrape_article
import main


class ArticleCurationTestCase(unittest.TestCase):

    def test_article_fetch(self):
        response = scrape_article(
            url='https://www.cnn.com/2019/03/25/us/yale-rescinds-student-admissions-scandal/index.html')

        self.assertGreater(len(response["text"].split()), 150)
        self.assertIn("Yale rescinds", response["title"])
        self.assertIn("http", response["img_url"])

        # Tricky url, tests if the extended newspaper component works
        response = scrape_article(
            url='http://www.physiciansnewsnetwork.com/ximed/study-hospital-physician-vertical-integration-has-little-impact-on-quality/article_257c41a0-3a11-11e9-952b-97cc981efd76.html')

        self.assertGreater(len(response["text"].split()), 150)
        self.assertIn("http", response["img_url"])

    def test_article_fetch_endpoint(self):
        """
        Test the actual endpoint by simulating the request object
        :return:
        """

        data = {
            "article_url": "https://techcrunch.com/2019/05/01/alexa-in-skill-purchasing-which-lets-developers-make-money-from-voice-apps-launches-internationally"
        }
        req = Mock(get_json=Mock(return_value=data), args=data)
        response, code, headers = main.fetch_article(req)

        self.assertEqual(code, 200)
        self.assertGreater(len(json.loads(response)["text"].split()), 150)

        # Testing a bad url, see error message
        data = {
            "article_url": "https://example.com/test123"
        }
        req = Mock(get_json=Mock(return_value=data), args=data)
        response, code, headers = main.fetch_article(req)

        self.assertEqual(code, 500)

    def test_download_rss_endpoint(self):
        data = {
            "rss_url": "http://rss.cnn.com/rss/cnn_topstories.rss"
        }
        req = Mock(get_json=Mock(return_value=data), args=data)

        response, code, headers = main.download_rss(req)

        self.assertEqual(code, 200)
        self.assertGreater(len(json.loads(response)), 1)

    def test_fetch_rss_endpoint(self):
        data = {
            "rss_url": "http://rss.cnn.com/rss/cnn_topstories.rss"
        }
        req = Mock(get_json=Mock(return_value=data), args=data)
        response, code, headers = main.fetch_rss(req)

        self.assertEqual(code, 200)
        self.assertGreater(len(json.loads(response)), 1)

        # Test case when rss not in DB
        data = {
            "rss_url": "http://www.example.com/example.rss"
        }
        req = Mock(get_json=Mock(return_value=data), args=data)
        response, code, headers = main.fetch_rss(req)

        self.assertEqual(code, 404)



    # def test_get_article_dicts_from_rss_cache(self):
    #
    #     start = time.time()
    #     for i in range(1000):
    #         article_dicts = get_article_dicts_from_rss('http://rss.cnn.com/rss/cnn_topstories.rss')
    #
    #     end = time.time()
    #     total_time = end - start
    #
    #     # Make less than 10 sec, so cache works
    #     self.assertLess(total_time, 10)
    #
    # def test_get_article_dicts_from_rss(self):
    #
    #     article_dicts = get_article_dicts_from_rss('http://rss.cnn.com/rss/cnn_topstories.rss')
    #     self.assertGreater(len(article_dicts), 0)
    #
    #     for article in article_dicts:
    #         self.assertIn("http", article["img_url"])
    #
    #         # Make sure title has more than 0 characters
    #         self.assertGreater(len(article["title"]), 0)
