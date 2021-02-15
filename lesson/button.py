import dash
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

introduction_text = """
### Instructions about button in Dash

There actually is no Button component 
in dash_core_components. 
The regular dash_html_components.Button 
component does the job quite well, 
but we've included it here because 
this is the one plain html component 
that's commonly used as a callback input:
"""

app.layout = html.Div([
    dcc.Markdown(introduction_text),

    html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Submit', id='button', 
    style = {'color': 'white', 
    'backgroundColor': 'blue'}),
    html.Div(id='output-container-button',
             children='Enter a value and press submit')
])


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )


if __name__ == '__main__':
    app.run_server(debug=True)