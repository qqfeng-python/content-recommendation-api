import requests

# r = requests.post("http://127.0.0.1:5000/summary-related", json={'article_url': 'http://www.physiciansnewsnetwork.com/ximed/study-hospital-physician-vertical-integration-has-little-impact-on-quality/article_257c41a0-3a11-11e9-952b-97cc981efd76.html', 'user_id': 1})
# print(r.status_code, r.reason)
# print(r.text)


# url = 'https://messenger-formatter-dot-graph-intelligence.appspot.com/related?analyzeURL1=https%3A%2F%2Fwww.cnn.com%2F2019%2F03%2F07%2Fhealth%2Ffish-mislabeling-investigation-oceana%2Findex.html&db_id=1'
# print(requests.get(url).json())



# keep the API warm:
while True:
    r = requests.post("https://wyzefind-api-dot-graph-intelligence.appspot.com/summary-related", json={
        'article_url': 'http://www.physiciansnewsnetwork.com/ximed/study-hospital-physician-vertical-integration-has-little-impact-on-quality/article_257c41a0-3a11-11e9-952b-97cc981efd76.html',
        'user_id': 1})
    print(r.status_code, r.reason)
    print(r.text)

    import time
    time.sleep(900)




