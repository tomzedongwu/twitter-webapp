# Hello this is Zane's file

def main():
    url = search('iPhone 12 Pro Max')
    print(url)


def search(query):
    words = query.split(' ')
    url = 'https://twitter.com/search?q='
    for word in range(len(words) - 1):
        url += words[word] + '%20'
    url += words[len(words) - 1]

    url += '&src=typed_query'
    return url


if __name__ == '__main__':
    main()
