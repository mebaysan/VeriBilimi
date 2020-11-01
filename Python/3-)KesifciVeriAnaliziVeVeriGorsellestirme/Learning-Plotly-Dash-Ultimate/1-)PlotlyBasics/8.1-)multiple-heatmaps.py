import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

df = pd.read_csv(
    'https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/2010SitkaAK.csv',
    error_bad_lines=False)
df2 = pd.read_csv(
    'https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/2010SantaBarbaraCA.csv',
    error_bad_lines=False)
df3 = pd.read_csv(
    'https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/2010YumaAZ.csv',
    error_bad_lines=False)

trace1 = go.Heatmap(x=df['DAY'],
                    y=df['LST_TIME'],
                    z=df['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',
                    zmin=5,
                    zmax=40
                    )
trace2 = go.Heatmap(x=df2['DAY'],
                    y=df2['LST_TIME'],
                    z=df2['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',
                    zmin=5,
                    zmax=40
                    )
trace3 = go.Heatmap(x=df3['DAY'],
                    y=df3['LST_TIME'],
                    z=df3['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',
                    zmin=5,
                    zmax=40
                    )

data = [trace1, trace2, trace3]
layout = go.Layout(title='Multiple Heatmaps')
fig = make_subplots(rows=1, cols=3,
                    shared_yaxes=True,  # kaç satır kaç sütun ve y ekseni paylaşılsın mı
                    subplot_titles=['Sitka AK', 'SantaBarbara CA',
                                    'Yuma AZ'],  # subplot'ların isimleri

                    )
fig.add_trace(trace1, row=1, col=1)
fig.add_trace(trace2, row=1, col=2)
fig.add_trace(trace3, row=1, col=3)
fig['layout'].update(title='Temps for 3 cities')
pyo.plot(figure_or_data=fig, filename='8.1-)multiple-heatmaps.html')
