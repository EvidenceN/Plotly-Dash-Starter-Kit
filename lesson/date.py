import dash_core_components as dcc
from datetime import date
import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label("Date Picker"),
    dcc.DatePickerSingle(
        id='date-picker-single',
        date=date(1997, 5, 10)
    ),

    #html.Label("Date picker range"),
    html.Div(html.Label("Date picker range")),
    
    html.Div(dcc.DatePickerRange(
        id='date-picker-range',
        start_date=date(1997, 5, 3),
        end_date_placeholder_text='Select a date!'
    )),

])

if __name__ == '__main__':
    app.run_server(debug=True)