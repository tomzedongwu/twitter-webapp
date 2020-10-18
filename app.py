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
app.title = "Twitter-WebApp"

app.layout = html.Div([
	html.Div([
		html.Img(src="assets/images/icon.png", className="hack"),
    	html.H2('Twitter Sentiment Dashboard', className="header"),
		html.Img(src="assets/images/icon2.png", className="uw"),
	], className="banner"),
	html.Div([html.P('An interactive web app to search for and filter Tweets and gain insight into users\' sentiments')],
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
		html.Button("Search", id="search_button", className="search")
	
	], className="filters", id="filter"),
	html.Div([
		html.Div([], className="column", id="col1"),
		html.Div([], className="column", id="col2"),
		html.Div([], className="column", id="col3"),
		html.Div([], className="column", id="col4")
	], id="container", className="container"),
	html.Img(src="assets/images/dog.jpg", className="instruct")
])

@app.callback(
	[Output("col1", "children"),
	Output("col2", "children"),
	 Output("col3", "children"),
	 Output("col4", "children")],
	[Input('search_button', 'n_clicks')],
	[State("terms", "value"),
	 State("hashtags", "value"),
	 State("accounts", "value")]	
)
def refresh_content(button_clicks, terms, hashtags, accounts):
	if terms is None and hashtags is None and accounts is None:
		return html.P(""), html.P(""),html.P(""),html.P("")
	terms = '' if terms is None else terms
	hashtags = '' if hashtags is None else hashtags
	accounts = '' if accounts is None else accounts
	cards = reference.get_tweet_cards(terms, hashtags, accounts)
	num_column = 4
	res = [html.Div([cards[i + j] if i + j < len(cards) else html.Div() for j in range(0, len(cards), num_column)], className="column") for i in range(num_column)]
	#temp = [cards[i + j] if i + j < len(cards) else html.Div() for j in range(0, len(cards), num_column)]
	#print(len(cards))
	
	return res[0], res[1], res[2], res[3]

if __name__ == '__main__':
    app.run_server(debug=True)