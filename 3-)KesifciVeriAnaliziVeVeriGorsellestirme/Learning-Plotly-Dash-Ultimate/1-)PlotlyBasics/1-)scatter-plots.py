"""
İki değişken arasındaki ilişkiyi göstermek için kullanırız.
"""
import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [go.Scatter(x=random_x,  # x ekseni data
                   y=random_y,  # y ekseni data
                   mode='markers',  # scatter tipi (lines, markers, lines+markers)
                   marker=dict(size=12,
                               color='rgb(51,204,153)',
                               symbol='pentagon',
                               line=dict(width=2)
                               )  # işaretleyicilerin (markers) özelliklerini set ediyoruz (opsiyonel)
                   )  # Scatter plot oluşturuyoruz
        ]  # istediğimiz kadar plot koyabiliriz içeriye

layout = go.Layout(  # bir Layout hazırlıyoruz
    title='Random X and Random Y Correlation with Scatter Plot',
    xaxis={'title': 'Random X'},
    yaxis=dict(title='Random Y'),
    hovermode='closest',
)

fig = go.Figure(layout=layout, data=data)  # oluşacak figür'ün özelliklerini kendi hazırladıklarımız ile set ediyoruz

pyo.plot(fig,  # oluşturduğumuz figürü veriyoruz
         filename='1-)scatter-plots.html'  # çıktı dosyasının adı
         )  # html olarak oluşturduğumuz figürü verir
