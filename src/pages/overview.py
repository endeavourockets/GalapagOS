from app import app, html, dcc, dash
from db import Data, Sensor
import plotly.graph_objs as go
import dash_table
import pandas as pd
from util import angle_between
from pages.components.orientation import Orientation
from pages.components.card import Card
from pages.components.row import Row

orientation = Orientation()
card = Card()
row = Row()

overview = html.Div([
    html.H2('Overview'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    ),
    row.create(children=[
        card.create(
            title='Orientation',
            children=[orientation.create(id='orientation')],
            footer_id='orientation_text',
            col_sizes={'md': 6, 'xl': 4}
        ),
        card.create(
            title='Altitude',
            children=[
                dcc.Graph(
                    id='altitude-graph',
                    figure=go.Figure(data=[go.Scatter(x=[0], y=[0])])
                )
            ],
            footer_id='altitude_text',
            col_sizes={'md': 12, 'xl': 8}
        ),
    ])
])


@app.callback(dash.dependencies.Output('orientation', 'style'),
              [dash.dependencies.Input('interval-component', 'n_intervals')])
def update_xz_rocket(n_intervals):
    data_query = Data.query
    try:
        df = pd.read_sql(data_query.statement, data_query.session.bind)
        x = float(df[df['title'] == 'X'].iloc[-1]['data_v'])
        y = float(df[df['title'] == 'Y'].iloc[-1]['data_v'])
        z = float(df[df['title'] == 'Z'].iloc[-1]['data_v'])
        angle_x = angle_between((1, 0), (z, x))
        angle_y = angle_between((1, 0), (z, y))
        if angle_x > angle_y:
            angle = angle_x
        else:
            angle = angle_y
        return orientation.get_style(angle)
    except:
        return orientation.get_style(0)


@app.callback(dash.dependencies.Output('orientation_text', 'children'),
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
