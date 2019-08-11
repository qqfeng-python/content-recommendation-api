import newspaper
import feedparser
import urllib.parse

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from article_parser import Article
from config import KEYFILE

# If less than 100 tokens retry parsing the article not cleaning dom
retry_article_parse_tokens = 100


def download(url, clean_doc=True):
    """
    Tries to download + parse the article using newspaper
    :param url:
    :return:
    """

    article = Article(url)
    is_valid = True

    try:
        article.download()
        article.parse(clean_doc=clean_doc)
    except newspaper.article.ArticleException:
        print("Download error: {0}".format(url))
        is_valid = False

    return article, is_valid


def scrape_article(url):
    """
    Downloads the article from URL
    :param url:
    :return:
    """

    article, is_valid = download(url)

    if is_valid:

        # Retry downloading article without cleaning
        if len(article.text.split()) < retry_article_parse_tokens:
            article, is_valid = download(url, clean_doc=False)

        title = article.title
        text = article.text
        date = article.publish_date
        img = article.top_image

        return {
            'text': text,
            'title': title,
            'date': str(date),
            'img_url': img,
            'url': url,
        }


def rss_to_article_dicts(rss_link, max_articles=5):
    """
    Takes the rss link, parses articles from it and gets the article dict for each link in the rss feed
    :param rss_link:
    :return:
    """

    feed = feedparser.parse(rss_link)
    article_dicts = []

    for entry in feed['entries'][:max_articles]:
        article = scrape_article(entry['links'][0]['href'])

        # First n sentences + remove newlines
        article['summary'] = ". ".join(article['text'].split('.')[:6]).replace("\n", " ")
        article_dicts.append(article)

    return article_dicts


def store_article_dicts_from_rss(rss_link):
    """
    Parses the rss_link and saves the individual articles in the DB
    :param rss_link:
    :return:
    """

    try:
        # Check if app already initialized will fail if apps with same name initialized twice
        if (not len(firebase_admin._apps)):
            cred = credentials.Certificate(KEYFILE)
            firebase_admin.initialize_app(cred)

        db = firestore.client()

        article_dicts = rss_to_article_dicts(rss_link)

        # Create a document with URL encoded RSS link as the key
        encoded = urllib.parse.quote_plus(rss_link)

        rss_docs = db.collection("rss_feeds").document(encoded)
        # Need to add rss_feed property so that rss_feeds collection can be queried for rss_feeds, with no feild (only document) the collection comes back empty
        # Becuase with no feilds considered "virtual document", "This document does not exist and will not appear in queries or snapshots, but identically structured document works"
        rss_docs.set({
            "rss_feed": rss_link
        })

        # Get old titles to delete later
        old_articles = db.collection("rss_feeds").document(encoded).collection('articles').stream()
        old_titles = [article.to_dict()['title'] for article in old_articles]
        new_titles = [article['title'] for article in article_dicts]


        # Add each article_dict as a document in the 'articles' collection with the title as the key
        for article in article_dicts:
            rss_docs.collection('articles').document(article['title']).set(article)

        # Only delete after adding new articles so api will never be queried when DB empty, otherwise if called when refreshing content no articles my come back.
        for old in old_titles:
            if old not in new_titles:
                rss_docs.collection('articles').document(old).delete()


    except Exception:
        return None

    # If documents are successfully saved return the article dict
    return article_dicts


def get_article_dicts_from_rss(rss_link):
    """
    Checks the DB for the rss_link key and returns the list of article_dicts if found
    :param rss_link:
    :return:
    """

    try:
        # Check if app already initialized will fail if apps with same name initialized twice
        if (not len(firebase_admin._apps)):
            cred = credentials.Certificate(KEYFILE)
            firebase_admin.initialize_app(cred)

        db = firestore.client()

        articles = db.collection("rss_feeds").document(urllib.parse.quote_plus(rss_link)).collection(
            'articles').stream()
        article_dicts = [article.to_dict() for article in articles]

    except KeyError:
        return None

    # If documents are successfully saved return the article dict
    return article_dicts
