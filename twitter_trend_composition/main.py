import twitter
import setting
from get_trend import getTrend
from generate_tweet import generateTweet

t = twitter.Twitter(
    auth=twitter.OAuth(
        token=setting.TW_TOKEN,
        token_secret=setting.TW_TOKEN_SECRET,
        consumer_key=setting.TW_CONSUMER_KEY,
        consumer_secret=setting.TW_CONSUMER_SECRET
        ))

trends = getTrend(t)
generater = generateTweet()
tweet = generater.generate_tweet(trends.trends)

print(tweet)
t.statuses.update(status=tweet)
