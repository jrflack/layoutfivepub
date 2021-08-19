from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_table
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import math
import abc
from app import app
import base64
# TODO update this name
import json
import ezdxf
from ezdxf.filemanagement import dxf_stream_info
import io
import urllib
import urllib.parse
from tempfile import NamedTemporaryFile

from ezdxf.math import Vector
# import os



@app.callback(
    [
        Output('hub-results-table', 'children'),
        Output('bearing-results-table', 'children'),
    ],
    [Input('calc-bending-moment', 'n_clicks')],
    [
        State('general-arrangement-dims', 'data'),
        State('stress-concentrations', 'data'),
        State('design-criteria-table', 'data'),
        State('load-two-table', 'data')
     ]
)
def Calculate_Automatic_Results(
        n_clicks,
        general_arrangement_dims,
        stress_concentrations,
        design_criteria_table2,
        loads
                                ):
    # Don't update callback when program loads first time to prevent None types being returned:
    if n_clicks is None:
       raise PreventUpdate

    dummy_shaft_table_data = [
        dict(Component='Selected Shaft Material', Result='to be programmed 1'),
        dict(Component='Selected Shaft Yield Stress (MPa)', Result='to be programmed 1'),
    ]

    # Create DataFrame.
    dummy_shaft_table_df = pd.DataFrame(dummy_shaft_table_data)

    # extract data/rows and columns
    columns = [{"name": i, "id": i, } for i in (dummy_shaft_table_df.columns)]
    data = dummy_shaft_table_df.to_dict('rows')

    # Create a dash datatable
    dummy_shaft_results_table = dash_table.DataTable(data=data, columns=columns,
                                       style_as_list_view=True,
                                       style_cell={'textAlign': 'center',
                                                   'minWidth': '0px', 'width': '200px', 'maxWidth': '200px',
                                                   'overflow': 'hidden',
                                                   'textOverflow': 'ellipsis',
                                                   'font-family': 'sans-serif',
                                                   },
                                       style_cell_conditional=[
                                           {
                                               'if': {'column_id': 'Component'},
                                               'textAlign': 'left'
                                           }
                                       ]
                                       )


    dummy_table_data = [
        dict(Component='Selected Bearing Manufacturer', Result='to be programmed 1'),
        dict(Component='Bearing Life (Hrs)', Result='to be programmed 3'),
    ]

    # Create DataFrame.
    dummy_table_df = pd.DataFrame(dummy_table_data)

    # extract data/rows and columns
    columns = [{"name": i, "id": i, } for i in (dummy_table_df.columns)]
    data = dummy_table_df.to_dict('rows')

    # Create a dash datatable
    dummy_table = dash_table.DataTable(data=data, columns=columns,
                                         style_as_list_view=True,
                                         style_cell={'textAlign': 'center',
                                                     'minWidth': '0px', 'width': '200px', 'maxWidth': '200px',
                                                     'overflow': 'hidden',
                                                     'textOverflow': 'ellipsis',
                                                     'font-family': 'sans-serif',
                                                     },
                                         style_cell_conditional=[
                                             {
                                                 'if': {'column_id': 'Component'},
                                                 'textAlign': 'left'
                                             }
                                         ]
                                         )


    return dummy_table, dummy_shaft_results_table






