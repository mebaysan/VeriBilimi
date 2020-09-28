import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

# df = pd.read_csv(
#     'https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/2010SantaBarbaraCA.csv',
#     error_bad_lines=False)
df = pd.read_csv(
    'https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/2010YumaAZ.csv',
    error_bad_lines=False)

heatmap = go.Heatmap(x=df['DAY'],
                     y=df['LST_TIME'],
                     z=df['T_HR_AVG'].values.tolist(),
                     colorscale='Jet',  # renk paleti

                     )

data = [heatmap]
layout = go.Layout(title='Heatmap')
fig = go.Figure(layout=layout, data=data)

pyo.plot(figure_or_data=fig, filename='8-)heatmaps.html')
