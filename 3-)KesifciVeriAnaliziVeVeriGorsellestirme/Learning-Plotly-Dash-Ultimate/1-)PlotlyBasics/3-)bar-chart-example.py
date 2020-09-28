import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/mocksurvey.csv',
    error_bad_lines=False)

# data = [go.Bar(x=df.index, y=df[var], name=var, orientation='h') for var in df.columns]

data = [go.Bar(x=df[var], y=df.index, name=var, orientation='h') for var in df.columns]

layout = go.Layout(title='Survey Results', barmode='stack')

fig = go.Figure(data=data, layout=layout)

pyo.plot(figure_or_data=fig, filename='3-)bar-chart-example.html')
