import dash
from dash import html, dcc, callback, Input, Output, dash_table
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
dash.register_page(__name__, title='akta')
import numpy as np

file = open('assets/Data/Akta.txt')
df = pd.read_csv(file, sep="\t", decimal = ".", header = 2, engine = 'python')
df = pd.DataFrame(df)

def get_xy(name):
    x_loc = df.columns.get_loc(name) -1
    x = df.iloc[:,x_loc]
    y = df[name]
    name = name
    return x,y,name


def plot_data():
    file = open('assets/Data/Akta.txt')
    df = pd.read_csv(file, sep="\t", decimal=".", header=2, engine='python')
    df = pd.DataFrame(df)
    fig = make_subplots(specs=[[{"secondary_y":True}]])

    for i in df.columns[1::2]:
        x,y,name = get_xy(i)
        if name =='mAU':
            fig.add_trace(go.Scatter(x=x,y=y,name=name),secondary_y=False)
        if name not in ['Fraction','Logbook','Injection','mAU']:
            fig.add_trace(go.Scatter(x=x, y=y, name=name), secondary_y=True)
        if name == 'Fraction':
            fig.add_trace(go.Scatter(x=[0, 0], y=[0, 0], mode='lines',
                                     legendgroup='Fractions', name='fractions'))
            for k,i in enumerate(x.dropna()):
                fig.add_trace(go.Scatter(x=[i,i],y=[df['mAU'].min(),df['mAU'].max()/15],
                                         mode='lines',
                                         legendgroup='Fractions',name='fractions',showlegend=False,
                                         opacity=0.5,line=dict(color='black')))

                fig.add_trace(go.Scatter(x=[i], y=[df['mAU'].max()/15],mode='text',text=k,
                                        textposition="top center",showlegend=False))
                                                                    # adds numbers to fraction lines.
                                                                    # Needs to be done like this because
                                                                    # of the x=[i,i] adds to points
                                                                    # so numbering will be dublicated


        else:
            pass

 #   fig.add_trace(go.Scatter(x=df['ml'], y=df['mAU'],name='test')),
 #  fig.add_trace(go.Scatter(x=df['ml'], y=df['mAU'], name='test'))
    return fig


layout = html.Div(id='parent', children=[
            dcc.Graph(id='line_plot',
                      figure=plot_data()),




])

