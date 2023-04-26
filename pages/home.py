import dash
from dash import html, dcc

dash.register_page(__name__,title='Home')

layout = html.Div(children=[
    html.H1(children='Welcome to UniPlotter',
            style={'textAlign':'center','marginTop':'20px'}),

    html.Div(children=[
        'A dashboard which includes some of the the scripts', html.Br(), 'i have written and used during my time in SBiNLab'
    ],style={'textAlign':'center'}),

    html.Div(children='''
        A pet project by Alexander Hebbelstrup.
    ''', style={'textAlign':'center'},
        className="fixed-bottom bg-dark text-white"),


])