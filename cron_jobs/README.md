# Cron Jobs

Used to refresh content and manage the content processing pipeline.

Cron jobs are deployed as cloud functions which are invoked by the cloud scheduler (GCP).


## Endpoints

### GET /update_rss_articles
Invoked by a GET request taking no parameters.
- All of the current RSS feeds are fetched from the database.
- The download_rss endpoint is used to update each of the RSS feeds with new articles.
- RSS feeds that dont' update are tried again
- A report of the update along with the queue of the failed RSS feeds is returned.

**Request Params**
- None

**Sample Response**
```json
{
    "report": "Total RSS Feeds: 4 Total Failed: 0 Total Time to Update: 29.32970881462097 Average Time to update: 7.332427203655243",
    "failed_queue": []
}
```

## Deployment
Google Cloud Function deployed through serverless framework.


## Next Steps
- Add testing
- Make update_rss calls asynchronous or function will timeout
- Add Zapier integration to send message if error




 

