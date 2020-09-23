import dash
import dash_core_components as dcc  # çekirdek dash componentleri için gerekli (dropdown vb.)
import dash_html_components as html  # HTML component'leri için gerekli (H1, Div vb.)

app = dash.Dash()  # bir dash uygulaması oluşturuyoruz

LAYOUT = html.Div(
    children=[
        html.H1('Hello Dash!!'),
        html.Div('Dash Data Driven Development!')
    ]
) # dash html component'lerinden bir Div oluşturuyoruz

app.layout = LAYOUT # oluşturduğumuz app'in layout'una LAYOUT'u yerleştiriyoruz

if __name__ == '__main__':
    app.run_server()
