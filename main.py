import tweepy
import schedule
import datetime
from time import sleep
from keys import *
from words import *
from letters_dict import *


auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

FILE_NAME = "wordle_id.txt"


def retrieve_wordle_id():
    f_read = open("wordle_id.txt", 'r')
    wordle_id = int(f_read.read())
    f_read.close()
    return wordle_id


def update_wordle_id(wordle_id):
    f_write = open("wordle_id.txt", 'w')
    f_write.write(str(wordle_id + 1))
    f_write.close()
    return


def get_word(wordle_id):
    word = WORDS_LIST[wordle_id + 1]
    output = u""
    for letter in word:
        output += LETTERS_UNICODE[letter] + " "
    return output


def tweet():
    wordle_id = retrieve_wordle_id()
    update_wordle_id(wordle_id)
    word = get_word(wordle_id)
    print(
        f"#Wordle {datetime.date.today()}\n{word}\n#Wordle #Wordle{wordle_id}")
    api.update_status(
        f"#Wordle {datetime.date.today()}\n\n{word}\n\n\n#Wordle #Wordle{wordle_id}")
    return


# schedule.every().day.at("06:00").do(tweet)
schedule.every().second.do(tweet)


def main():
    schedule.run_pending()
    sleep(1)


while True:
    main()
