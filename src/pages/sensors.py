from app import app, html, dcc, dash
from db import Data, Sensor
import dash_table
import pandas as pd

sensors = html.Div([
    html.H2('Sensors'),
    html.Div(id='display-sensor'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    ),
    html.H2('Sensor Values'),
    html.Div(id='display-value')
])


def getSensorTable():
    sensor_query = Sensor.query
    df = pd.read_sql(sensor_query.statement, sensor_query.session.bind)

    return dash_table.DataTable(
        id='sensor-table',
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        style_cell={'textAlign': 'center', 'min-width': '50px'},
    )


def getValueTable():
    data_query = Data.query
    df = pd.read_sql(data_query.statement, data_query.session.bind)
    df = df.sort_values(by='id', ascending=False)

    return dash_table.DataTable(
        id='sensor-table',
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        style_cell={'textAlign': 'center', 'min-width': '50px'},
    )


@app.callback(dash.dependencies.Output('display-sensor', 'children'),
              [dash.dependencies.Input('interval-component', 'n_intervals')])
def display_value(value):
    return getSensorTable()


@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('interval-component', 'n_intervals')])
def display_value(value):
    return getValueTable()
