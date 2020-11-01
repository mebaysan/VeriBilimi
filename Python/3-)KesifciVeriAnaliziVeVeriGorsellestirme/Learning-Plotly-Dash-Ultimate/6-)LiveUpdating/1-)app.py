import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash()

crash_free = 0

app.layout = html.Div([
    html.H1(id='live-update-text'),
    dcc.Interval(id='interval-component',
                 interval=2000,  # 2 saniyede bir yenilenecek
                 n_intervals=0  # başlangıç değeri
                 )
])


@app.callback(Output('live-update-text', 'children'), Input('interval-component', 'n_intervals'))
def update_layout(n):
    toplam = 0
    toplam += n * 2000
    return f"{n} kere yenilendi! Toplam {toplam / 1000} saniye geçti!"


if __name__ == '__main__':
    app.run_server()
