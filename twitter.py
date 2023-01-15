import tweepy
import os

def create_tweet(text:str, image_path:str):
    twitter_auth_keys = {

        "consumer_key"        : os.environ.get("CONSUMER_KEY"),

        "consumer_secret"     : os.environ.get("CONSUMER_SECRET"),

        "access_token"        : os.environ.get("ACCESS_TOKEN"),

        "access_token_secret" : os.environ.get("ACCESS_TOKEN_SECRET")

    }

 

    auth = tweepy.OAuthHandler(

            twitter_auth_keys['consumer_key'],

            twitter_auth_keys['consumer_secret']

            )

    auth.set_access_token(

            twitter_auth_keys['access_token'],

            twitter_auth_keys['access_token_secret']

            )

    api = tweepy.API(auth)

 

    # Upload image

    media = api.media_upload(image_path)

 

    # Post tweet with image

    tweet = text

    post_result = api.update_status(status=tweet, media_ids=[media.media_id])

def main():
    create_tweet("testing again sorry", "test.png")

if __name__ == "__main__":
    main()