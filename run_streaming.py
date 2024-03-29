from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import simplejson as json
import pytz, datetime
import sys
import os

data_folder = 'data/01-tweets-christchurch-hourly'

with open('keychain.json') as f:
    keychain = json.load(f)

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key=keychain['CONSUMER_KEY']
consumer_secret=keychain['CONSUMER_SECRET']

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token=keychain['ACCESS_TOKEN']
access_token_secret=keychain['ACCESS_TOKEN_SECRET']

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self):
        self.tweets_collected = 0

    def on_data(self, data):
        # print(data.id)
        tweet = json.loads(data)
        prefix_hour = datetime.datetime.now(pytz.timezone('Europe/Helsinki')).isoformat()[:13]
        hour_folder = '%s/%s' % (data_folder, prefix_hour)
        if not os.path.exists(hour_folder):
            print('... creating directory: ', hour_folder)
            os.makedirs(hour_folder)

        if 'id' in tweet.keys():
            with open('%s/%s.json' % (hour_folder, tweet['id']), 'w') as f:
                json.dump(tweet, f, indent=1)
            self.tweets_collected += 1
            timestamp = datetime.datetime.now(pytz.timezone('Europe/Helsinki')).isoformat()
            sys.stdout.write('\r%s: %s' % (timestamp, self.tweets_collected))
            sys.stdout.flush()
            # print(tweet['id'])

        # with open('')
        # json.dump()
        return True

    def on_error(self, status):
        print(status)

def run_streaming(stream, search_terms):
    timestamp = datetime.datetime.now(pytz.timezone('Europe/Helsinki')).isoformat()
    print('%s Streaming data' % timestamp)
    print('... search terms: ', ', '.join(search_terms))
    try:
        stream.filter(track=search_terms)
    # See https://github.com/tweepy/tweepy/issues/591#issuecomment-92642455
    # various exception handling blocks
    except KeyboardInterrupt:
        sys.exit()
    # except AttributeError as e:
    #     print('AttributeError occured:')
    #     print(e)
    except Exception as e:
        print('Unhandled exception:')
        print(e)
        print('... reconnecting to stream')
        run_streaming(stream, search_terms)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    search_terms = [
        'twitterapi',
        'Twitter streaming API',
    ]
    run_streaming(stream, search_terms)
