from abc import ABCMeta, abstractmethod


class TweetRepository(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getTweet(self, **kwargs):
        """
        :param kwargs:
            _id, tweet_id, uid, geoX, geoY, geoThreshold, retctMin
            , retctMax, startTime, endTime, sentimentMin
            , sentimentMax, dtf_oid
        :return: A list of tweets
        """
        return None


class UserRepository(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def getUser(self, user):
        return None