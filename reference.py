import twitter
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

def main():
    result = search('Donald Trump', '')
    card = make_cards(result)
    print(len(result))

def make_card(status):
    status=status.AsDict()
    full_text = if_has_key(status, "full_text")
    user = if_has_key(status, "user")
    hashtags = if_has_key(status, "hashtags")
    retweeted_status = if_has_key(status, "retweeted_status") 
    return None

def if_has_key(status, key):
    if key in status:
        return status[key]
    return None

def make_cards(tweets):
    return [make_card(tweet) for tweet in tweets]

def search(words, hashtags):
    url = 'q='

    words_str = ''
    words = words.split(' ')
    words_str = '%20'.join(words)

    hashtags = hashtags.split(' ')
    hash_query_str = ''
    if hashtags[0] != '':
        hash_query = [hashtag.replace('#', '%23') for hashtag in hashtags]
        hash_query_str += '(' + '%20OR%20'.join(hash_query) + ')'
    
    url += words_str
    if(len(hash_query_str) > 0):
        url += '%20' + hash_query_str
    url += "%20lang%3Aen&count=100"

    print(url)

    api = authenticateApi()
    results = api.GetSearch(raw_query=url)
    return results


def authenticateApi():
    """
    Feeds keys to create interface with twitter and returns the interface
    object. Expects keys in folder names 'key_and_secret'.
    """
    with open("keys_and_secrets/api_key.txt") as f:
        key = f.read().rstrip()

    with open('keys_and_secrets/api_secret.txt') as f:
        secret = f.read().rstrip()

    with open("keys_and_secrets/access_token.txt") as f:
        token = f.read().rstrip()

    with open('keys_and_secrets/access_token_secret.txt') as f:
        token_secret = f.read().rstrip()

    api = twitter.Api(consumer_key=key,
                      consumer_secret=secret,
                      access_token_key=token,
                      access_token_secret=token_secret,
                      tweet_mode="extended")
    return api


if __name__ == '__main__':
    main()



