# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Dropdown Menu'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL' # default value
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        multi=True
    ),

    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
        
    ),

    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'NYC']
    ),

    html.Label('Text Input'),
    dcc.Input(value='San Francisco', type='text'),

    html.Label('Slider'),
    dcc.Slider(
        min=9,
        max=15,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(9, 16)},
        value=11,
    ),

    html.Label('Range Slider'),
    dcc.RangeSlider(
        marks = {i: "{}".format(i) for i in range(-5, 11)},
        count=1,
        min=-5,
        max=10,
        step=1,
        value=[-3, 7]
    ), 

    html.Label('Input text holder'),
    dcc.Input(
        placeholder='Enter a value...',
        type='text',
        value=''
    ),  

    html.Label("Text area"),
    dcc.Textarea(
        placeholder='Enter a value...',
        value='This is a TextArea component',
        style={'width': '100%'}
    ),  

    html.Label("Checkboxes inline"),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF'],
        labelStyle={'display': 'inline-block'}

        # can also use inline style on radio items

    ),
    
      

], style={'columnCount': 2})

if __name__ == '__main__':
    app.run_server(debug=True)