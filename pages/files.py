import dash
from dash import html, dcc

dash.register_page(__name__,title='Files')

layout = html.Div(children=[
    html.H1(children='Placeholder for file section'),

    html.Div(children='''
        placeholder to have files
    '''),

])