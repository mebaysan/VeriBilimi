import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import seaborn as sns
import pandas as pd


def get_fig(df):
    return px.scatter(df, x="total_bill", # x eksenindeki değişken
                      y="tip", # y eksenindeki değişken
                      color='time', # time değişkenine göre renklenecek
                      log_x=True,
                      size_max=60, # max marker boyutu
                      title='Toplam Hesaba Göre Verilen Bahşiş Miktarı', # grafiğin başlığı
                      labels={'time': 'Hangi Öğün', 'total_bill': 'Toplam Hesap', 'tip': 'Bahşiş'} # değişken isimlerine takma isim takıyoruz
                      )


tips = sns.load_dataset('tips')

DF = tips.copy()

app = dash.Dash()

day_dropdown = dcc.Dropdown(
    id='day-dropdown',
    options=[
        {'label': f'Gün: {day}', 'value': day} for day in DF['day'].unique() # day değişkenindeki sınıfları bir listeye basıyoruz
    ],
    searchable=False, # dropdown içerisinde arama yapılamaz
    placeholder='Gün Seçebilirsiniz...', # boşken gözükecek metin
)

smoker_dropdown = dcc.Dropdown(
    id='smoker-dropdown',
    options=[
        {'label': f'Sigara: {smoker}', 'value': smoker} for smoker in DF['smoker'].unique()
    ],
    searchable=False,
    placeholder='Sigara Durumunu Seçebilirsiniz...'
)

LAYOUT = html.Div(children=[
    html.H1('Callback Çalışması', style={
        'textAlign': 'center',
        'color': 'red',
    }),
    html.Div(children=[
        html.Div(children=[
            day_dropdown, # dropdown'ları diziyoruz
            smoker_dropdown,
        ], style={'width': '50%', 'float': 'left', 'margin-top': '140px'}),
        dcc.Graph( # grafiği çizdiriyoruz
            id='scatter-chart',
            figure=get_fig(DF),
            style={'width': '50%', 'float': 'right'}
        ),
    ]),
])

app.layout = LAYOUT


@app.callback(
    dash.dependencies.Output('scatter-chart', 'figure'),
    [dash.dependencies.Input('day-dropdown', 'value'),  # 2 adet input'umuz olduğu için liste olarak veriyoruz
     dash.dependencies.Input('smoker-dropdown', 'value')]
)
def day_filtrele(day_value, smoker_value): # input'ların sırasıyla callback'e gelecek değerleri yakalıyoruz
    if not day_value and not smoker_value: # bu kısım daha da optimize edilebilir, biraz aceleyle yazdığım için amatörce kaldı ^^
        print(f'İKİSİDE YOK ---> {day_value} + {smoker_value}')
        return get_fig(DF) # eğer hiçbir değer seçilmediyse DF'i olduğu gibi geri yolluyoruz
    elif day_value and not smoker_value:
        print(f'SADECE DAY_VAL ---> {day_value}')
        return get_fig(DF.query(f'day == "{day_value}"')) # eğer bir değer seçildiyse uygun filtrelemeyi yapıp güncel DF'i yolluyoruz
    elif smoker_value and not day_value:
        print(f'SADECE SMOKER_VAL ---> {smoker_value}')
        return get_fig(DF.query(f'smoker == "{smoker_value}"'))
    else:
        print(f'İKİSİDE VAR ---> {day_value} + {smoker_value}')
        return get_fig(DF.query(f'day == "{day_value}"').query(f'smoker == "{smoker_value}"'))


if __name__ == '__main__':
    app.run_server()
