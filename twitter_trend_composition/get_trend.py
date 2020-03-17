import twitter

class getTrend:
    def __init__(self, t):
        self.__woeid = { "日本": 23424856 }
        self.trends = self.get_trend(t)

    def get_trend(self, t):
        for area, wid in self.__woeid.items():
            results = t.trends.place(_id = wid)
            # woeidの現在のトレンドをランキング順に取得
            trends = []
            for location in results:
                for trend in location['trends']:
                    trends.append(trend['name'])
        return trends
