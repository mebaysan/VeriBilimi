import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/2018WinterOlympics.csv',
    error_bad_lines=False)

bar_chart = go.Bar(x=df['NOC'], y=df['Gold'], name='Gold', marker={'color': '#FFD700'})
bar_chart2 = go.Bar(x=df['NOC'], y=df['Silver'], name='Silver', marker={'color': '#9EA0A1'})
bar_chart3 = go.Bar(x=df['NOC'], y=df['Bronze'], name='Bronze', marker={'color': '#CD7F32'})

data = [bar_chart, bar_chart2, bar_chart3]  # nested barchart oluşturduk

layout = go.Layout(title='Medals',
                   barmode='stack'  # nested barchart'ı stacked barchart olarak güncelledik
                   )

fig = go.Figure(layout=layout, data=data)

pyo.plot(figure_or_data=fig, filename='3-)bar-charts.html')
