import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np

app = dash.Dash()

np.random.seed(42)
x = np.random.randint(1, 101, 100)
y = np.random.randint(1, 101, 100)

app.layout = html.Div(
    children=[
        dcc.Graph(
            id='my-scatter',
            figure={
                'data': [go.Scatter(x=x, y=y, mode='markers',
                                    marker={'size': 8, 'color': 'rgb(51,204,153)', 'symbol': 'pentagon',
                                            'line': {'width': 12}})],
                'layout': go.Layout(title='Plotly and Dash',
                                    xaxis={'title': 'Random X'},
                                    yaxis=dict(title='Random Y')
                                    )
            }
        ),
        dcc.Graph(
            id='my-scatter2',
            figure={
                'data': [go.Scatter(x=x, y=y, mode='markers',
                                    marker={'size': 12, 'color': 'rgb(200,204,53)', 'symbol': 'pentagon',
                                            'line': {'width': 2}})],
                'layout': go.Layout(title='Second Scatter',
                                    xaxis={'title': 'Random X'},
                                    yaxis=dict(title='Random Y')
                                    )
            }
        )
    ])

if __name__ == '__main__':
    app.run_server()
