import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import json

df = pd.read_csv('https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/wheels.csv',
                 error_bad_lines=False)
app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Div(children=[
            dcc.Graph(id='wheels-chart',
                      figure={'data': [
                          go.Scatter(
                              x=df['color'],
                              y=df['wheels'],
                              dy=1,
                              mode='markers',
                              marker={'size': 15}
                          )],
                          'layout': go.Layout(title='Hover Data', hovermode='closest')
                      },
                      ),
        ],
            style={'width': '30%', 'float': 'left'}
        ),
        html.Div(
            children=[
                html.Pre(id='hover-data',
                         style={'paddingTop': 35}
                         ),
            ],
            style={'width': '30%'}
        )
    ],
)


@app.callback(
    Output('hover-data', 'children'),
    Input('wheels-chart', 'hoverData')  # wheels-chart içerisinde verilerin üzerine gelinince tetiklenecek
)
def callback_hover(hoverData):
    return json.dumps(hoverData, indent=2)


if __name__ == '__main__':
    app.run_server()
