import unittest
from processor import scrape_article


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
