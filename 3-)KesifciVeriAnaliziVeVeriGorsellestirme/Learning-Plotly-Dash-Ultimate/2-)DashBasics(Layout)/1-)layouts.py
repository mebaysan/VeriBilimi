import dash  # dash uygulaması oluşturmamızı sağşayacak
import dash_core_components as dcc  # çekirdek componentler için
import dash_html_components as html  # html componentleri için

app = dash.Dash()  # bir dash uygulaması oluşturuyoruz (flask)

app.layout = html.Div(  # app'in layout'unu oluşturuyoruz
    children=[  # div componenti içerisine birden fazla component alabilir
        html.H1('Merhaba Dash!'),
        dcc.Graph(  # grafik oluşturmamızı sağlar
            id='my-chart',  # her grafiğin bir id'si olmalıdır
            figure={  # 2 parametre alır, data ve layout. layout -> nasıl görüneceği, data -> verileri
                'data': [
                    {'x': ['X Salary', 'Y Salary', 'Z Salary'], 'y': [4, 5, 6], 'type': 'bar', 'name': 'SF'},
                    {'x': ['X Salary', 'Y Salary', 'Z Salary'], 'y': [2, 7, 8], 'type': 'bar', 'name': 'NYC'}
                ],
                'layout': {
                    'title': 'My Bar Chart',
                },
            })
    ]
)

if __name__ == '__main__':  # eğer bu dosya çalışırsa
    app.run_server(debug=True, dev_tools_hot_reload=True)  # uygulamayı çalıştır
    # app.run_server()
