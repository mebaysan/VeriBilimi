import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px  # yüksek seviyeli grafik arayüzü
import seaborn as sns

app = dash.Dash()
tips = sns.load_dataset('tips')
df = tips.copy()

fig = px.scatter(x='total_bill', y='tip', color='smoker', size='total_bill', data_frame=df, text='tip',
                 title='Toplam hesaba göre bahşiş oranı')

LAYOUT = html.Div(
    children=[
        html.H1('Hello Dash!!', style={'textAlign': 'center', 'color': 'red'}),
        html.Div('Dash Data Driven Development!'),
        dcc.Graph(
            id='my-first-graph',
            figure=fig
        )
    ]
)
app.layout = LAYOUT

if __name__ == '__main__':
    app.run_server()
