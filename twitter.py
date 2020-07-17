from twitter import Twitter
from twitter import *

t = Twitter(auth=OAuth([Access Token], [Access Token secret], [Consumer Key], Consumer Secret))
pythonTweets = t.search.tweets(q = "#python")
print(pythonTweets)