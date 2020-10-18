import twitter
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html


def get_tweet_cards(terms, hashtags, accounts):
    result = search(terms, hashtags, accounts)
    cards = make_cards(result)
    return cards


def make_card(status):
    status = status.AsDict()
    full_text = if_has_key(status, "full_text")
    user = if_has_key(status, "user")
    full_text = if_has_key(status, "full_text")
    hashtags = if_has_key(status, "hashtags")
    retweeted_status = if_has_key(status, "retweeted_status")
    media = if_has_key(status, "media")

    profile_image_url = if_has_key(user, "profile_image_url")
    name = if_has_key(user, "name")
    description = if_has_key(user, "description")
    header=html.Div([
            html.Img(src=profile_image_url, style={"border-radius":"10px", "height":"50px", "width":"50px"}),
            html.Div([
                html.H4(name),
                html.P(description, style={"fontStyle":"italic"})
            ], className="name_des"),
            
        ], className = "card_header")

    card = make_inner_card(full_text, media)

    result = html.Div([
        header,
        card
    ], className="card")
    return result


def make_inner_card(full_text, media, url=None):
    card = dbc.Card([
                dbc.CardBody([
                    html.P(full_text)
                ])
                #TODO: link url
            ], className="inner_card")
    if media is not None:
        card.children.append(dbc.CardImg(src=media[0]["media_url"], className="card_img"))
    return card


def if_has_key(status, key):
    if key in status:
        return status[key]
    return None


def make_cards(tweets):
    return [make_card(tweet) for tweet in tweets]


def search(terms, hashtags, accounts):
    api = authenticateApi()
    query = (terms + " " + hashtags).strip()
    print("calling twitter api")
    results = api.GetSearch(term=query, count=100, lang='en',
                            result_type='mixed')
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
