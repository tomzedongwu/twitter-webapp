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
    status = status.AsDict()
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


def newSearch(words, hashtags):
    api = authenticateApi()
    query = words + hashtags
    results = api.GetSearch(term=query, count=100, lang='en',
                            result_type='mixed')
    print(results[0].created_at)
    print(len(results))
    for i in range(len(results)):
        print(i + 1, results[i].full_text)
        print()
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
