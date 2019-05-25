import requests
import json

r = requests.post("http://127.0.0.1:5000/rss-content", json={'rss_url': 'http://rss.cnn.com/rss/cnn_topstories.rss'})
print(r.status_code, r.reason)
print(r.text)


# url = 'https://messenger-formatter-dot-graph-intelligence.appspot.com/related?analyzeURL1=https%3A%2F%2Fwww.cnn.com%2F2019%2F03%2F07%2Fhealth%2Ffish-mislabeling-investigation-oceana%2Findex.html&db_id=1'
# print(requests.get(url).json())



# # keep the API warm:
# while True:
#     r = requests.post("https://wyzefind-api-dot-graph-intelligence.appspot.com/summary", json={
#         'article_url': 'https://pilotonline.com/entertainment/festivals/article_10a31f32-75b8-11e9-83de-af3cdb515609.html',
#         'user_id': 1, 'processor_id': 'language-processor-health'})
#     print(r.status_code, r.reason)
#     print(json.dumps(r.json(), indent=2))
#
#     import time
#     time.sleep(900)




