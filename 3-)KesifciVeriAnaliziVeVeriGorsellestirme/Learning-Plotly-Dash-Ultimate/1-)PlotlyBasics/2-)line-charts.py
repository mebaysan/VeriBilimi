import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

np.random.seed(56)

x_values = np.linspace(0, 1, 100)
y_values = np.random.rand(100)

trace1 = go.Scatter(x=x_values, y=y_values + 5,
                    mode='markers', name='markers')

trace2 = go.Scatter(x=x_values, y=y_values,
                    mode='lines', name='lines')

trace3 = go.Scatter(x=x_values, y=y_values - 5,
                    mode='lines+markers', name='lines+markers')

data = [trace1, trace2, trace3]

layout = go.Layout(title='Line Charts')

fig = go.Figure(layout=layout, data=data)

pyo.plot(figure_or_data=fig, filename='2-)line-charts.html')
