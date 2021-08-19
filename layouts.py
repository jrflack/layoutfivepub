# from pydoc import classname

import dash_core_components as dcc
import dash_html_components as html
import dash_table
# from textwrap import dedent as s
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from app import app
from text_store import *


# Layout styles:


board_group_style = {
    "background-color": "rgb(260, 260, 260)",
    "border-radius": "5px",
    'border': '1px solid rgb(190, 190, 190)',
    "box-shadow": "4px 4px 4px lightgrey",
    "padding": "5px",
    "margin": "20px 40px",  # top/ bottom sides I think
}

input_group_style = {"background-color": "#f9f9f9",
                     ######### OLD
                     "border-radius": "5px", ''
                                             'border': '1px solid #d9d9d9',
                     "position": "relative",
                     "box-shadow": "4px 4px 4px lightgrey",
                     "padding": "5px"}

input_group_container_style = {"background-color": "rgb(260, 260, 260)",
                               ########### OLD
                               "border-radius": "5px",
                               'border': '1px solid rgb(190, 190, 190)',
                               "position": "relative",
                               "box-shadow": "4px 4px 4px lightgrey",
                               "padding": "5px",
                               "margin": "20px 40px",  # top/ bottom sides I think
                               "justify-content": "space-around",
                               "display": "flex",
                               "align-items": "flex-start"
                               # this enables all children to be treated as self adjusting columns, ie if theres 3 children
                               # there will be 3 equally spaced columns
                               # NOTE: edit the style dictionary of the children so width = 1 / n_columns where n_columns is number
                               # of columns/ children of this parent
                               }

input_side_container_style = {"background-color": "rgb(260, 260, 260)",
                              "padding": "2px",
                              # 'border': '1px solid #d9d9d9',
                              "box-sizing": "border-box",
                              "width": "25%",
                              "margin": "5px 1px",
                              "display": "grid",
                              "grid-template-columns": "2fr 1fr"

                              }

input_box_style = "eleven columns"  # old

layout1 = html.Main(
    style={
        'margin': '0px 0px',
        'padding': '0px'
    },
    children=[

        ########### HEADER ########################################################################################
        html.Header(
            (
                html.Div(
                    children=[
                        html.H3(title_text,
                                style={
                                    'margin-bottom': '0.5rem',
                                }),
                        html.H6(version_text),

                    ]
                ),


            ),
            className="container",
            style={
                "display": "flex",
                "flex-direction": "row",
                "justify-content": "space-between",
                "align-items": "center",
                # "background-image": "url('/dashboard/assets/preffered_banner7.png')",
                "background-color": "var(--color-off-black)",
                # "background-image": "radial-gradient(farthest-side at 60% 85%, rgb(0, 77, 153), rgb(20, 20, 20))",
                "color": "#fff",
                'margin': '0px 0px',
                "padding-top": "0rem",
                "padding-bottom": "0rem",
                "height": "125px",
            },
        ),

        ######### END HEADER

        ########### TAB INPUT BOXES  ########################################################################################

        html.Div(
            className="block container",
            children=[
                html.H4("General Information"),
                html.Div(
                    className="GroupContainer",
                    style={
                        # "margin-bottom": "5px",
                        # 'display': 'grid',
                        # 'grid-template-columns': '1fr 1fr',
                        # 'grid-column-gap': '1%',
                        'textAlign': 'left',
                        'margin': '0px'
                           },
                    children=[
                        dcc.Markdown(
                            """
                            This is a general layout of a program in development.
                            * The layout takes inputs
                            * The layout it then data crunches the inputs, and returns graphs.
                            """,
                        ),

                    ],
                ),
            ],
        ),


        html.Div(
            className="block container",
            children=[
                html.H4("Arrangement Input Data"),
                dcc.Tabs(
                    id="tabs",
                    content_className="TabGroupContainer",
                    children=[
                        dcc.Tab(
                            label="Pulley General Arrangement",
                            children=[
                                html.H4("Enter dimensions",
                                        style={
                                            # "display": "flex",
                                            'textAlign': 'center',
                                        },
                                        ),
                                html.Div(
                                    className="Container",
                                    style={
                                        # "display": "flex",
                                        # "flex-direction": "column",
                                        # "justify-content": "center",
                                        'display': 'grid',
                                        'grid-template-columns': '1fr 3fr',
                                        # 'grid-template-rows': '1fr 1fr',
                                        'grid-column-gap': '1%',
                                        'textAlign': 'center',
                                        'margin': '0px'
                                    },
                                    children=[
                                        html.Div(
                                            style={
                                                "display": "flex",
                                                "justify-content": "center",
                                            },
                                            children=[
                                                dash_table.DataTable(
                                                    id='general-arrangement-dims',
                                                    editable=True,
                                                    # width = '75%',
                                                    style_table={
                                                        'width': 'auto',
                                                        # 'textAlign': 'center',
                                                        # 'overflowY': 'scroll',
                                                        'border': 'thin lightgrey solid',

                                                    },
                                                    style_cell={
                                                        'textAlign': 'center',
                                                        'backgroundColor': 'rgb(255, 255, 255)',
                                                        'font-family': 'sans-serif',
                                                        'width': '7%'
                                                    },
                                                    style_cell_conditional=[
                                                        {'if': {'column_id': 'id_name'},
                                                         'display': 'None'},
                                                    ],
                                                    style_data_conditional=[
                                                        {'if': {'column_editable': True},
                                                         'color':'rgb(0, 0, 230)',
                                                         'background-color': 'var(--color-off-white)',
                                                         },
                                                    ],
                                                    columns=(
                                                            [{'id': 'Description', 'name': 'Description',
                                                              'editable': False}] +
                                                            [{'id': 'Value', 'name': 'Value', 'editable': True}] +
                                                            [{'id': 'id_name', 'name': 'id_name', 'editable': True}]
                                                    ),
                                                    # IF YOU UPDATE THIS YOU UPDATE THE SHAFTDESIGN.PY CODE
                                                    # hidden_columns = ['id_name'],
                                                    data=[
                                                        {'Description': 'Bearing Centres (m)', 'Value': '2.3',
                                                         'id_name': 'C'},
                                                        {'Description': 'Face Width (m)',
                                                         'Value': '1.8', 'id_name': 'FW'},
                                                        {'Description': 'Hub Centres (m)',
                                                         'Value': '1.66', 'id_name': 'hub_cntrs'},
                                                        {'Description': 'Dia Overlagging (m)',
                                                         'Value': '.678', 'id_name': 'dia_OL'},
                                                        {'Description': 'Lagging Thickness (mm)',
                                                         'Value': '16', 'id_name': 't_lag'},
                                                        {'Description': 'Shaft Ext LHS (m)',
                                                         'Value': '.08', 'id_name': 'T'},
                                                        {'Description': 'Dim \'A\' (m)',
                                                         'Value': '0.2', 'id_name': 'Z'},
                                                        {'Description': 'Dim \'B\' (m)',
                                                         'Value': '0.167', 'id_name': 'dim_B'},
                                                        {'Description': 'Dim \'C\' (m)',
                                                         'Value': '0.15', 'id_name': 'dim_C'},
                                                        {'Description': 'Drive Extension (m)',
                                                         'Value': '0.15', 'id_name': 'L_drive'},
                                                        {'Description': 'Belt Width (m)',
                                                         'Value': '1.6', 'id_name': 'BW'},
                                                    ],
                                                ),
                                            ],
                                        ),

                                        html.Div(
                                            style={
                                                "textAlign": "center"
                                            },
                                            children=[
                                                html.Img(
                                                    src=app.get_asset_url('pulley_dims_input_good.jpg'),
                                                    style={
                                                        "margin-top": "5px",
                                                        "margin-bottom": "5px",
                                                        "width": "90%",
                                                    }
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        dcc.Tab(
                            label="Shaft Stress Concentrations",
                            children=[
                                html.Div(
                                    className="Container",
                                    style={
                                        "display": "flex",
                                        "flex-direction": "column",
                                        "justify-content": "center",
                                        "textAlign": "center"
                                    },
                                    children=[
                                        dcc.Markdown(
                                            """ Shaft calculations are undertaken in accordance with AS1403.
                                             The software will automatically calculate shaft diameter change stress concentrations where the user inputs "radius".
                                             The software (currently) will calculate bearing and hub stress concentrations based on K factors of 2 and 3 respectivly where the user inputs "bearing" and "hub".
                                             Programming is in progress to calculate the stress concentrations based on AS1403 for user selected bearing and hub fit selections.
                                            """
                                        ),
                                        html.Div(
                                            style={
                                                "textAlign": "center"
                                            },
                                            children = [
                                                html.Img(
                                                    src=app.get_asset_url('Kvalues1.jpg'),
                                                    style={
                                                        "margin-top": "10px",
                                                        "margin-bottom": "10px",
                                                        "width": "60%",
                                                        "textAlign": "center"
                                                    }
                                                ),
                                            ],
                                        ),
                                        html.H6("Enter description of stress concentration. Values entered must be "
                                                "\"end\", \"hub\", \"radius\" or \"drive\"",
                                                style={
                                                    # "display": "flex",
                                                    'textAlign': 'center',
                                                },
                                                ),
                                        html.Div(
                                            style={
                                                "display": "flex",
                                                "justify-content": "center",
                                            },
                                            children=[
                                                dash_table.DataTable(
                                                    id='stress-concentrations',
                                                    editable=True,
                                                    # width = '75%',
                                                    style_table={
                                                        'width': '900px',
                                                        # 'textAlign': 'center',
                                                        # 'overflowY': 'scroll',
                                                        'border': 'thin lightgrey solid',

                                                    },
                                                    style_cell={
                                                        'textAlign': 'center',
                                                        'backgroundColor': 'rgb(255, 255, 255)',
                                                        'font-family': 'sans-serif',
                                                        'width': '7%'
                                                    },
                                                    # style_cell_conditional=[
                                                    #     {'if': {'column_id': 'Dimension_Reference'},
                                                    #      'width': '10%'},
                                                    # ],
                                                    style_data_conditional=[
                                                        {'if': {'column_editable': True},
                                                         'color':'rgb(0, 0, 230)',
                                                         'background-color': 'var(--color-off-white)',
                                                         },
                                                    ],
                                                    columns=(
                                                            [{'id': 'K_ID', 'name': 'Stress Concentration ID:',
                                                              'editable': False}] +
                                                            [{'id': 'K0', 'name': 'K0', 'editable': True}] +
                                                            [{'id': 'K1', 'name': 'K1', 'editable': True}] +
                                                            [{'id': 'K2', 'name': 'K2', 'editable': True}] +
                                                            [{'id': 'K3', 'name': 'K3', 'editable': True}] +
                                                            [{'id': 'K4', 'name': 'K4', 'editable': True}] +
                                                            [{'id': 'K5', 'name': 'K5', 'editable': True}] +
                                                            [{'id': 'K6', 'name': 'K6', 'editable': True}] +
                                                            [{'id': 'K7', 'name': 'K7', 'editable': True}] +
                                                            [{'id': 'K8', 'name': 'K8', 'editable': True}] +
                                                            [{'id': 'K9', 'name': 'K9', 'editable': True}] +
                                                            [{'id': 'K10', 'name': 'K10', 'editable': True}] +
                                                            [{'id': 'K11', 'name': 'K11', 'editable': True}]
                                                    ),
                                                    data=[
                                                        {
                                                            # 'id':'dimension',
                                                            # 'name':'dimension',
                                                            'K_ID': 'Description',
                                                            'K0': 'end',
                                                            'K1': 'bearing',
                                                            'K2': 'radius',
                                                            'K3': 'hub',
                                                            'K4': 'radius',
                                                            'K5': 'radius',
                                                            'K6': 'hub',
                                                            'K7': 'radius',
                                                            'K8': 'bearing',
                                                            'K9': 'radius',
                                                            'K10': 'drive',
                                                            'K11': 'end',
                                                        },
                                                    ],
                                                ),
                                            ]
                                        ),

                                    ],
                                ),
                            ],
                        ),
                        dcc.Tab(
                            label="Loads",
                            children=[
                                html.Div(
                                    className="Container",
                                    style={
                                        'display': 'grid',
                                        'grid-template-columns': '1fr 1fr 1fr',
                                        # 'grid-template-rows': '1fr 1fr',
                                        'grid-column-gap': '1%',
                                        'textAlign': 'center',
                                        'margin': '0px'
                                    },
                                    children=[
                                        html.Div(
                                            style={
                                                "display": "flex",
                                                "justify-content": "center",
                                            },
                                            children=[
                                                dash_table.DataTable(
                                                    id='load-two-table',
                                                    editable=True,
                                                    # width = '75%',
                                                    style_table={
                                                        # 'width': '900px',
                                                        'width': 'auto',
                                                        # 'textAlign': 'center',
                                                        # 'overflowY': 'scroll',
                                                        'border': 'thin lightgrey solid',

                                                    },
                                                    style_cell={
                                                        'textAlign': 'center',
                                                        'backgroundColor': 'rgb(255, 255, 255)',
                                                        'font-family': 'sans-serif',
                                                        # 'width': '7%'
                                                        'width': 'auto'
                                                    },
                                                    # style_cell_conditional=[
                                                    #     {'if': {'column_id': 'Dimension_Reference'},
                                                    #      'width': '10%'},
                                                    # ],
                                                    style_data_conditional=[
                                                        {'if': {'column_editable': True},
                                                         'color': 'rgb(0, 0, 230)',
                                                         'background-color': 'var(--color-off-white)',
                                                         },
                                                    ],
                                                    columns=(
                                                            [{'id': 'Load_Description', 'name': 'Load Description',
                                                              'editable': False}] +
                                                            [{'id': 'Value', 'name': 'Value', 'editable': True}]
                                                    ),
                                                    # IF YOU UPDATE THIS YOU UPDATE THE SHAFTDESIGN.PY CODE
                                                    data=[
                                                        {'Load_Description': 'T1 running (kN)', 'Value': '56.2',
                                                         'name': 'T1_run'},
                                                        {'Load_Description': 'T2 running (kN)',
                                                         'Value': '23.8', 'name': 'T2_run'},
                                                        {'Load_Description': 'T1 starting (kN)',
                                                         'Value': '60', 'name': 'T1_srt'},
                                                        {'Load_Description': 'T2 starting (kN)',
                                                         'Value': '25', 'name': 'T2_srt'},
                                                        {'Load_Description': 'Drive torque running (kNm)',
                                                         'Value': '-13.7', 'name': 'Tq_op'},
                                                        {'Load_Description': 'Overhung load running (kN)',
                                                         'Value': '12.9', 'name': 'P_op'},
                                                        {'Load_Description': 'Direction of overhung load (deg)', 'Value': '270',
                                                         'name': 'P_theta'},
                                                        {'Load_Description': 'Angle of T1 (deg)', 'Value': '180',
                                                         'name': 'T1_theta'},
                                                        {'Load_Description': 'Angle of T2 (deg)', 'Value': '180',
                                                         'name': 'T2_theta'},
                                                    ],
                                                ),
                                            ]),
                                        html.Div(
                                            style={
                                                "textAlign": "center"
                                            },
                                            children=[
                                                html.Img(
                                                    src=app.get_asset_url('OL_theta.jpg'),
                                                    style={
                                                        "margin-top": "10px",
                                                        "margin-bottom": "10px",
                                                        "width": "75%",
                                                    }
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            style={
                                                "textAlign": "center"
                                            },
                                            children=[
                                                html.Img(
                                                    src=app.get_asset_url('T_theta.jpg'),
                                                    style={
                                                        "margin-top": "10px",
                                                        "margin-bottom": "10px",
                                                        "width": "75%",
                                                    }
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),


                        dcc.Tab(
                            label="Design Criteria",
                            children=[
                                html.Div(
                                    className="Container",
                                    style={
                                        "display": "flex",
                                        "flex-direction": "column",
                                        "justify-content": "center",
                                    },
                                    children=[
                                        html.Div(
                                            style={
                                                "display": "flex",
                                                "justify-content": "center",
                                            },
                                            children=[
                                                dash_table.DataTable(
                                                    id='design-criteria-table',
                                                    editable=True,
                                                    # width = '75%',
                                                    style_table={
                                                        # 'width': '900px',
                                                        'width': 'auto',
                                                        # 'textAlign': 'center',
                                                        # 'overflowY': 'scroll',
                                                        'border': 'thin lightgrey solid',

                                                    },
                                                    style_cell={
                                                        'textAlign': 'center',
                                                        'backgroundColor': 'rgb(255, 255, 255)',
                                                        'font-family': 'sans-serif',
                                                        # 'width': '7%'
                                                        'width': 'auto'
                                                    },
                                                    # style_cell_conditional=[
                                                    #     {'if': {'column_id': 'Dimension_Reference'},
                                                    #      'width': '10%'},
                                                    # ],
                                                    style_data_conditional=[
                                                        {'if': {'column_editable': True},
                                                         'color': 'rgb(0, 0, 230)',
                                                         'background-color': 'var(--color-off-white)',
                                                         },
                                                    ],
                                                    columns=(
                                                            [{'id': 'Design_Criteria','name': 'Design_Criteria', 'editable': False}] +
                                                            [{'id': 'DC_Value', 'name': 'Value', 'editable': True}]
                                                            # [{'id': 'M', 'name': 'M', 'editable': False}]
                                                    ),
                                                    # IF YOU UPDATE THIS YOU UPDATE THE SHAFTDESIGN.PY CODE
                                                    data=[
                                                        {'Design_Criteria': 'Shaft Safety Factor','DC_Value' : '1.2', 'name':'FS'},
                                                        {'Design_Criteria': 'Shaft Ultimate Stress (MPa)','DC_Value' : '850' , 'name':'FU'},
                                                        {'Design_Criteria': 'Shaft Endurance Limit Stress (MPa)','DC_Value' : '380', 'name':'FR'},
                                                        {'Design_Criteria': 'Maximum Shaft Deflection 1 / ','DC_Value' : '2000', 'name':'Defl'},
                                                        {'Design_Criteria': 'Maximum Shaft Slope At Bearing (deg)','DC_Value' : '0.5', 'name':'max_slope_b'},
                                                        {'Design_Criteria': 'Maximum Shaft Slope At Hub (rad)','DC_Value' : '0.00145', 'name':'max_slop_hub'},
                                                        {'Design_Criteria': 'Minimum Bearing Life (Hrs)','DC_Value' : '100000', 'name':'b_life'},
                                                        {'Design_Criteria': 'Pulley rpm','DC_Value' : '60', 'name':'rpm'},
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),



        ######################### END INPUT BOXES #########################


        html.Div(
            style={'fontsize': 30,
                   'textAlign': 'center',
                   "justify-content": "center"
                   },
            children=[
                html.Button(id='calc-bending-moment',
                            n_clicks=0,
                            children='Calculate',
                            style={'fontsize': 30,
                                   'background-color': '#33C3F0',
                                   'color': 'rgb(255, 255, 255)',
                                   # 'textAlign': 'center',
                                   "justify-content": "center"
                                   }
                            ),
            ],
        ),



        html.Div(
            className="block container",
            children=[
                html.Div(
                    className="GroupContainer",
                    children=[
                        html.H4("Preliminary Component Selection Results",
                                style={
                                    "textAlign": "center",
                                    "textAlign": "center",
                                }
                                ),
                        html.Div(
                            style={
                                'display': 'grid',
                                'grid-template-columns': '1fr 1fr',
                                'textAlign': 'center',
                                'padding': '0px',
                                'margin': '0px',
                                # 'background-color': 'rgb(245, 245, 245)'
                            },
                            children = [
                                html.Div(id='hub-results-table',
                                         style={"margin-bottom": "10px",
                                                "display": "flex",
                                                "justify-content": "center"
                                                }
                                         ),
                                html.Div(id='bearing-results-table',
                                         style={"margin-bottom": "10px",
                                                "display": "flex",
                                                "justify-content": "center"
                                                }
                                         ),
                            ],
                        ),

                    ],
                ),
            ],
        ),

        html.Div(
            id='current-housing-data-for-storage',
            style={
                'display': 'none',
            },
        ),
        html.Div(
            id='current-hub-data-for-storage',
            style={
                'display': 'none',
            },
        ),



                html.Div(
                            className="block container",
                            children=[
                            html.Div([]),
                            # html.P(legal_text),
                            html.H5(copyright_text)
                            ]
                        )

    ])
############ END LAYOUT 1 ############################################################


# Setup layout parameters
layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="rgb(30, 30, 30)",
    paper_bgcolor="rgb(30, 30, 30)",
    # paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Satellite Overview",
    mapbox=dict(
        style="light",
        center=dict(lon=-78.05, lat=42.54),
        zoom=7,
    ),
)

