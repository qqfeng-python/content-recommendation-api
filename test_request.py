import requests
import json

# r = requests.post("http://127.0.0.1:5000/rss-content", json={'rss_url': 'https://us12.campaign-archive.com/rss-content/feed?u=4d28858ff8aaf5bba521824ba&id=f42d838542'})
# print(r.status_code, r.reason)
# print(r.text)


# url = 'https://messenger-formatter-dot-graph-intelligence.appspot.com/rss-content/related?analyzeURL1=https%3A%2F%2Fwww.cnn.com/rss-content%2F2019%2F03%2F07%2Fhealth%2Ffish-mislabeling-investigation-oceana%2Findex.html&db_id=1'
# print(requests.get(url).json())


# keep the API warm:
while True:

    try:
        r = requests.post("https://wyzefind-api-dot-graph-intelligence.appspot.com/rss-content",
                          json={'rss_url': 'https://danamic.org/category/music/rss'})

        print(r.status_code, r.reason)
        print(json.dumps(r.json(), indent=2))

    except:
        print("Oops something went wrong")

    import time
    time.sleep(120)
