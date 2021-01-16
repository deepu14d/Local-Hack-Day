# A bot that like tweets automatically based on a keyword.

import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
def lim_handle(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300)    # when we hit error the cursor stops clicking and rest for 300 sec

search_word = 'MLH'
num_of_tweets = 2
for tweet in tweepy.Cursor(api.search, search_word).items(num_of_tweets):
	try:
		tweet.favorite()
		print('I like that tweet')
	except tweepy.TweepError as err:
		print(err.reason)
	except StopIteration:
		break