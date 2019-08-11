# Cron Jobs

Used to refresh content and manage the content processing pipeline.
TODO: what used to scheudling?


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




## Deployment
Google Cloud Function deployed through serverless framework.

 

