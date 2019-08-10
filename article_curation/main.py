from processor import scrape_article
import json

from config import DEV_MODE


def fetch_article(request):
    """
    Takes article link and returns scraped data on article
    :return:
    """

    # Set CORS headers for main requests
    headers = {
        'Content-Type': 'application/json',
        # 'Access-Control-Allow-Origin': 'https://mydomain.com',
        # 'Access-Control-Allow-Credentials': 'true'
    }

    if not DEV_MODE:
        request = request.get_json()
        if not request:
            return ('POST json missing. Check that you are posting json.', 500, headers)

    try:
        url = request["article_url"]
    except (KeyError):
        return ('Missing article_url param', 500, headers)

    article_dicts = scrape_article(url)
    if article_dicts is None:
        return ('Scraping failed for: {0}'.format(url), 500, headers)

    return (json.dumps(article_dicts), 200, headers)

# Local test
# p = fetch_article({
#     'article_url': 'https://techcrunch.com/2019/05/01/alexa-in-skil-purchasing-which-lets-developers-make-money-from-voice-apps-launches-internationally/'
# })
#
# print(p)
