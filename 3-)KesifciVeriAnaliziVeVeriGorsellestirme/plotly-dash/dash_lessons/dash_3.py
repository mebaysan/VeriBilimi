import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

LAYOUT = html.Div(
    children=[
        html.H1('Hello Dash!!', style={'textAlign': 'center', 'color': 'red'}),
        # html componentlerine css ekleyebiliriz
        html.Div('Dash Data Driven Development!'),
        dcc.Graph(
            id='my-first-graph',
            figure={
                'data': [
                    {'x': [4, 6, 8],
                     'y': [12, 16, 18],
                     'type': 'bar',
                     'name': 'My First Chart'},
                    {'x': [4, 6, 8],
                     'y': [20, 24, 12],
                     'type': 'bar',
                     'name': 'My Second Chart'}
                ],
                'layout': {
                    'title': 'My Simple Bar Chart'
                }
            }
        )
    ]
)
app.layout = LAYOUT

if __name__ == '__main__':
    app.run_server()
