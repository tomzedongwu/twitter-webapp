# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_dangerously_set_inner_html
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from datetime import date
from dash.dependencies import Input, Output, State, MATCH, ALL


app = dash.Dash(__name__)

def make_card(text1, text2):
	div = html.Div([
		html.Div([
			html.Div([
				html.H5(text1),
				html.P(text2)
			], className = "card_front"),
			html.Div([
				html.H5(text1),
				html.P(text2)
			], className = "card_back")
		], className = "flip_card_inner")
	], className = "flip_card")
	return div

app.layout = html.Div([
    html.H2('Twitter-Like App for Filtering Sentiment', className = "header"),
	html.Div([
		html.P('This is an interactive web app designated for filtering tweets to see sentiments')
	], className = "intro"),

	html.Div([
		html.Div([
			html.P("Click To Add Cards  "),
			html.Button('Add Cards', id='add_cards', n_clicks=0, className = "btn")
		], className = "filter1"),

		html.Div([
			html.P("Click To Select Date  "),
			dcc.DatePickerSingle(
				id='date-picker-single',
				date=date(2020, 1, 1)
			)
		], className = "filter1"),

		html.Div([
			html.P("Click To Select Cities  "),
			dcc.Dropdown(
				options=[
					{'label': 'New York City', 'value': 'NYC'},
					{'label': 'Seattle', 'value': 'SEA'},
					{'label': 'San Francisco', 'value': 'SF'},
					{'label': 'Chicago', 'value': 'CHI'},
					{'label': 'Los Angeles', 'value': 'LA'}
				],
				multi=True,
				value="SEA"
			)  
		], className = "filter2"),

		html.Div([
			html.P("Range Slider For .....  "),
			dcc.Slider(
				min=0,
				max=5,
				marks={i: 'Label {}'.format(i) for i in range(5)},
				value=5,
			)   
		], className = "filter3")
	], className = "filters", id="filter"),

	html.Div([
		html.Div([make_card("Some Info", str(i) + "Some Info") for i in range(3)], 
		className = "row"),

		html.Div([make_card("Some Info", str(i) + "Some Info") for i in range(3)], 
		className = "row"),
		
		html.Div([make_card("Some Info", str(i) + "Some Info") for i in range(3)], 
		className = "row")
	], className = "container", id="container")
])

@app.callback(
	Output('container', 'children'),
	[Input('add_cards', 'n_clicks')],
	[State('container', 'children')]
)

def more_cards(n_clicks, div_children):
    if n_clicks > 0:
    	new_card = html.Div([make_card("Some Info", str(i) + "Some Info") for i in range(3)], 
		className = "row")
    	div_children.append(new_card)
    return div_children

if __name__ == '__main__':
    app.run_server(debug=True)