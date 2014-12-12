from summerschool.mongoRepository import MongoTweetsRepository

import json

tweetRepository = MongoTweetsRepository()
tweet = tweetRepository.getTweet(_id = "100416557024227254273")
print(tweet[0])
print(tweet[0].__dict__)

# attributes = dir(tweet[0])
# for attribute in attribute:
#     print(tweet[0], tweet[0][attribute])