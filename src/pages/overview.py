from app import app, html, dcc, dash, Data, Sensor
import plotly.graph_objs as go
import dash_table
import pandas as pd
import numpy as np

svg_style = {
    'transform': 'translateX(-51.2%)',
    'left': '50%',
    'position': 'absolute',
    'transition': 'all 1s',
    'opacity': '0.8',
}

svg_style_circle = svg_style.copy()
svg_style_circle['transform'] = 'translateX(-50%)'

overview = html.Div([
    html.H2('Overview'),
    dcc.Interval(
        id='interval-component',
        interval=1*500,  # in milliseconds
        n_intervals=0
    ),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Orientation XZ', className='card-title'),
                ],
                    className='card-header'),
                html.Div([
                    html.Img(src='assets/images/rocket/circle.svg',
                             height='300', style=svg_style),
                    html.Img(src='assets/images/rocket/rocket_black.svg',
                             height='300', style=svg_style_circle, id='rocket_xz'),
                    html.Div('', style={'height': '300px'}),
                ],
                    className='card-body'),
                html.Div('', id='text_xz', className='card-footer')
            ],
                className='card'),
        ],
            className='col-md-6 col-xl-4'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Orientation YZ', className='card-title'),
                ],
                    className='card-header'),
                html.Div([
                    html.Img(src='assets/images/rocket/circle.svg',
                             height='300', style=svg_style),
                    html.Img(src='assets/images/rocket/rocket_black.svg',
                             height='300', style=svg_style_circle, id='rocket_yz'),
                    html.Div('', style={'height': '300px'}),
                ],
                    className='card-body'),
                html.Div('', id='text_yz', className='card-footer')
            ],
                className='card'),
        ],
            className='col-md-6 col-xl-4'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Altitude', className='card-title'),
                ],
                    className='card-header'),
                html.Div([
                    dcc.Graph(id='altitude-graph',
                              figure=go.Figure(data=[go.Scatter(x=[0], y=[0])]))
                ],
                    className='card-body'),
                html.Div('', id='text_altitude', className='card-footer')
            ],
                className='card'),
        ],
            className='col-md-12 col-xl-4'),
    ],
        className='row')
])


def unit_vector(vector):
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.degrees(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))

@app.callback(dash.dependencies.Output('rocket_xz', 'style'),
              [dash.dependencies.Input('interval-component', 'n_intervals')])
def update_xz_rocket(n_intervals):
    data_query = Data.query
    try:
        df = pd.read_sql(data_query.statement, data_query.session.bind)
        x = float(df[df['title'] == 'X'].iloc[-1]['data_v'])
        z = float(df[df['title'] == 'Z'].iloc[-1]['data_v'])
        new_style = svg_style.copy()
        angle = angle_between((1, 0), (z, x))
        if x < 0:
            angle *= -1
        new_style['transform'] += f' rotate({angle}deg)'
        return new_style
    except:
        return svg_style

@app.callback(dash.dependencies.Output('rocket_yz', 'style'),
              [dash.dependencies.Input('interval-component', 'n_intervals')])
def update_yz_rocket(n_intervals):
    data_query = Data.query
    try:
        df = pd.read_sql(data_query.statement, data_query.session.bind)
        y = float(df[df['title'] == 'Y'].iloc[-1]['data_v'])
        z = float(df[df['title'] == 'Z'].iloc[-1]['data_v'])
        new_style = svg_style.copy()
        angle = angle_between((1, 0), (z, y))
        if y < 0:
            angle *= -1
        new_style['transform'] += f' rotate({angle}deg)'
        return new_style
    except:
        return svg_style

@app.callback(dash.dependencies.Output('text_xz', 'children'),
              [dash.dependencies.Input('interval-component', 'n_intervals')])
def update_xz_rocket_text(n_intervals):
    data_query = Data.query
    try:
        df = pd.read_sql(data_query.statement, data_query.session.bind)
        x = float(df[df['title'] == 'X'].iloc[-1]['data_v'])
        y = float(df[df['title'] == 'Y'].iloc[-1]['data_v'])
        z = float(df[df['title'] == 'Z'].iloc[-1]['data_v'])
        return f'X: {x:2f} Y: {y:2f} Z: {z:2f}'
    except:
        return 'no data'

@app.callback(dash.dependencies.Output('text_yz', 'children'),
              [dash.dependencies.Input('interval-component', 'n_intervals')])
def update_yz_rocket_text(n_intervals):
    data_query = Data.query
    try:
        df = pd.read_sql(data_query.statement, data_query.session.bind)
        x = float(df[df['title'] == 'X'].iloc[-1]['data_v'])
        y = float(df[df['title'] == 'Y'].iloc[-1]['data_v'])
        z = float(df[df['title'] == 'Z'].iloc[-1]['data_v'])
        return f'X: {x:2f} Y: {y:2f} Z: {z:2f}'
    except:
        return 'no data'


@app.callback(dash.dependencies.Output('altitude-graph', 'figure'),
              [dash.dependencies.Input('interval-component', 'n_intervals')])
def update_alt(n_intervals):
    data_query = Data.query
    try:
        df = pd.read_sql(data_query.statement, data_query.session.bind)
        data_alt = df[df['title'] == 'Altitude']['data_v']
        return go.Figure(data=[go.Scatter(x=list(range(len(data_alt))), y=data_alt)])
    except:
        return go.Figure(data=[go.Scatter(x=[0], y=[0])])
