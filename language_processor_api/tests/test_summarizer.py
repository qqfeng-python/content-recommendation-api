import unittest

from summarizer import Summarizer, SummaryException


class LanguageProcessorTestCase(unittest.TestCase):

    def setUp(self):
        self.test_text = ["""
        Donald Trump is speaking Mandarin.\n\nThis is happening in the city of Tianjin, about an hours drive south of Beijing, within a gleaming office building that belongs to iFlytek, one of Chinas rapidly rising artificial-intelligence companies. Beyond guarded gates, inside a glitzy showroom, the US president is on a large TV screen heaping praise on the Chinese company. Its Trumps voice and face, but the recording is, of course, fakea cheeky demonstration of the cutting-edge AI technology iFlytek is developing.\n\nJiang Tao chuckles and leads the way to some other examples of iFlyteks technology. Throughout the tour, Jiang, one of the companys cofounders, uses another remarkable innovation: a hand-held device that converts his words from Mandarin into English almost instantly. At one point he speaks into the machine, and then grins as it translates: I find that my device solves the communication problem.\n\niFlyteks translator shows off AI capabilities that rival those found anywhere in the world. But it also highlights a big hole in Chinas plan, unveiled in 2017, to be the world leader in AI by 2030. The algorithms inside were developed by iFlytek, but the hardwarethe microchips that bring those algorithms to lifewas designed and made elsewhere. While China manufactures most of the worlds electronic gadgets, it has failed, time and again, to master the production of these tiny, impossibly intricate silicon structures. Its dependence on foreign integrated circuits could potentially cripple its AI ambitions.\n\nHowever, AI itself could change all that. New types of chips are being invented to fully exploit advances in AI, by training and running deep neural networks for tasks such as voice recognition and image processing. These chips handle data in a fundamentally different way from the silicon logic circuits that have defined the cutting edge of hardware for decades. It means reinventing microchips for the first time in ages.\n\nA more advanced chip industry will help China realize its dream of becoming a true technology superpower.\n\nChina wont be playing catch-up with these new chips, as it has done with more conventional chips for decades. Instead, its existing strength in AI and its unparalleled access to the quantities of data required to train AI algorithms could give it an edge in designing chips optimized to run them.\n\nChinas chip ambitions have geopolitical implications, too. Advanced chips are key to new weapons systems, better cryptography, and more powerful supercomputers. They are also central to the increasing trade tensions between the US and China. A successful chip industry would make China more economically competitive and independent. To many, in both Washington and Beijing, national strength and security are at stake.\n\nSilicon visions\n\nOn the outskirts of Wuhan, a sprawling city a few days cruise up the Yangtze from Shanghai, stands a factory that would span several football fields. It belongs to Tsinghua Unigroup, a state-backed microchip manufacturer. By the end of 2019, the factory will be producing silicon wafers that will then be cut into advanced memory chips.\n\nTsinghua Unigroup aims to expand the Wuhan facility to three times its current size, at a total cost of $24 billion. Its developing two similar sites, one along the Yangtze in Nanjing and another further west in Chengdu, at similar cost. They will be the largest and most sophisticated chip factories ever built by a Chinese company.\n\nIts all part of an effort by China to drag its chipmaking industry forward."""]

    def test_summary(self):
        summarizer = Summarizer(self.test_text[0])
        summarizer.parse()

        text = summarizer.summarize()
        keywords = summarizer.keywords()
        key_noun_phrases = summarizer.key_noun_phrases()

        self.assertEqual(text, ['This is happening in the city of Tianjin, about an hours drive south of '
                                'Beijing, within a gleaming office building that belongs to iFlytek, one of '
                                'Chinas rapidly rising artificial-intelligence companies.',
                                'Beyond guarded gates, inside a glitzy showroom, the US president is on a '
                                'large TV screen heaping praise on the Chinese company.',
                                'This is happening in the city of Tianjin, about an hours drive south of '
                                'Beijing, within a gleaming office building that belongs to iFlytek, one of '
                                'Chinas rapidly rising artificial-intelligence companies.',
                                'Beyond guarded gates, inside a glitzy showroom, the US president is on a '
                                'large TV screen heaping praise on the Chinese company.',
                                'However, AI itself could change all that.',
                                'A more advanced chip industry will help China realize its dream of becoming '
                                'a true technology superpower.',
                                'China wont be playing catch-up with these new chips, as it has done with '
                                'more conventional chips for decades.',
                                'Chinas chip ambitions have geopolitical implications, too.',
                                'A successful chip industry would make China more economically competitive '
                                'and independent.'])
        self.assertEqual(keywords, ['chip',
                                    'china',
                                    'ai',
                                    'company',
                                    'iflytek',
                                    'technology',
                                    'algorithm',
                                    'microchip',
                                    'time',
                                    'silicon',
                                    'advanced',
                                    'industry',
                                    'beijing',
                                    'belongs',
                                    'inside'])
        self.assertEqual(key_noun_phrases, ['chinese company',
                                            'tsinghua unigroup',
                                            'donald trump',
                                            'gleaming office building',
                                            'artificial-intelligence companies'])

    def test_dirty_text_summary(self):
        test_text = '最新 科技 http: 新闻和创业 公司信息 ”∆˙∫˚˜ ˜µ∆∫˙© ∆∆˚µ˚' + self.test_text[0]
        summarizer = Summarizer(test_text)
        summarizer.parse()

        text = summarizer.summarize()
        keywords = summarizer.keywords()
        key_noun_phrases = summarizer.key_noun_phrases()

        self.assertEqual(text, ['This is happening in the city of Tianjin, about an hours drive south of '
                                'Beijing, within a gleaming office building that belongs to iFlytek, one of '
                                'Chinas rapidly rising artificial-intelligence companies.',
                                'Beyond guarded gates, inside a glitzy showroom, the US president is on a '
                                'large TV screen heaping praise on the Chinese company.',
                                'This is happening in the city of Tianjin, about an hours drive south of '
                                'Beijing, within a gleaming office building that belongs to iFlytek, one of '
                                'Chinas rapidly rising artificial-intelligence companies.',
                                'Beyond guarded gates, inside a glitzy showroom, the US president is on a '
                                'large TV screen heaping praise on the Chinese company.',
                                'However, AI itself could change all that.',
                                'A more advanced chip industry will help China realize its dream of becoming '
                                'a true technology superpower.',
                                'China wont be playing catch-up with these new chips, as it has done with '
                                'more conventional chips for decades.',
                                'Chinas chip ambitions have geopolitical implications, too.',
                                'A successful chip industry would make China more economically competitive '
                                'and independent.'])
        self.assertEqual(keywords, ['chip',
                                    'china',
                                    'ai',
                                    'company',
                                    'iflytek',
                                    'technology',
                                    'algorithm',
                                    'microchip',
                                    'time',
                                    'silicon',
                                    'advanced',
                                    'industry',
                                    'beijing',
                                    'belongs',
                                    'inside'])
        self.assertEqual(key_noun_phrases, ['chinese company',
                                            'tsinghua unigroup',
                                            'donald trump',
                                            'gleaming office building',
                                            'artificial-intelligence companies'])


    def test_empty_summary(self):

        def test(test_text):
            summarizer = Summarizer(test_text)
            summarizer.parse()

            text = summarizer.summarize()
            keywords = summarizer.keywords()

        self.assertRaises(SummaryException, test, '123')
        self.assertRaises(SummaryException, test, '')
        self.assertRaises(SummaryException, test, '最新 科技 http: 新闻和创业 公司信息 ”∆˙∫˚')