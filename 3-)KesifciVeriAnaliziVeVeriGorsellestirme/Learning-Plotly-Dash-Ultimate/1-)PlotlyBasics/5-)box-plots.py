import plotly.graph_objects as go
import plotly.offline as pyo
import numpy as np

y = [1, 14, 14, 15, 16, 18, 18, 19, 19, 20, 20, 23, 24, 26, 27, 27, 28, 29, 33, 54]
box = go.Box(y=y,
             # boxpoints='all',  # tüm y değerlerine ait noktaları gösterir
             boxpoints='outliers',  # yalnızca uç (aykırı) değerlere ait noktaları gösterir
             jitter=0.3,
             pointpos=0,  # y değerlerine ait noktaların nerede pozisyon alacağını gösterir
             name='y'
             )

y2 = np.random.randint(0, 100, 20)
box2 = go.Box(y=y2,
              boxpoints='all',
              jitter=0.3,
              pointpos=0,
              name='y2'
              )

y3 = np.random.randint(0, 200, 20)
box3 = go.Box(y=y3,
              boxpoints='all',
              jitter=0.3,
              pointpos=0,
              name='y3'
              )

data = [box, box2, box3]
layout = go.Layout(title='Boxplots')
fig = go.Figure(data=data, layout=layout)

pyo.plot(figure_or_data=fig, filename='5-)box-plots.html')
