import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import mydata

DF = mydata.get_data()

app = dash.Dash()
app.layout = html.Div(children=[
    html.Div(
        children=[
            html.Label('Tarih Aralığı Seçin', style={'fontSize': '20px', 'paddingRight': '15px'}),
            dcc.DatePickerRange(
                id='my-date-picker',
                min_date_allowed=datetime(DF['tarih'].min().year, DF['tarih'].min().month, DF['tarih'].min().day), # en az hangi tarih seçilebilir
                max_date_allowed=datetime(DF['tarih'].max().year, DF['tarih'].max().month, DF['tarih'].max().day + 1), # en fazla hangi tarih seçilebilir, +1 vermemizin sebebi bizim en sonki tarihimizden bir gün sonrası da seçilebilsin bu sayede son günümüzü de seçebiliriz
                start_date=datetime(DF['tarih'].min().year, DF['tarih'].min().month, DF['tarih'].min().day), # başlangıç değerini set ediyoruz
                end_date=datetime(DF['tarih'].max().year, DF['tarih'].max().month, DF['tarih'].max().day), # bitiş değerini set ediyoruz
                display_format='D/M/YYYY',
            ),
            html.Button(
                id='submit-button',
                n_clicks=0,
                children='Filtrele',
                style={'fontSize': 24, 'marginLeft': '30px'}
            )
        ],
        style={'paddingBottom': '30px', 'textAlign': 'center'}
    ),
    html.Div(
        children=[
            dcc.Graph(id='gunluk-chart', style={'width': '50%', 'float': 'left'}),
            dcc.Graph(id='toplam-chart', style={'width': '50%', 'float': 'right'}),
            dcc.Markdown(id='gunluk-ozet', style={'width': '50%', 'float': 'left'}),
            dcc.Markdown(id='toplam-ozet', style={'width': '50%', 'float': 'right'}),
        ]
    )
])


def gunluk_chart(start, end):
    filtered_df = DF.query(f'tarih >= "{start}"').query(f'tarih <= "{end}"') # başlangıç tarihine büyük veya eşit, bitiş değerine eşit veya küçük tarihleri getiriyoruz
    gunluk_column_names = ['gunluk_vaka', 'gunluk_vefat', 'gunluk_iyilesen'] # veri setindeki kolonlarımızdan hangilerine grafik çizmek istiyorsak o kolon isimlerini liste olarak aldık
    gunluk_traces = []
    for col_name in gunluk_column_names: # her kolonu gez ve ona özel bir grafik çıkart
        gunluk_traces.append(
            go.Scatter(x=filtered_df['tarih'], y=filtered_df[col_name], mode='lines', name=col_name))
    layout = go.Layout(title='2 Tarih Arasında Türkiye Günlük Corona Verileri', yaxis={'title': 'Günlük Veriler'},
                       xaxis={'title': 'Tarih'}, hovermode='x unified')
    gunluk_chart = go.Figure(layout=layout, data=gunluk_traces)
    return gunluk_chart


def toplam_chart(start, end):
    filtered_df = DF.query(f'tarih >= "{start}"').query(f'tarih <= "{end}"')
    toplam_column_names = ['toplam_vaka', 'toplam_vefat', 'toplam_iyilesen']
    toplam_traces = []
    for col_name in toplam_column_names:
        toplam_traces.append(go.Scatter(x=filtered_df['tarih'], y=filtered_df[col_name], mode='lines', name=col_name))
    layout = go.Layout(title='2 Tarih Arasında Türkiye Toplam Corona Verileri', yaxis={'title': 'Toplam Veriler'},
                       xaxis={'title': 'Tarih'}, hovermode='x unified')
    toplam_chart = go.Figure(layout=layout, data=toplam_traces)
    return toplam_chart


@app.callback([Output('gunluk-chart', 'figure'), Output('toplam-chart', 'figure')],
              Input('submit-button', 'n_clicks'),
              [State('my-date-picker', 'start_date'), State('my-date-picker', 'end_date')])
def callback(n_clicks, start_date, end_date):
    start = pd.to_datetime(datetime.strptime(start_date[:10], '%Y-%m-%d')) # gelen tarih verisini pandas veri tipine dönüştürüyoruz, çünkü kendi verimizi pandas veri tipinde güncellemiştik
    end = pd.to_datetime(datetime.strptime(end_date[:10], '%Y-%m-%d'))
    return gunluk_chart(start, end), toplam_chart(start, end)


@app.callback(
    Output('gunluk-ozet', 'children'),
    Input('gunluk-chart', 'clickData')
)
def gunluk_hover(clickData):
    if not clickData == None:
        tarih = clickData['points'][0]['x']
        tarih = pd.to_datetime(tarih)
        filtered_df = DF.query(f'tarih == "{tarih}"')
        return f"""
### Tarih: {tarih.day}/{tarih.month}/{tarih.year}
| Günlük Vaka   |      Günlük İyileşen      |  Günlük Vefat |
|:----------:|:-------------:|:------:|
| {filtered_df['gunluk_vaka'].sum()} |  {filtered_df['gunluk_iyilesen'].sum()} | {filtered_df['gunluk_vefat'].sum()} |

                """


@app.callback(
    Output('toplam-ozet', 'children'),
    Input('toplam-chart', 'clickData')
)
def toplam_hover(clickData):
    if not clickData == None:
        tarih = clickData['points'][0]['x']
        tarih = pd.to_datetime(tarih)
        filtered_df = DF.query(f'tarih == "{tarih}"')
        return f"""
    ### Tarih: {tarih.day}/{tarih.month}/{tarih.year}
    | Toplam Vaka   |      Toplam İyileşen      |  Toplam Vefat |
    |:----------:|:-------------:|:------:|:-------:|
    | {filtered_df['toplam_vaka'].sum()} |  {filtered_df['toplam_iyilesen'].sum()} | {filtered_df['toplam_vefat'].sum()} |

                    """


if __name__ == '__main__':
    app.run_server(debug=True)
