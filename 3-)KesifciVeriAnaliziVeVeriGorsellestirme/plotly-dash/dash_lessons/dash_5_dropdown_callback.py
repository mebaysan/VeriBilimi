import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import seaborn as sns

app = dash.Dash()
tips = sns.load_dataset('tips')
df = tips.copy()

LAYOUT = html.Div(
    children=[
        html.H1('Hello Dash!!', style={'textAlign': 'center', 'color': 'red'}),
        dcc.Dropdown(
            id='first-dropdown',
            options=[
                {'label': 'Akşam Yemeği', 'value': 'Dinner'},
                {'label': 'Öğle Yemeği', 'value': 'Lunch'},
                {'label': 'Kahvaltı', 'value': 'Breakfast', 'disabled': True}
                # istersek bir seçeneği de disabled yapabiliriz
            ],
            value='',
            # multi=True,  # çoklu seçimlere müsaade edilir
            placeholder='Öğün Seçin',
            # disabled=True, # dropdown seçilemez olur
        ),
        html.Div(
            dcc.Graph(
                id='first-graph',

            )
        )
    ]
)
app.layout = LAYOUT


@app.callback(
    dash.dependencies.Output('first-graph', 'figure'),
    # çıktıyı nereye vereceğiz? first-grapf id'li component içerisindeki figüre
    [dash.dependencies.Input('first-dropdown',
                             'value')])  # girdiği nerden alacağız? first-dropdown id'li component içerisinden seçilen value'den
def ogun_sec(value):
    if value and value != '':
        filtered_df = df.query(f'time=="{value}"')
        time_string = f'({value} Öğünü)'
    else:
        filtered_df = df
        time_string = '(Tüm Öğünler)'
    fig = px.scatter(x='total_bill', y='tip', color='smoker', size='total_bill', data_frame=filtered_df, text='tip',
                     title=f'Toplam hesaba göre bahşiş oranı {time_string}',
                     labels={'total_bill': 'Toplam Hesap', 'tip': 'Bahşiş', 'smoker': 'Sigara İçme Durumu'})

    return fig


if __name__ == '__main__':
    app.run_server()
