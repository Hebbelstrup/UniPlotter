import base64
import io
import dash
from dash import html, dcc, callback, Input, Output, dash_table,State
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


dash.register_page(__name__, title='akta')



def get_xy(name,df):
    x_loc = df.columns.get_loc(name) -1
    x = df.iloc[:,x_loc]
    y = df[name]
    name = name
    return x,y,name

def parse_content(contents):
    for data in contents:

        content_type, content_string = data.split(',')

        decoded = base64.b64decode(content_string)
        file = io.StringIO(decoded.decode('utf-8'))

        df = pd.read_csv(file, sep="\n|\\t", decimal=".", header=2, engine='python')
        df = pd.DataFrame(df)

    return df

layout = html.Div(id='parent', children=[
            html.Div(children=
                ['A plotter for data from Äkta systems',html.Br(), 'Uploading more than one file will only overlay 280 nm']
                              ,style={'textAlign':'center'}),
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
            dcc.Graph(id='akta_plot'),
            html.H1(id='output-data-upload'),
            html.P(id='placeholder'),



])






@callback(Output('akta_plot','figure'),
          Output('output-data-upload','children'),
          [Input('upload-data','contents')],config_prevent_initial_callbacks=True)


def plot_data(contents):


    df = parse_content(contents)
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    if len(contents) == 1:

        for i in df.columns[1::2]:
            x,y,name = get_xy(i,df)
            if name =='mAU':
                fig.add_trace(go.Scatter(x=x,y=y,name=name),secondary_y=False)
            if name not in ['Fraction','Logbook','Injection','mAU']:
                fig.add_trace(go.Scatter(x=x, y=y, name=name,visible='legendonly'), secondary_y=True)
            if name == 'Fraction':
                fig.add_trace(go.Scatter(x=[0, 0], y=[0, 0], mode='lines',
                                         legendgroup='Fractions', name='fractions',visible='legendonly'))
                for k,i in enumerate(x.dropna()):
                    fig.add_trace(go.Scatter(x=[i,i],y=[df['mAU'].min(),df['mAU'].max()/15],
                                             mode='lines',
                                             legendgroup='Fractions',name='fractions',showlegend=False,
                                             opacity=0.5,line=dict(color='black'),visible='legendonly'))
                    fig.add_trace(go.Scatter(x=[i], y=[df['mAU'].max()/15],mode='text',text=k+1,
                                            textposition="top center",showlegend=False,legendgroup='Fractions',visible='legendonly'))
                                                                    # adds numbers to fraction lines.
                                                                    # Needs to be done like this because
                                                                    # of the x=[i,i] adds to points
                                                                    # so numbering will be dublicates
        fig['layout']['xaxis']['title'] = 'ml'
        fig['layout']['yaxis1']['title'] = '280 nm'
        return fig, None

    else:
        for data in contents:
            df = parse_content(data)
            fig.add_trace(go.Scatter(x=df['ml'],y=df['mAU'],name='test'))
        return fig,None


