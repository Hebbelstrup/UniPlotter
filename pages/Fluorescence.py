import base64
import io
import dash
from dash import html, dcc, callback, Input, Output, dash_table,State
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import numpy as np



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
                           "marginBottom": "5px",
                       },
                       multiple=True,
                       className="d-grid gap-2 col-6 mx-auto"),


                       html.Button('concentration',id='fluoro_concentrations',n_clicks=0,
                                   style={
                                       'display' : 'none'
                                   }),



                       dbc.Tabs([]
                           ,id="fluoro_tabs",
                           active_tab='normal',
                           style={'display':'none'},
                       ),

                       dcc.Graph(id='Fluorescence_plot'),
                       html.P(id='Fluorescence_placeholder'),
                       dbc.Modal(
                           [
                               dbc.ModalHeader(dbc.ModalTitle("Header")),
                               dbc.ModalBody(children="This is the content of the modal",id='modalbody'),
                               dbc.ModalFooter(
                                   dbc.Button(
                                       "Close", id="close", className="ms-auto", n_clicks=0
                                   )
                               ),
                           ],
                           id="modal",
                           is_open=False,
                       ),

])

@callback(Output('modalbody','children'),Input('upload-data', 'contents'),config_prevent_initial_callbacks=True)
def update_modal_with_files(content):
   # data = [parse_content(i) for i in content]

    return 'testing'

@callback(Output('modal','is_open'),Output('close','n_clicks'),
          [Input('fluoro_concentrations','n_clicks'),Input('close','n_clicks')])

def open_modal(n_click,close_click):

    if n_click >= 1 and close_click == 0:
        return True,0
    else:
        return False,0


@callback(Output('fluoro_concentrations','style'), # Input is whenever files are uploaded. Output is style and className for the button
          Output('fluoro_concentrations','className'),
            Input('upload-data', 'contents'),config_prevent_initial_callbacks=True)

def update_button(data): # Returns style and position for button if more than 1 file is uploaded. Button is used for concentration input.
        if len(data) > 1:
            style = {'width': '154px', 'height': '30px', 'marginTop': 5}
            position = "d-grid gap-2 col-6 mx-auto"
            return style,position

        else:
            return {'display':'none'},None

@callback(Output('fluoro_tabs','children'),
          Output('fluoro_tabs','style'),
          Output('fluoro_tabs','className'),
            Input('upload-data', 'contents'),config_prevent_initial_callbacks=True)

def update_tab(event):
    return [
                               dbc.Tab(label='Normal',tab_id='normal'),
                               dbc.Tab(label='Wavelength',tab_id='wavelength'),
                               dbc.Tab(label='Intensity',tab_id='intensity')
           ], None ,'mx-auto'

@callback(Output('Fluorescence_plot','figure'),
          [Input('upload-data', 'contents'),
           Input('fluoro_tabs','active_tab'),
           State('upload-data', 'filename')], config_prevent_initial_callbacks=True)

def plot_fluorescence(content,active_tab,filename):


    data = [parse_content(i) for i in content]

    fig = make_subplots(rows=1, cols=1)

    if active_tab == 'normal':
        for i in range(0,len(data)):
            fig.add_trace(go.Scatter(x=data[i]['nM'],y=data[i]['I'],name=filename[i]),row=1,col=1)




    ### WAVELENGTH PLOTTER. CURRENTLY TAKES THE NM WITH MAX INT FOR FILE 0 AND PLOTS FOR ALL
    ### STILL NEEDS ABILITY TO DECIDE WAVELENGTH & SHOULD TAKE IN LIST OF DENATURANT VALUES

    if active_tab == 'wavelength':
        I_max = data[0]['I'].max()
        nm = data[0].loc[data[0]['I'] == float(I_max)]['nM']
        x = np.arange(0,len(data),1)
        y = []

        for i in range(0,len(data)):
            I_at_nM = float(data[i].loc[data[i]['nM'] == float(nm)]['I'])
            y.append(I_at_nM)

        fig.add_trace(go.Scatter(x=x,y=y,name='testing',mode='markers'),row=1,col=1)

        #fig['layout']['xaxis']['title'] = y
    return fig
