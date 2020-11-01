import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import seaborn as sns
import pandas as pd



def get_fig(df):
    return px.scatter(df, x="Lokasyon_Sayisi", y="Cihaz_Sayisi",
                      size="Data-Download(GB)", color='Lokasyon_Kategorisi',
                      log_x=True, size_max=60,
                      title='Ana Lokasyon Kategorilerinin Alt Bölge Sayısı ve Bağlı Toplam Cihaz Sayısına Göre Download Edilen Data (GB) Miktarı'
                      )


ibb = pd.read_csv('ibb_wifi.csv') # Dataset -> https://data.ibb.gov.tr/dataset/ibbwifi-lokasyon-kategorisine-gore-veri-kullanimi/resource/c80cc8b2-3791-4070-865a-f61296a4cac0

DF = ibb.copy()

app = dash.Dash()

lokasyon_dropdown = dcc.Dropdown(
    id='lokasyon-dropdown',
    options=[
        {'label': f'{lokasyon}', 'value': lokasyon} for lokasyon in DF['Lokasyon_Kategorisi'].unique()
    ],
    searchable=True,
    placeholder='Lokasyon Kategorisi Seçebilirsiniz...',
)

LAYOUT = html.Div(children=[
    html.H1('Callback Çalışması', style={
        'textAlign': 'center',
        'color': 'red',
    }),
    html.Div(children=[
        lokasyon_dropdown,
        dcc.Graph(
            id='scatter-chart',
            figure=get_fig(DF)
        )
    ]),
])

app.layout = LAYOUT


@app.callback(
    dash.dependencies.Output('scatter-chart', 'figure'),
    [dash.dependencies.Input('lokasyon-dropdown', 'value')]
)
def lokasyon_filtrele(value):
    if value:
        return get_fig(DF.query(f'Lokasyon_Kategorisi == "{value}"'))
    else:
        return get_fig(DF)


if __name__ == '__main__':
    app.run_server()
