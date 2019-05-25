import unittest
import json

from article_processor import download, fetch_article, article_processor


class ArticleProcessorTestCase(unittest.TestCase):

    def test_article_fetch(self):
        response = fetch_article(
            url='http://www.physiciansnewsnetwork.com/ximed/study-hospital-physician-vertical-integration-has-little-impact-on-quality/article_257c41a0-3a11-11e9-952b-97cc981efd76.html')

        self.assertGreater(len(response["text"].split()), 150)
        self.assertIn("http", response["img_url"])

        response = fetch_article(
            url='https://www.cnn.com/2019/03/25/us/yale-rescinds-student-admissions-scandal/index.html')

        self.assertGreater(len(response["text"].split()), 150)
        self.assertIn("Yale rescinds", response["title"])
        self.assertIn("http", response["img_url"])

    def test_article_processor(self):
        response, is_valid = article_processor(
            url='http://www.physiciansnewsnetwork.com/ximed/study-hospital-physician-vertical-integration-has-little-impact-on-quality/article_257c41a0-3a11-11e9-952b-97cc981efd76.html',
            processor_id="language-processor-health")

        self.assertEqual(len(response['embedding']), 250)

        del response['embedding']

        self.assertGreater(len(response["text"].split()), 150)

        self.assertIn(" Hospital-Physician Vertical", response["title"])
        self.assertIn("http", response["img_url"])
