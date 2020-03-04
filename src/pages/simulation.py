from app import app, html, dcc, dash, Data, Sensor, add_sensor_reading, set_simulation_status, get_simulation_status
import dash_table
import pandas as pd
import numpy as np
import time
import yaml

simulation = html.Div([
    html.Div([
        html.Div([
            html.H3('Simulation', className='card-title'),
            html.Div([
                html.Button('Start', id='start-button',
                            className='btn btn-primary btn-sm', style={'margin-right': '5px'}),
                html.Div(),
                html.Button('Stop', id='cancel-button',
                            className='btn btn-danger btn-sm')
            ], className='card-options')
        ], className='card-header'),
        html.Div([
            dcc.Dropdown(
                id='sim-dropdown',
                options=[
                    {'label': 'random sensor data', 'value': 'random_sensor_data'},
                    {'label': 'gps data', 'value': 'gps'},
                    {'label': 'orientation data', 'value': 'orientation'},
                ],
                value='random_sensor_data'
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
    if n_clicks != None:
        sim_data = yaml.load(open(f'simulations/{value}.yaml','r'))
        set_simulation_status(value, True)
        last_val = {}
        while get_simulation_status(value).running:
            data_list = []
            for sensor in sim_data['sensors']:
                sensor_dict = {}
                name = list(sensor.keys())[0]
                sensor_dict['Sensor'] = name
                values = sensor[name]
                for val_k in values:
                    key = list(val_k.keys())[0]
                    val = val_k[key]
                    loc = val['loc']
                    rand_num = np.random.normal(loc, val['scale'])
                    if 'update loc' in val and val['update loc']:
                        namekey = f'{name}.{key}'
                        if namekey in last_val:
                            loc = last_val[namekey]
                        rand_num = np.random.normal(loc, val['scale'])
                        last_val[namekey] = rand_num
                    sensor_dict[key] = rand_num
                data_list.append(sensor_dict)
            add_sensor_reading(data_list)
            time.sleep(sim_data['timeout'])
        return ""
    return ""


@app.callback(
    dash.dependencies.Output('cancel-output', 'children'),
    [dash.dependencies.Input('cancel-button', 'n_clicks')],
    [dash.dependencies.State('sim-dropdown', 'value')])
def cancel_simulation(n_clicks, value):
    try:
        if n_clicks != None:
            set_simulation_status(value, False)
            return "Simulation stopped."
    except:
        pass
    return ""