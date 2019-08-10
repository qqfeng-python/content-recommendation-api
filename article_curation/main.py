from processor import scrape_article, store_article_dicts_from_rss, get_article_dicts_from_rss
import json

from config import DEV_MODE

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


def fetch_article(request):
    """
    Takes article link and returns scraped data on article
    :return:
    """

    if not DEV_MODE:
        request = request.get_json()
        if not request:
            return error_message('POST json missing. Check that you are posting json.', 500)

    try:
        url = request["article_url"]
    except (KeyError):
        return error_message('Missing article_url param', 500)

    article_dict = scrape_article(url)
    if article_dict is None:
        return error_message('Failed scraping article: {0}'.format(url), 500)

    return (json.dumps(article_dict), 200, headers)


def download_rss(request):
    """
    Takes rss link and and enters scraped article data into DB
    :return:
    """

    if not DEV_MODE:
        request = request.get_json()
        if not request:
            return error_message('POST json missing. Check that you are posting json.', 500)

    try:
        url = request["rss_url"]
    except (KeyError):
        return error_message("Missing rss_url param", 500)

    article_dicts = store_article_dicts_from_rss(url)
    if not article_dicts:
        return error_message("Failure scraping and saving articles from: {0}".format(url), 500)

    return (json.dumps(article_dicts), 200, headers)


def fetch_rss(request):
    """
    Takes rss link and and enters scraped article data into DB
    :return:
    """

    if not DEV_MODE:
        request = request.get_json()
        if not request:
            return error_message('POST json missing. Check that you are posting json.', 500)

    try:
        url = request["rss_url"]
    except (KeyError):
        return error_message("Missing rss_url param", 500)

    article_dicts = get_article_dicts_from_rss(url)
    if not article_dicts:
        return error_message("Failure fetching RSS from DB: {0}".format(url), 404)

    return (json.dumps(article_dicts), 200, headers)

# Local testing with DEV_MODE
# p = fetch_article({
#     'article_url': 'https://techcrunch.com/2019/05/01/alexa-in-skil-purchasing-which-lets-developers-make-money-from-voice-apps-launches-internationally/'
# })
#
# print(p)

# p = download_rss({
#     'rss_url': 'https://danamic.org/music/rss/'
# })
# print(p)

# p = fetch_rss({
#     'rss_url': 'https://danamic.org/music/rss/'
# })
# print(p)
