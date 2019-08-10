# Article Curation API

This API is responsible for downloading, parsing, and caching articles from the web. This API also has endpoints for downloading all of the articles from a RSS feed. A data base is used to cache articles for performance.

## Endpoints

### POST /fetch-article
Takes the URL of an article. 
- The URL is parsed using the python newspaper library. The original Article downloader was extended to allow for downloading articles from webpages that could otherwise not be parsed.
- The text and title of the article are returned along with additional Metadata.


**Request Params**
- article_url

**Sample Response**


### POST /fetch-rss
Takes the URL of the RSS feed.
- The database is checked to see if it contain the RSS feed.
- If that URLs is new thr individual article links are parsed out of the RSS feed.
- 

**Request Params**
- rss_url

**Sample Response**


### POST /download-rss
Takes the URL of the RSS feed.
- The database is checked to see if it contain the RSS feed. Existing RSS feeds are over written while new RSS feeds are created as entries. 
- The individual article links are parsed out of the RSS feed and downloaded.
- The RSS URL is saved in the data base as a key with the corresponding data being the individual analyzed articles containing text with additional metadata.

**Request Params**
- rss_url

**Sample Response**





## Deployment
Google Club Function deployed through serverless framework.

 

