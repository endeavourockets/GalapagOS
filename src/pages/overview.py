from app import app, html, dcc, dash

overview = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i}
                 for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])


@app.callback(
    dash.dependencies.Output('display-value', 'children'),
    [dash.dependencies.Input('dropdown', 'value')]
)
def display_value(value):
    return 'You have selected "{}"'.format(value)
