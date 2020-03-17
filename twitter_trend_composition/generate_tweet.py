import random

class generateTweet:
    def __init__(self):
        with open('template.txt', mode='rt', encoding='utf-8') as f:
            self.template= list(f)

    def generate_tweet(self, trends):
        tweet = random.choice(self.template)
        end = []
        for trend in trends:
            if '$$$' not in tweet:
                break
            if trend[0] == '#':
                trend = trend[1:]
            tweet = tweet.replace('$$$', trend, 1)
            end.append('\n#' + trend)
        tweet += '\n'
        for e in end:
            tweet += e
        return tweet
