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
from github import Github



dash.register_page(__name__, title='Buffer')

layout = html.Div('Work in progress')



