import tweepy
import os

def main():
    twitter_auth_keys = {

        "consumer_key"        : os.environ.get("CONSUMER_KEY"),

        "consumer_secret"     : os.environ.get("CONSUMER_SECRET"),

        "access_token"        : "1041168468739932161-054KuEx04kP1grfyMHIq7kiNlYuExq",

        "access_token_secret" : "UYlq8ZiKW6qUN7qqSHAIxLeGixSI1QWhB4jDjY3OUOryL"

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

    media = api.media_upload("test.png")

 

    # Post tweet with image

    tweet = "Testing please ignore by the way look at this duck"

    post_result = api.update_status(status=tweet, media_ids=[media.media_id])

 

if __name__ == "__main__":

    main()