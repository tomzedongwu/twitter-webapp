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
from reference import temp


app = dash.Dash(__name__)


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
		html.Div(temp(), 
		className="row"),

		html.Div([], 
		className="row"),
		
		html.Div([], 
		className="row")
	], className="container", id="container")
])

if __name__ == '__main__':
    app.run_server(debug=True)