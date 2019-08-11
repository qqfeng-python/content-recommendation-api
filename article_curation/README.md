# Article Curation API

This API is responsible for downloading, parsing, and caching articles from the web. This API also has endpoints for downloading all of the articles from a RSS feed. A data base is used to cache articles for performance.

## Endpoints

### POST /fetch_article
Takes the URL of an article. 
- The URL is parsed using the python newspaper library. The original Article downloader was extended to allow for downloading articles from webpages that could otherwise not be parsed.
- The text and title of the article are returned along with additional Metadata.


**Request Params**
- article_url

**Sample Response**
```json
{
    "text": "A year after Amazon opened in-skill purchasing to all Alexa developers in the U.S.can be used for",
    "title": "Alexa in-skill purchasing, which lets developers make money from voice apps, launches internationally – TechCrunch",
    "date": "2019-05-01 00:00:00",
    "img_url": "https://techcrunch.com/wp-content/uploads/2019/05/amazon-echo-alexa.jpg?w=600",
    "url": "https://techcrunch.com/2019/05/01/alexa-in-skill-purchasing-which-lets-developers-make-money-from-voice-apps-launches-internationally"
}
```


### POST /fetch_rss
Takes the URL of the RSS feed.
- The database is checked to see if it contain the RSS feed. RSS feeds must be initially inserted by calling `/download_rss`
- If the URL is not in the DB, 404 returned

**Request Params**
- rss_url

**Sample Response**
```json
[
    {
        "text": "Sample text",
        "title": "Jeffrey Epstein has died by suicide, sources say",
        "date": "None",
        "img_url": "https://cdn.cnn.com/cnnnext/dam/assets/190810090556-jeffrey-epstein-handout-130525-super-tease.jpg",
        "url": "http://rss.cnn.com/~r/rss/cnn_topstories/~3/2ZvWB18lbSg/index.html",
        "summary": "Sample summary"
    },
    {
        "text": "Sample text",
        "title": "Jeffrey Epstein found dead in jail, officials say",
        "date": "None",
        "img_url": "https://cdn.cnn.com/cnnnext/dam/assets/190810090900-jeffrey-epstein-handout-170328-super-tease.jpg",
        "url": "http://rss.cnn.com/~r/rss/cnn_topstories/~3/LxyKWnJeF7Y/jeffrey-epstein-found-dead-new-york-jail-vpx-nr.cnn",
        "summary": "Sample summary"
    }
]
```


### POST /download_rss
Takes the URL of the RSS feed.
- The individual article links are parsed out of the RSS feed and downloaded.
- The RSS URL is saved in the data base as a key with the corresponding data being the individual analyzed articles containing text with additional metadata.
- The urlencoded RSS URL is used as the DB key to the collection of article documents found in the RSS feed.
- Existing RSS feeds are over written

**Request Params**
- rss_url

**Sample Response**
```json
[
    {
        "text": "Sample text",
        "title": "Jeffrey Epstein has died by suicide, sources say",
        "date": "None",
        "img_url": "https://cdn.cnn.com/cnnnext/dam/assets/190810090556-jeffrey-epstein-handout-130525-super-tease.jpg",
        "url": "http://rss.cnn.com/~r/rss/cnn_topstories/~3/2ZvWB18lbSg/index.html",
        "summary": "Sample summary"
    },
    {
        "text": "Sample text",
        "title": "Jeffrey Epstein found dead in jail, officials say",
        "date": "None",
        "img_url": "https://cdn.cnn.com/cnnnext/dam/assets/190810090900-jeffrey-epstein-handout-170328-super-tease.jpg",
        "url": "http://rss.cnn.com/~r/rss/cnn_topstories/~3/LxyKWnJeF7Y/jeffrey-epstein-found-dead-new-york-jail-vpx-nr.cnn",
        "summary": "Sample summary"
    }
]
```




## Deployment
Google Cloud Function deployed through serverless framework.

 

