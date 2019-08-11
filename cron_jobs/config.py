# Allows for easier debugging and unit testing. For example in dev mode functions don't expect a Flask request input.
DEV_MODE = False

KEYFILE = 'keyfile.json'

BASE_URL = 'https://us-central1-media-voice-applications.cloudfunctions.net'
DOWNLOAD_RSS_URL = "{0}/download_rss".format(BASE_URL)