import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import mydata

DF = mydata.get_data()

app = dash.Dash()

fig = px.area(x='tarih', y='gunluk_iyilesen', data_frame=DF, title='Günlere Göre Toplam Vaka Sayısı')

# fig.add_bar(x='tarih', y='gunluk_iyilesen')

fig.update_layout(
    xaxis_title='Tarih',
    yaxis_title='Günlük İyileşen',
)

app.layout = dcc.Graph(
    id='test',
    figure=fig
)
if __name__ == '__main__':
    app.run_server(debug=True)
