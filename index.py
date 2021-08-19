import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from layouts import layout1
import callbacks

""" THIS PROGRAM PY SETUP IS FROM https://dash.plot.ly/urls"""

server = app.server

### Base layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


### Routing
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return layout1

if __name__ == '__main__':
    app.run_server(debug=True)
