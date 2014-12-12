from pymongo import MongoClient
from summerschool.item import *
from summerschool.repository import TweetRepository


class DbConfig(object):
    HOST_NAME = 'localhost'
    PORT = 27071
    DB_NAME = 'twitter'
    TWEET_COL = 'tweets'
    USER_COL = 'users'


class MongoTweetsRepository(TweetRepository):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client[DbConfig.DB_NAME]
        self.tweetCollection = self.db[DbConfig.TWEET_COL]
        self.userCollection = self.db[DbConfig.USER_COL]

    def getAllTweet(self):
        return map(self.toTweet, self.tweetCollection.find({}))

    def getTweet(self, **kwargs):
        """
        :param kwargs:
            _id, tweet_id, uid, geoX, geoY, geoThreshold, retctMin
            , retctMax, startTime, endTime, sentimentMin
            , sentimentMax, dtf_oid
        :return: A list of tweets
        """
        results = []
        first = True
        for key, value in kwargs.iteritems():
            if len(kwargs) <= 0:
                break
            if key == "geoThreshold":
                continue
            if key == "_id":
                if not first:
                    print("Cannot have other query")
                    exit(-1)
                tweet = self.toTweet(self.tweetCollection.find_one({"_id": value}))
                results.append(tweet)
            elif key == "tweet_id":
                if not first:
                    print("Cannot have other query")
                    exit(-1)
                tweet = self.toTweet(self.tweetCollection.find_one({"id": value}))
                results.append(tweet)
            elif key == "uid":
                if first:
                    tweets = map(self.toTweet, self.tweetCollection.find({"uid": value}))
                    results.append(tweets)
                else:
                    results = filter(lambda tweet: tweet.uid == value, results)
            elif key == "geoX":
                if first:
                    tweets = self.getAllTweet()
                    results = tweets
                results = filter(
                    lambda tweet: kwargs["geoX"] - kwargs["geoThreshold"] <= tweet.geo[0] <= kwargs["geoX"] + kwargs[
                        "geoThreshold"], results)
            elif key == "geoY":
                if first:
                    tweets = self.getAllTweet()
                    results = tweets
                results = filter(
                    lambda tweet: kwargs["geoY"] - kwargs["geoThreshold"] <= tweet.geo[1] <= kwargs["geoY"] + kwargs[
                        "geoThreshold"], results)
            elif key == "retctMin":
                if first:
                    tweets = self.getAllTweet()
                    results = tweets
                results = filter(
                    lambda tweet: value <= tweet.retct, results)
            elif key == "retctMax":
                if first:
                    tweets = self.getAllTweet()
                    results = tweets
                results = filter(
                    lambda tweet: tweet.retct <= value, results)
            elif key == "startTime":
                if first:
                    results = map(self.toTweet, self.tweetCollection.find({"pub_time": {"$gte": value}}))
                results = filter(lambda tweet: tweet.pub_time >= value, results)
            elif key == "endTime":
                if first:
                    results = map(self.toTweet, self.tweetCollection.find({"pub_time": {"$lt": value}}))
                results = filter(lambda tweet: tweet.pub_time <= value, results)
            elif key == "sentimentMin":
                if first: results = self.getAllTweet()
                results = filter(lambda tweet: tweet.sentiment>=value, results)
            elif key == "sentimentMax":
                if first: results = self.getAllTweet()
                results = filter(lambda tweet: tweet.sentiment<=value, results)
            elif key == "dtf_oid":
                if first:
                    results = map(self.toTweet, self.tweetCollection.find({"dtf_oid": value}))
                else:
                    results = filter(lambda tweet: tweet.dtf_oid == value, results)
            else:
                print("invalid key values: " + str(key) + " " + str(value))
                exit(-1)

            first = False
        return results


    def toTweet(self, jsonItem):
        print jsonItem
        _id = jsonItem["_id"]
        tweet_id = jsonItem["id"]
        uid = jsonItem["uid"]
        geo = self.parseGeo(jsonItem["geo"]) if 'geo' in jsonItem  else UNKNOWN_VALUE
        retct = int(jsonItem["retct"]) if 'retct' in jsonItem  else UNKNOWN_VALUE
        url = jsonItem["url"] if 'url' in jsonItem  else UNKNOWN_VALUE
        uname = jsonItem["uname"] if 'uname' in jsonItem  else UNKNOWN_VALUE
        image = jsonItem["image"] if 'image' in jsonItem  else UNKNOWN_VALUE
        dtf_s = jsonItem["dtf_s"] if 'dtf_s' in jsonItem  else UNKNOWN_VALUE
        content = jsonItem["content"] if 'content' in jsonItem  else UNKNOWN_VALUE
        pub_time = jsonItem["pub_time"] if 'pub_time' in jsonItem  else UNKNOWN_VALUE
        fet_time = jsonItem["fet_time"] if 'fet_time' in jsonItem  else UNKNOWN_VALUE
        dtf_oid = jsonItem["dtf_oid"] if 'dtf_oid' in jsonItem  else UNKNOWN_VALUE
        sentiment = int(jsonItem["sentiment"]) if 'sentiment' in jsonItem  else UNKNOWN_VALUE
        return Tweet(_id=_id, tweet_id=tweet_id, uid=uid, geo=geo, retct=retct, url=url, uname=uname, image=image,
                     dtf_s=dtf_s, content=content, pub_time=pub_time, fet_time=fet_time, dtf_oid=dtf_oid,
                     sentiment=sentiment)