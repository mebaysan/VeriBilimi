import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

LAYOUT = html.Div(children=[
    html.H1('Callback for Interactivity', style={'textAlign': 'center', 'color': 'red'}),
    dcc.Input(id='my-input', type='text', placeholder='Placeholder..'),
    html.Div(id='my-result-div')
])

app.layout = LAYOUT


@app.callback( # callback decoratoru içerisine tetiklenecek fonksiyonları yazarız
    Output(component_id='my-result-div', component_property='children'), # önce çıktıyı nereye vereceğiz, hangi id'nin hangi özelliğine
    Input('my-input', 'value') # girdiği nerden alacağız, hangi id'nin hangi özelliği
)
def my_callback(value):
    if value: return f"Girdiğiniz string: {value}"


if __name__ == '__main__':
    app.run_server()
