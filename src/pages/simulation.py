from app import app, html, dcc, dash, Data, Sensor, add_sensor_reading, set_simulation_status, get_simulation_status
import dash_table
import pandas as pd
import numpy as np
import time

simulation = html.Div([
    html.Div([
        html.Div([
            html.H3('Simulation', className='card-title'),
            html.Div([
                html.Button('Start', id='start-button',
                            className='btn btn-primary btn-sm'),
                html.Button('Cancel', id='cancel-button',
                            className='btn btn-danger btn-sm')
            ], className='card-options')
        ], className='card-header'),
        html.Div([
            dcc.Dropdown(
                id='sim-dropdown',
                options=[
                    {'label': 'random sensor data', 'value': 'rsd'},
                    {'label': 'gps data', 'value': 'gps'},
                ],
                value='rsd'
            ),
            html.Div(id='simulation-output'),
            html.Div(id='cancel-output')
        ], className='card-body'),
    ], className='card col-lg-6'),
])



@app.callback(
    dash.dependencies.Output('simulation-output', 'children'),
    [dash.dependencies.Input('start-button', 'n_clicks')],
    [dash.dependencies.State('sim-dropdown', 'value')])
def start_simulation(n_clicks, value):
    if value == 'rsd' and n_clicks != None:
        set_simulation_status(value, True)
        while get_simulation_status(value).running:
            test_array = [
                {'Sensor': 'Temperature',
                    'Temperature': np.random.normal(15, 15)},
                {'Sensor': 'GPS', 'Altitude': np.random.normal(1000, 200), 'Longitude': np.random.normal(
                    23, 50), 'Latitude': np.random.normal(57, 50)}
            ]
            add_sensor_reading(test_array)
            time.sleep(5)
        return "simulation stopped"
    return ""


@app.callback(
    dash.dependencies.Output('cancel-output', 'children'),
    [dash.dependencies.Input('cancel-button', 'n_clicks')],
    [dash.dependencies.State('sim-dropdown', 'value')])
def cancel_simulation(n_clicks, value):
    if n_clicks != None:
        set_simulation_status(value, False)
    return ""