import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd
import seaborn as sns

tips = sns.load_dataset('tips')
df = tips.copy()

data = []

for day in df['day'].unique():
    trace = go.Scatter(x=df['total_bill'], y=df[df['day'] == day]['tip'], mode='lines', name=day)
    data.append(trace)

layout = go.Layout(title='Günlere Göre Bahşiş')

fig = go.Figure(data=data)

pyo.plot(figure_or_data=fig, filename='2-)line-charts-example-tips.html')
