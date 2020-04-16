import twitter
import setting
from trend import Trend
from tweetgenerater import tweetGenerator

t = twitter.Twitter(
    auth=twitter.OAuth(
        token=setting.TW_TOKEN,
        token_secret=setting.TW_TOKEN_SECRET,
        consumer_key=setting.TW_CONSUMER_KEY,
        consumer_secret=setting.TW_CONSUMER_SECRET
        ))

trends = Trend(t)
generator = tweetGenerator()
tweet = generator.generate(trends.trends)

print(tweet)
t.statuses.update(status=tweet)
