# main.py
NUMBER_OF_RELATED_ARTICLES = 3


# There are multiple functions for differnt doc2vec models
natural_language_function_base_url = "https://us-central1-graph-intelligence.cloudfunctions.net/{0}"

# graph_url = "http://neo4j:Trebinje66@localhost:7474/db/data/"
GRAPH_URL = "http://neo4j:Trebinje66@35.202.226.197:7474/db/data/"

# article_downloader.py
# If less than 100 tokens retry parsing the article not cleaning dom
retry_article_parse_tokens = 100