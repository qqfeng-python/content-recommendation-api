# Wyzefind Core API

This API is responsible for powering the chatbot, voice, and web applications. It powers features such as summary, related content, and explainable related content. This API is responsible for interacting with the neo4j database which hosts the content graph.

The main goal is to have as much logic as possible live on the Wyzefind Core API in order for easily porting to new integrations.


## Endpoints

### POST /explore
Takes a url of an article in the graph and finds the corresponding title.
- Finds the most similar articles to that title
- Explains connections from original article to related articles in terms of concepts, entities, and topics.

**Request Params**
- article_url (Must be article in the graph)

Returns a JSON response with the processed original article as well as data on the related articles.

**Sample Response**



### POST /summary
Route takes the url of an article
- Downloads article
- Processed article using the language-processor api

**Request Params**
- article_url (Not required to be in graph)
- processor_id (The id of the cloud function used to process the text, different cloud functions for different Gensim Doc2Vec models. Ie: Health, Tech ...)

Returns JSON containing the summary.

**Sample Response**


### POST /summary-related:
Route takes the url of an article
- Downloads article
- Finds most similar articles by embedding

**Request Params**
- article_url (Not required to be in graph)
- processor_id

Return JSON containing data on processed original article as well as top 3 related articles.

**Sample Response**



## Deployment
This microservice is deployed on App engine standard. The service must be deployed on F2 instances, F1 runs out of memory.


## Issues
- Service costs ~$135 / month to deploy on app engine, issue with to many instances?
- The URL of the Compute Engine Neo4j graph can change if instance is shutdown, need to update graph_url variable.
- The newspaper library is modified due to an issue with the parsing. article_downloader.py contains code to extend the orignal cleaner class. The newspaper Library contains a cleaner class which causes an issue with some websites where the text cannot be extracted. This issue was solved by extending the original cleaner class and removing the cleaning feature when no text is extracted the first time.

## Next Steps
- [ ] Fix problem where spinning up new instances since will not have the same RSS feed caches. All instances must read the pre-parsed RSS feeds from a DB which can be updated every x hours with a cron server.


