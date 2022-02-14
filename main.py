import sys
import tweepy

# auth = tweepy.OAuthHandler("mYnV80efTQJe2uFmC5jahKovb",
#                            "XYOgzrdCxbPSs7rgg1Mngr3a9usO3cNlVRUCBhYremb9oOsPY3")
# auth.set_access_token("1492973847053803522-x4l3JyemFsYUDlfOuTG8OKHNqnKRoI",
#                       "E1d1TbOTPEEwWqEodQsn8ifeiwVX50BXNCV1p8dkkodXt")

# api = tweepy.API(auth)

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")


# class MyStreamListener(tweepy.StreamListener):
#     def on_status(self, status):
#         print(status.text)

#     def on_error(self, status_code):
#         print(status_code)


consumer_key = "mYnV80efTQJe2uFmC5jahKovb"
consumer_secret = "XYOgzrdCxbPSs7rgg1Mngr3a9usO3cNlVRUCBhYremb9oOsPY3"
access_token = "1492973847053803522-x4l3JyemFsYUDlfOuTG8OKHNqnKRoI"
access_token_secret = "E1d1TbOTPEEwWqEodQsn8ifeiwVX50BXNCV1p8dkkodXt"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

if (not api):
    print("Authentication failed!")
    sys.exit(-1)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
# myStream.filter(track=["news"])
