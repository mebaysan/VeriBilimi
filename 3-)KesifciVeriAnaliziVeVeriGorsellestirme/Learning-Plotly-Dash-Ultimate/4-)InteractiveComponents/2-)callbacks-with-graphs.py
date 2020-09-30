import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

DF = pd.read_csv(
    'https://raw.githubusercontent.com/Pierian-Data/Plotly-Dashboards-with-Dash/master/Data/gapminderDataFiveYear.csv',
    error_bad_lines=False)

app = dash.Dash()

LAYOUT = html.Div(children=[
    html.H1('Callback with Graph', style={'textAlign': 'center', 'color': 'red'}),
    dcc.Dropdown(id='year-dropdown',
                 options=[{'label': str(year), 'value': year} for year in DF['year'].unique()],
                 # DF['year'] içerisindeki yıllar kadar (unique) option üretiyoruz
                 value=DF['year'].min()),  # default olarak minimum yılı alıyoruz
    dcc.Graph(id='my-chart'),
])

app.layout = LAYOUT


def create_chart(year):
    filtered_df = DF[DF['year'] == year]
    # filtered_df = DF.query(f'year == {year}') # yukarıdaki kod ile aynı işi yapmaktadır. İkisi de filtreleme yapar
    traces = []  # hatırlayalım bir figure nasıl oluşturuluyordu? data,layout ikilisi ile (https://plotly.com/python/creating-and-updating-figures/#figures-as-graph-objects)
    for continent_name in DF['continent'].unique():  # her bölge ismine ayrı olarak chart oluşturacağız
        df_by_continent = filtered_df[
            filtered_df['continent'] == continent_name]  # ilgili bölge ismine göre dataframe'i filtreliyoruz
        traces.append(go.Scatter(
            # oluşturduğumuz grafiği traces listesine ekliyoruz. Çünkü bu return ettiğimizde en nihayetinde şu şekilde olacak -> Figure('data':traces)
            x=df_by_continent['gdpPercap'],  # grafiğin x eksenine gdpPercap değişkeni gelecek
            y=df_by_continent['lifeExp'],  # y eksenine lifeExp değişkeni gelecek
            mode='markers',  # scatter çizeceğimiz için markers olarak işaretliyoruz
            opacity=0.7,
            name=continent_name,  # çizilen grafiğin adı ne olacak, yani bunu seaborn'den hue olarak düşünebiliriz
            marker={'size': 15}  # işaretleyicilerin boyutu
        ))
        layout = go.Layout(title='Custom Plot with Callback',
                           xaxis={'title': 'GDP Per Cap', 'type': 'log'},
                           yaxis={'title': 'Life Expectancy'})
    return {'data': traces, 'layout': layout}  # en nihayetinde bu şu şekli alacak Figure('data':traces,'layout':layout)


@app.callback(
    Output(component_id='my-chart', component_property='figure'),
    # my-chart id'li component'in figure özelliğine çıktı vereceğiz
    Input('year-dropdown', 'value')  # year-dropdown id'li componentten input alacağız
)
def my_callback(selected_year):
    return create_chart(selected_year)


if __name__ == '__main__':
    app.run_server()
