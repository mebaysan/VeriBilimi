import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/mpg.csv')

bubble = go.Scatter(x=df['horsepower'],
                    y=df['mpg'],
                    text=df['name'],  # bubble üzerine gelince ne yazsın
                    mode='markers',  # scatter'dan bubble yapacağımız için modu markers olarak set ediyoruz
                    marker=dict(
                        size=df['weight'] / 100,  # her gözlemin weight özelliği / 100 boyutunda olsun
                        color=df['cylinders'],  # silindir sayısına göre renklensin
                        showscale=True,  # renk paleti gözüksün
                    ),
                    )

data = [bubble]

layout = go.Layout(title='Bubble Chart', xaxis={'title': 'Horsepower'}, yaxis={'title': 'Mpg'})

fig = go.Figure(data=data, layout=layout)

pyo.plot(figure_or_data=fig, filename='4-)bubble-charts.html')
