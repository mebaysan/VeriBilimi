import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

my_input = dcc.Input(id='my-input',  # component id'si
                     type='text',  # input tipi
                     placeholder='Aramak İstediğiniz Metni Girin...',  # input box boş ise ne yazacak
                     debounce=True,  # enter'a basmadan kutuya her girileni post etmesin
                     value=''  # başlangıç değeri
                     )

LAYOUT = html.Div(children=[
    html.H1('Dropdown Çalışması', style={
        'textAlign': 'center',
        'color': 'red',
    }),
    my_input,
    html.H4(id='my-output') # hedef component'imiz
])

app.layout = LAYOUT


@app.callback(
    dash.dependencies.Output(component_id="my-output", component_property="children"),
    dash.dependencies.Input("my-input", "value"),
)
def set_value(value): # Input alacağımız componenti set ettikten sonra callback çağrıldığında bu fonksiyona parametre olarak component_property gelecek
    if value:
        return f'Aradığınız kelime -> {value}' # Hedef component'imizin children özelliğine stringi return ediyoruz


if __name__ == '__main__':
    app.run_server()
