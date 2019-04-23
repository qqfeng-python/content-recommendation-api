import unittest

from article_downloader import Article


class ArticleDownloaderTestCase(unittest.TestCase):

    def test_article(self):
        article = Article(
            url='http://www.physiciansnewsnetwork.com/ximed/study-hospital-physician-vertical-integration-has-little-impact-on-quality/article_257c41a0-3a11-11e9-952b-97cc981efd76.html')
        article.download()

        article.parse(clean_doc=False)

        title = article.title
        text = article.text
        date = article.publish_date

        self.assertEqual(title,
                         "Study: Hospital-Physician Vertical Integration Has Little Impact on Quality of Care; Greater Market Concentration Reduces It")
        self.assertEqual(str(date), 'None')
        self.assertEqual(text.split()[100:105],
                         ['directly', 'in', 'California,', 'Scripps', 'has']
                         )
