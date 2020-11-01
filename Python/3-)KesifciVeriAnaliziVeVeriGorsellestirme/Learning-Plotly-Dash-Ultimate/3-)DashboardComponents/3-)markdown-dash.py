import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

markdown_text = """
### Dash and Markdown
Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/) specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
Markdown includes syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.

- A
- B
    - B.1
        - B.1.1
"""

app.layout = html.Div(children=[
    dcc.Markdown(children=[
        markdown_text
    ])
])

if __name__ == '__main__':
    app.run_server()
