import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import pandas as pd
from numpy import random

app = dash.Dash()

df = pd.read_csv('https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/mpg.csv',
                 error_bad_lines=False)

df['year'] = random.randint(-4, 5, len(df)) * 0.10 + df['model_year']  # yeni bir kolon ekliyoruz

app.layout = html.Div([
    html.Div(children=[dcc.Graph(
        id='mpg-scatter',
        figure={
            'data': [go.Scatter(
                x=df['year'] + 1900,
                y=df['mpg'],
                text=df['name'],
                hoverinfo='text',
                mode='markers'
            )],
            'layout': go.Layout(
                title='mpg.csv dataset from github',
                xaxis={'title': 'Model Year'},
                yaxis={'title': 'Miles Per Gallon'},
                hovermode='closest'
            )
        }
    )], style={'width': '50%', 'display': 'inline-block'}),
    html.Div(children=[
        dcc.Graph(id='mpg-line',
                  figure={'data': [go.Scatter(x=[0, 1], y=[0, 1], mode='lines')],
                          'layout': go.Layout(title='Acceleration', margin={'l': 0, }, xaxis={'visible': False},
                                              yaxis={'visible': False})}
                  )
    ],
        style={'width': '50%', 'display': 'inline-block'})
])


@app.callback(
    Output('mpg-line', 'figure'),
    Input('mpg-scatter', 'hoverData')
)
def callback(hoverData):  # mpg-scatter üzerindeki verilerde gover olduğunda yanda yeni bir chart çizeceğiz
    print(hoverData)
    v_index = hoverData['points'][0]['pointIndex']
    figure = {
        'data': [go.Scatter(x=[0, 1], y=[0, 60 / df.iloc[v_index]['acceleration']], mode='lines')],
        'layout': go.Layout(title=df.iloc[v_index]['name'], margin={'l': 0}, height=300, xaxis={'visible': False},
                            yaxis={'visible': False, 'range': [0, 60 / df['acceleration'].min()]})
    }
    return figure


if __name__ == '__main__':
    app.run_server()
