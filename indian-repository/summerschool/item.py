UNKNOWN_VALUE = 'SUMMERSCHOOL_UNKNOWN_15959423'


class Tweet(object):
    def __init__(self, _id, tweet_id, uid, geo=UNKNOWN_VALUE, retct=UNKNOWN_VALUE, url=UNKNOWN_VALUE, uname=UNKNOWN_VALUE,
                 image=UNKNOWN_VALUE, dtf_s=UNKNOWN_VALUE, content=UNKNOWN_VALUE, pub_time=UNKNOWN_VALUE,
                 fet_time=UNKNOWN_VALUE, dtf_oid=UNKNOWN_VALUE,
                 sentiment=UNKNOWN_VALUE):
        self._id = _id
        self.tweet_id = tweet_id
        self.uid = uid
        self.geo = geo
        self.retct = retct
        self.url = url
        self.uname = uname
        self.image = image
        self.dtf_s = dtf_s
        self.content = content
        self.pub_time = pub_time
        self.fet_time = fet_time
        self.dtf_oid = dtf_oid
        self.sentiment = sentiment


class User(object):
    def __init__(self, _id, user_id, name, sname, loc=UNKNOWN_VALUE, stact=UNKNOWN_VALUE, frdct=UNKNOWN_VALUE,
                 url=UNKNOWN_VALUE, dtf_s=UNKNOWN_VALUE, fet_time=UNKNOWN_VALUE, head=UNKNOWN_VALUE,
                 folct=UNKNOWN_VALUE):
        self._id = _id
        self.user_id = user_id
        self.name = name
        self.sname = sname
        self.loc = loc
        self.stact = stact
        self.frdct = frdct
        self.url = url
        self.dtf_s = dtf_s
        self.fet_time = self.fet_time
        self.head = head
        self.folct = folct