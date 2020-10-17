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


app = dash.Dash(__name__)


def make_card(text1, text2, url):
	div = html.Div([
		html.Div([
			html.Div([
				html.H5(text1),
				html.Img(src = url)
			], className="card_front"),
			html.Div([
				html.H5(text1),
				html.P(text2)
			], className="card_back")
		], className="flip_card_inner")
	], className="flip_card")
	return div


app.layout = html.Div([
    html.H2('Twitter-Like App for Filtering Sentiment', className="header"),
	html.Div([html.P('This is an interactive web app designated for \
					  filtering tweets to see sentiments')],
					  className="intro"),

	html.Div([
		html.Div(
			[dcc.Input(
				id="terms",
				type="text",
				placeholder="Terms",
				className = "tools",
				style={'fontSize': '100%'}
        	),
			html.Button("Search")]
		),
		html.Div(
			[dcc.Input(
				id="hashtags",
				type="text",
				placeholder="Hashtags",
				className = "tools",
				style={'fontSize': '100%'}
			),
			html.Button("Search")]
		),
		html.Div(
			[dcc.Input(
				id="accounts",
				type="text",
				placeholder="Accounts",
				className = "tools",
				style={'fontSize': '100%'}
			),
			html.Button("Search")]
		),
		html.Div([dcc.DatePickerSingle(
			id='my-date-picker-single',
			min_date_allowed=date(2006, 3, 31),
			date=date(2020, 10, 17)
    	)])
	], className="filters", id="filter"),

	html.Div([
		html.Div([make_card("Some Info", str(i) + "Some Info", 
		"") \
				  for i in range(3)], 
		className="row"),

		html.Div([make_card("Some Info", str(i) + "Some Info",
		"") \
				  for i in range(3)], 
		className="row"),
		
		html.Div([make_card("Some Info", str(i) + "Some Info",
		"") \
				  for i in range(3)], 
		className="row")
	], className="container", id="container")
])

if __name__ == '__main__':
    app.run_server(debug=True)