import unittest
import time

from article_curation import get_article_dicts_from_rss


class ArticleCurationTestCase(unittest.TestCase):

    def test_get_article_dicts_from_rss_cache(self):

        start = time.time()
        for i in range(1000):
            article_dicts = get_article_dicts_from_rss('http://rss.cnn.com/rss/cnn_topstories.rss')

        end = time.time()
        total_time = end - start

        # Make less than 10 sec, so cache works
        self.assertLess(total_time, 10)

    def test_get_article_dicts_from_rss(self):

        article_dicts = get_article_dicts_from_rss('http://rss.cnn.com/rss/cnn_topstories.rss')
        self.assertGreater(len(article_dicts), 0)

        for article in article_dicts:
            self.assertIn("http", article["img_url"])

            # Make sure title has more than 0 characters
            self.assertGreater(len(article["title"]), 0)



