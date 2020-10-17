# Hello this is Zane's file

def main():
    url = search('iPhone 12 Pro', '#Max #great')
    print(url)


def search(words, hashtags):
    url = 'q='

    words = words.split(' ')
    if len(words) > 0:
        url += '%20'.join(words)

    hashtags = hashtags.split(' ')
    if len(hashtags) > 0:
        if(len(words) > 0):
            url += '%20('
        else:
            url += '('
        hash_query = []
        for hashtag in hashtags:
            hash_query.append(hashtag.replace('#', '%23'))
        url += '%20OR%20'.join(hash_query)
        url += ')'

    url += '&src=typed_query'
    return url


if __name__ == '__main__':
    main()
