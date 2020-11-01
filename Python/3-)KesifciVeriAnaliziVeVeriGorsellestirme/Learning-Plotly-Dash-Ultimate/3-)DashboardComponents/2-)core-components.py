import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.Label('Dropdowm'),
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'İstanbul', 'value': 34},  # seçeneleri dict tutan liste olarak veririz
                {'label': 'Ankara', 'value': 6},
                {'label': 'Erzurum', 'value': 25},
            ],
            multi=True,
            value=34,
            searchable=True,
        ),
        html.Label('Radio'),
        dcc.RadioItems(
            id='my-radio',
            options=[
                {'label': 'İstanbul', 'value': 34},
                {'label': 'Ankara', 'value': 6},
                {'label': 'Erzurum', 'value': 25},
            ],
            value=34,
        ),
        html.Label('Slider'),
        dcc.Slider(
            id='my-slider',
            min=0,
            max=20,
            step=0.5,
            value=10,
            marks={i: i for i in range(0, 21)}
        ),
    ]
)

if __name__ == '__main__':
    app.run_server()
