import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

COLORS = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(
    children=[
        html.H1('Merhaba Dash!',
                style={  # stil ekleyebiliriz
                    'color': COLORS['text'],
                    'textAlign': 'center',
                }
                ),
        dcc.Graph(
            id='my-chart',
            figure={
                'data': [
                    {'x': ['X Salary', 'Y Salary', 'Z Salary'], 'y': [4, 5, 6], 'type': 'bar', 'name': 'SF'},
                    {'x': ['X Salary', 'Y Salary', 'Z Salary'], 'y': [2, 7, 8], 'type': 'bar', 'name': 'NYC'}
                ],
                'layout': {
                    'title': 'My Bar Chart',
                    'plot_bgcolor': COLORS['background'],  # grafiğin arka planı
                    'paper_bgcolor': COLORS['background'],  # grafiğin üzerinde bulunduğu kağıdın rengi
                    'font': {'color': COLORS['text']},  # fontun stillerini dict olarak veririz
                },
            },
            style={  # figürün stilleri
                'bakcgroundColor': COLORS['background']
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)
