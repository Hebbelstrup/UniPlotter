import base64
import io
import dash
from dash import html, dcc, callback, Input, Output, dash_table,State
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


dash.register_page(__name__, title='fluorescence')

layout = html.Div(id='parent', children=[
            html.H1(id='H1', children='Fluorescence Plotter', style={'textAlign': 'center', 'marginTop': 40, 'marginBottom': 40}),
            html.Div(children=
                ['A plotter for Fluorescence data from ...',html.Br(), 'Uploading more than one file will only overlay 280 nm']
                              ,style={'textAlign':'center','marginBottom':20}),
            dcc.Upload(id='upload-data', children=html.Div([html.A("Select File(s)")]),
                       style={
                           "width": "305px",
                           # "height": "60px",
                           # "lineHeight": "60px",
                           "borderWidth": "1px",
                           "borderStyle": "solid",
                           "borderRadius": "5px",
                           "textAlign": "center",
                           # "margin": "5px",
                       },
                       multiple=True,
                       className="d-grid gap-2 col-6 mx-auto"),
                       dcc.Graph(id='Fluorescence_plot'),
                       html.P(id='Fluorescence_placeholder'),

])


def parse_content(contents): # Takes in one element from "upload-Data","contents" and returns a dataframe for that file


    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    file = io.StringIO(decoded.decode('utf-8'))

    df = pd.read_csv(file, sep="\n|\\t", decimal='.', names=["nM","I"], engine='python', header=None)
    df = pd.DataFrame(df)
    data_start = float(df.loc[df['nM'].str.startswith('#DATA')].index[0] + 1)
    data = df[int(data_start):]
    data['nM'] = data['nM'].astype(float)

    return data

@callback(Output('Fluorescence_plot','figure'),
          [Input('upload-data','contents')],config_prevent_initial_callbacks=True)

def show(content):
    data = [parse_content(i) for i in content]
    fig = make_subplots(rows=2, cols=1, row_heights=[0.8,0.2])

    fig.add_trace(go.Scatter(x=data[0]['nM'],y=data[0]['I']),row=1,col=1)

    return fig