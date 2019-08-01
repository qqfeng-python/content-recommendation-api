from article_processor import fetch_article

import feedparser
import cachetools.func


# Cache for 3 hours
@cachetools.func.ttl_cache(ttl= 60 * 60 * 3, maxsize=250)
def rss_to_article_dicts(rss_link, max_articles=5):
    """
    Takes the rss link, parses articles from it and gets the article dict for each link in the rss feed
    :param rss_link:
    :return:
    """

    feed = feedparser.parse(rss_link)
    article_dicts = []

    for entry in feed['entries'][:max_articles]:
        article = fetch_article(entry['links'][0]['href'])

        # First n sentences + remove newlines
        article['summary'] = ". ".join(article['text'].split('.')[:6]).replace("\n", " ")
        article_dicts.append(article)

    return article_dicts


def get_article_dicts_from_rss(rss_link):
    """
    Uses cache to stores the rss_link and article dicts for n hours
    :param rss_link:
    :return:
    """

    article_dicts = rss_to_article_dicts(rss_link)
    return article_dicts