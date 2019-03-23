import os
from requests_oauthlib import OAuth1Session

consumer_key=os.environ['TWITTER_CONSUMER_KEY']
consumer_secret=os.environ['TWITTER_CONSUMER_SECRET']
access_token=os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']

session = OAuth1Session(consumer_key,
                        client_secret=consumer_secret,
                        resource_owner_key=access_token,
                        resource_owner_secret=access_token_secret)

# The URL endpoint to update a status (i.e. tweet)
url = 'https://api.twitter.com/1.1/statuses/update.json'

hashtag_conversion_dict = {
    'frankenstein'      : '#Frankenstein',
    'modestproposal'    : '#modestproposal',
    'prideprejudice'    : '#PrideandPrejudice',
    'secretgarden'      : '#theSecretGarden',
    'huckleberryfinn'   : '#HuckleBerryFinn'
}

def tweet(status, source):
    status = status + ' ' + hashtag_conversion_dict[source[8:-4]]
    resp = session.post(url, { 'status': status })
    return resp.text
    