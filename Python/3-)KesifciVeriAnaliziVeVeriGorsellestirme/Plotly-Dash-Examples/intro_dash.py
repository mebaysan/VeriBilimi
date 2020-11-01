import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import seaborn as sns

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = sns.load_dataset('tips')

fig = px.bar(df, x="day", y="tip", color="time",
             range_y=(0,50),
             title='Günlere Göre Öğünlerdeki Bahşiş Grafiği',
             labels={'day': 'Günler', 'tip': 'Bahşiş', 'time': 'Öğünler'},
             barmode='group')

fig2 = px.scatter(df, x="total_bill", y="tip", color="smoker",
             title='Sigara İçenlerin Toplam Hesap Tutarına Göre Bahşiş Grafiği',
             labels={'total_bill': 'Toplam Hesap', 'tip': 'Bahşiş', 'smoker': 'Sigara Durumu'},
             )



colors = {
    'text': '#ffffff',
    'header-background': '#333538',
    'left-background': '#FF6384',
    'right-background': '#36A2EB',
}

header = html.H1('Plotly Worksheet by Baysan', style={
    'color': colors['text'],
    'text-align': 'center',
    'border-style': 'dotted',
    'background-color': colors['header-background'],
})

left = html.Div(
    html.Div(children=[
dcc.Graph(
            id='example-graph2',
            figure=fig2
        )
    ], style={
        'float': 'left',
        'width': '50%',
        'background': colors['left-background'],
        'color': colors['text'],
    })
)

right = html.Div(
    html.Div(style={
        'float': 'right',
        'width': '50%',
        'background': colors['right-background'],
        'color': colors['text']
    }, children=[
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])
)

app.layout = html.Div(
    children=[
        header,
        left,
        right
    ],
)

if __name__ == '__main__':
    app.run_server(debug=True)
