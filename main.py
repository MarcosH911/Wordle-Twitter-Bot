import tweepy
from keys import *


auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

FILE_NAME = "wordle_id.txt"


def retrieve_wordle_id(file_name):
    f_read = open("wordle_id.txt", 'r')
    wordle_id = int(f_read.read())
    f_read.close()
    return wordle_id


def store_wordle_id(file_name, wordle_id):
    f_write = open("wordle_id.txt", 'w')
    f_write.write(strint(text) + 1)
    f_write.close()
    return


# store_wordle_id()

# api.update_status('This is my first tweet with the API!\n:D')
# #Wordle  #Wordle241
