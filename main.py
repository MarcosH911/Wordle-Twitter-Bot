import tweepy


consumer_key = "P5Q5GJvYatyRBEt4tx4iLOpfU"
consumer_secret = "8jouxLezINeAUzMuc3vXb15Yge6FvEonII1o2s1NH0EeptPJt4"
access_token = "1492973847053803522-4zg3t9UZwTLjDsMaqeThuW3mHcGRw9"
access_token_secret = "ZSrQoGHKVjMIvK3s9xk0T9Yk9CiMOGwAUFbAyYLugpGRQ"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
# myStream.filter(track=["news"])
