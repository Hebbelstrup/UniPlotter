import base64
import io
import dash
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy import optimize
from sklearn.metrics import r2_score
from dash import dcc,callback
from dash import html
from dash.dependencies import Input, Output, State





dash.register_page(__name__, title='Calenders')

layout = html.Div(children=[html.H1('Overview of calenders for SBiNLab',style={'textAlign': 'center', 'marginTop': 40, 'marginBottom': 20}),
                            html.Iframe(
                                src='https://teamup.com/ks2c34d39bb683096a',
                                style={'border':'O','width':'1400px','height':'1000px'},className="d-grid gap-2 col-6 mx-auto"),
                            html.Iframe(
                                src='https://teamup.com/ksk3sa262qd9msry66',
                                style={'border': 'O', 'width': '1400px', 'height': '1000px'},className="d-grid gap-2 col-6 mx-auto"),
                            html.Iframe(
                                src='https://teamup.com/ksiam57om3ixp4tjwr',
                                style={'border': 'O', 'width': '1400px', 'height': '1000px'},
                                className="d-grid gap-2 col-6 mx-auto")



]),



