import os
from werkzeug.exceptions import HTTPException
import dash
import dash

external_stylesheets = []

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__, external_stylesheets=None)
server = app.server
app.config.suppress_callback_exceptions = True
app.title = "layout_two"