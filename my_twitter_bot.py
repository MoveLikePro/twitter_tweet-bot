import tweepy
import time
print("twitter bot")

API_KEY = 'PASTE YOUR API KEY HERE'
API_KEY_SECRET = 'PASTE YOUR API KEY SECRET HERE'
ACCESS_TOKEN = 'PASTE YOUR ACCESS TOKEN HERE'
ACCESS_TOKEN_SECRET = 'PASTE YOUR ACCESS TOKEN SECRET HERE'

auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
print(api)

FILE_NAME = "last_seen_id.txt"

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, "r")
    last_seen_id = f_read.read().strip()
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, "w")
    f_write.write(str(last_seen_id))
    f_write.close()
    return
def reply_to_tweets():
    print("Retrieving and Replying...")
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    new=api.retweet

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        print(mention.user.screen_name)
        if '#hi' in mention.full_text.lower():
            print('found #hi')
            print('responding back')
            api.update_status('@' + mention.user.screen_name + '`Hello back to you!', mention.id)
            print(mention.user.screen_name)
        if 'how you doing' in mention.full_text.lower():
            print('found how you doing')
            print('responding back')
            api.update_status('@' + mention.user.screen_name + '`Hi! I am doing #great. What about you?', mention.id)
            print(mention.user.screen_name)
        if 'how are you' in mention.full_text.lower():
            print('found how are you')
            print('responding back')
            api.update_status('@' + mention.user.screen_name + '`Hi! I am #fine. What about you?', mention.id)
            print(mention.user.screen_name)

while True:
    reply_to_tweets()

