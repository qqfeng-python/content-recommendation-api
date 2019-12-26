import unittest

from language_processor import LanguageProcessor


class LanguageProcessorTestCase(unittest.TestCase):

    def test_substitute_contractions(self):
        processor = LanguageProcessor()
        result = processor.substitute_contractions("can\'t wouldn\'t mike\'s")
        self.assertEqual(result, "cannot would not mike\'s")

    def test_get_non_stopwords(self):
        processor = LanguageProcessor()
        result = processor.get_non_stopwords(
            "Donald Trump is speaking Mandarin.\n\nThis is happening in the city of Tianjin, about an hours drive south of Beijing, within a gleaming office building that belongs to iFlytek, one of Chinas rapidly rising artificial-intelligence companies.")
        self.assertEqual(result, ['donald',
                                  'trump',
                                  'speaking',
                                  'mandarin',
                                  'happening',
                                  'city',
                                  'tianjin',
                                  'hour',
                                  'drive',
                                  'south',
                                  'beijing',
                                  'gleaming',
                                  'office',
                                  'building',
                                  'belongs',
                                  'iflytek',
                                  'china',
                                  'rapidly',
                                  'rising',
                                  'artificial-intelligence',
                                  'company'])

        processor = LanguageProcessor()
        result = processor.get_non_stopwords(
            "Donald Trump is 最新科技新闻和创业公司信息")
        self.assertEqual(result, ['donald',
                                  'trump'])

    def test_get_noun_phrases(self):

        processor = LanguageProcessor()
        result = processor.get_noun_phrases(
            "Donald Trump is a fan of artificial intelligence 最新科技新闻和创业公司信息")
        self.assertEqual(result, ['donald trump', 'fan', 'artificial intelligence 最新科技新闻和创业公司信息'])

        processor = LanguageProcessor()
        result = processor.get_noun_phrases(
            "Donald Trump is a fan of artificial intelligence research and dogs")
        self.assertEqual(result, ['donald trump', 'fan', 'artificial intelligence', 'dogs'])
