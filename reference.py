import twitter


def main():
    url = search('iPhone 12 Pro', '')
    print(url)


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
    url += "%20lang%3Aen&count=2"

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
                      access_token_secret=token_secret)
    return api


if __name__ == '__main__':
    main()
