import json
import requests
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from config import KEYFILE, DOWNLOAD_RSS_URL

# Set CORS headers for main requests
headers = {
    'Content-Type': 'application/json',
    # 'Access-Control-Allow-Origin': 'https://mydomain.com',
    # 'Access-Control-Allow-Credentials': 'true'
}


def error_message(message, code):
    """
    Used to return the JSON body, error code, and headers of an error message.

    Formats text error messages into JSON format. https://stackoverflow.com/questions/12806386/standard-json-api-response-format
    :param message:
    :return:
    """

    # The three values to be returned as response from Google Cloud Function
    return ({
                "error": {
                    "code": code,
                    "message": message
                }
            }, code, headers)


def update_rss_articles(request):
    """
    Cron Job updates cached RSS feeds and their scraped articles in DB
    :return:
    """

    # Check if app already initialized will fail if apps with same name initialized twice
    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate(KEYFILE)
        firebase_admin.initialize_app(cred)

    db = firestore.client()

    # Get all RSS links from DB
    rss_feeds = db.collection("rss_feeds").get()
    rss_feeds = [article.to_dict()['rss_feed'] for article in rss_feeds]

    # Try again for RSS feeds that could not be refreshed
    failed_queue = []
    times = []

    for feed in rss_feeds:

        start_time = time.time()
        r = requests.post(DOWNLOAD_RSS_URL, json={'rss_url': feed})

        # Measure how long it takes to refresh RSS URLs in the DB
        times.append(time.time() - start_time)

        if r.status_code == 500:
            failed_queue.append(feed)

    # Try refreshing the feeds that failed again
    for feed in failed_queue:
        r = requests.post(DOWNLOAD_RSS_URL, json={'rss_url': feed})

        # If worked this time, remove from failed queue
        if r.status_code == 200:
            failed_queue.remove(feed)

    report = f"Total RSS Feeds: {len(rss_feeds)} Total Failed: {len(failed_queue)} Total Time to Update: {sum(times)} Average Time to update: {sum(times) / len(times)}"

    return (json.dumps({
        'report': report,

        # Return list of RSS feeds that could not be refreshed
        'failed_queue': failed_queue
    }), 200, headers)


# print(update_rss_articles(123))
