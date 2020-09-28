import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
df = tips.copy()

hist = go.Histogram(x=df['total_bill'],
                    xbins=dict(start=df['total_bill'].min(),  # sütunların başlangıç değeri
                               end=df['total_bill'].max(),  # sütunların bitiş değeri
                               size=10,  # sütunlar kaçarlı gruplansın
                               ),
                    )

data = [hist]

layout = go.Layout(title='Histogram')
fig = go.Figure(layout=layout, data=data)

pyo.plot(figure_or_data=fig, filename='6-)histograms.html')
