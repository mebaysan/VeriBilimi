import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
app.head = [
    html.Link(
        href='https://baysansoft.com/media/web/logo-siyah-bg-mor-kirmizi_Rx96Qm3.png',
        rel='icon'
    ),
]
app.title = "Baysan's Worksheet"

df = pd.read_csv('attacks_data.csv')  # https://www.kaggle.com/argolof/predicting-terrorism
DF = df.copy()


def get_pie(df, value, name, title):
    return px.pie(df,
                  values=value,
                  names=name,
                  hover_data=['Injured', 'Description'],
                  title=title,
                  color_discrete_sequence=px.colors.sequential.RdBu,
                  height=600

                  ).update_traces(
        textinfo='percent+label')


def get_cities_from_country(df, country_name):
    return [{'label': f'{city}', 'value': city} for city in df.query(f'Country == "{country_name}"')['City'].unique()]


app.layout = html.Div(
    children=[
        html.H1("Baysan's Plotly Dash Worksheet", style={'text-align': 'center', 'color': 'red'}),
        html.Label('Select Country'),
        dcc.Dropdown(
            id='country-dropdown',
            options=[
                {'label': f'{country}', 'value': country} for country in df['Country'].unique()
            ],
            searchable=True,
            multi=False,
            placeholder='Select Country...',
        ),
        html.Label('Select City'),
        dcc.Dropdown(
            id='city-dropdown',
            searchable=True,
            multi=False,
            placeholder='Select City...',
        ),
        dcc.Graph(
            id='attack-pie'
        ),
    ],
)


@app.callback(
    [dash.dependencies.Output('attack-pie', 'figure'),
     dash.dependencies.Output('city-dropdown', 'options')],
    [dash.dependencies.Input('country-dropdown', 'value'),
     dash.dependencies.Input('city-dropdown', 'value'), ])
def get_country(country=None, city=None):
    if country and city:
        return get_pie(DF.query(f"Country == '{country}'").query(f'City == "{city}"'), 'Killed', 'City',
                       f'Religious Terrorist Attacks based on {city}'), get_cities_from_country(DF, country)
    elif country:
        return get_pie(DF.query(f"Country == '{country}'"), 'Killed', 'City',
                       f'Religious Terrorist Attacks based on {country}\'s Cities'), get_cities_from_country(DF,
                                                                                                             country)
    else:
        return get_pie(DF, 'Killed', 'Country', 'Religious Terrorist Attacks based on Country'), [
            {'label': 'Please Choose Country', 'value': 'Please Choose Country', 'disabled': True}]


if __name__ == '__main__':
    app.run_server(debug=True)
