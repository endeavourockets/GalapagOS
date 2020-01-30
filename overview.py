from app import app, html, dcc, dash

# sensor data for table
global sensors
global values
sensors = ["S1", "S2", "S3", "S4", "S5"]
values = [1, 2, 3, 4, 5]

overview = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i}
                 for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value'),

    html.Table(

        # Sensor names
        [html.Tr([html.Th("Sensor",), html.Th("Value")])] +

        # Sensor Values
        [html.Tr([html.Td(sensors[i]), html.Td(values[i])])
         for i in range(max(len(sensors), len(values)))]
    )
])


@app.callback(
    dash.dependencies.Output('display-value', 'children'),
    [dash.dependencies.Input('dropdown', 'value')]
)
def display_value(value):
    return 'You have selected "{}"'.format(value)
