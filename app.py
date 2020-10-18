# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
from datetime import date
from dash.dependencies import Input, Output, State, MATCH, ALL
import reference

app = dash.Dash(__name__)


app.layout = html.Div([
    html.H2('Twitter-Like App for Filtering Sentiment', className="header"),
	html.Div([html.P('This is an interactive web app designated for \
					  filtering tweets to see sentiments')],
					  className="intro"),

	html.Div([
		html.Div([
			dcc.Input(
				id="terms",
				type="text",
				placeholder="Terms",
				className = "tools",
				style={'fontSize': '100%'}
        )]),
		html.Div(
			[dcc.Input(
				id="hashtags",
				type="text",
				placeholder="Hashtags",
				className = "tools",
				style={'fontSize': '100%'}
		)]),
		html.Div(
			[dcc.Input(
				id="accounts",
				type="text",
				placeholder="Accounts",
				className = "tools",
				style={'fontSize': '100%'}
		)]),
		html.Button("Search", id="search_button")
	
	], className="filters", id="filter"),

	html.Div([], className="container", id="container")
])


@app.callback(
	[Output('container', 'children')],
	[Input('search_button', 'n_clicks')],
	[State("terms", "value"),
	 State("hashtags", "value"),
	 State("accounts", "value")]	
)
def refresh_content(button_clicks, terms, hashtags, accounts):
	if terms is None and hashtags is None and accounts is None:
		return ([html.P("you've found the flag: flag{twitter_webapp}")])
	terms = '' if terms is None else terms
	hashtags = '' if hashtags is None else hashtags
	accounts = '' if accounts is None else accounts
	cards = reference.get_tweet_cards(terms, hashtags, accounts)
	res = [html.Div([cards[i + j] for j in range(0, len(cards) - 1, 3)]) for i in range(3)]
	print(len(cards))

	return [res]


if __name__ == '__main__':
    app.run_server(debug=True)