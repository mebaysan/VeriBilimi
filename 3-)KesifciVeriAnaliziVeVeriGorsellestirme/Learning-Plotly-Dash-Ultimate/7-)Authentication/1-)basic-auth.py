import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_auth  # pip install dash-auth

AUTH_BILGILERI = [  # izin verdiğimiz giriş bilgilerini set ediyoruz
    ['username', 'password'], ['BAYSAN', '321']
]

app = dash.Dash()

auth = dash_auth.BasicAuth(app, AUTH_BILGILERI)  # app ile auth bilgilerini eşleştiriyoruz

app.layout = html.Div('Authentication Uygulaması', style={'textAlign': 'center', 'color': 'red'})

if __name__ == '__main__':
    app.run_server()
