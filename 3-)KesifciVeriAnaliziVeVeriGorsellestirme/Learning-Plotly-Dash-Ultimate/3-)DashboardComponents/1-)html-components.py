import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(
    children=[
        'Dışardaki div',
        html.Div(
            children=[
                'İçerdeki div',
                html.Div('En içerdeki div',
                         style={
                             'color': 'blue',
                             'border': '2px blue solid',
                         }
                         )
            ],
            style={
                'color': 'red',
                'border': '2px red solid',
            }
        )
    ],
    style={
        'color': 'green',
        'border': '2px green solid',
    }
)

if __name__ == '__main__':
    app.run_server()
