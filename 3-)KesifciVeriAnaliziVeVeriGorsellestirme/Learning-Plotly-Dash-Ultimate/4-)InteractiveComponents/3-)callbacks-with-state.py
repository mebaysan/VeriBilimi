import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id='number-in',
        value=1,
        style={'fontSize': 28}
    ),
    html.Button(
        id='submit-button',
        n_clicks=0,
        children='Submit',
        style={'fontSize': 28}
    ),
    html.H1(id='number-out')
])


@app.callback(
    Output('number-out', 'children'),  # çıktıyı nereye vereceğiz
    [Input('submit-button', 'n_clicks')],  # girdiyi nereden alacağız, burada button'dan alıyoruz.
    [State('number-in',
           'value')])  # burası ise durumu tuttuğumuz yer. Burada da bir veri tutuluyor ancak asıl fonksiyon butona basılınca tetikleniyor
def output(n_clicks, number):
    return '{} displayed after {} clicks'.format(number, n_clicks)


if __name__ == '__main__':
    app.run_server()
