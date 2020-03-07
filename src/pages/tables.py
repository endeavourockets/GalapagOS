from app import app, html, dcc, dash, Data, Sensor
import dash_table
import pandas as pd
import plotly.express as px


#f = px.data.iris()
#ig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

# If you print fig, you'll see that it's just a regular figure with data and layout
# print(fig)

fig.show()

overview = html.Div([
    html.H2('Sensors'),
    html.Div(id='display-value'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    )
])


def getSensorTable():
    sensor_query = Sensor.query
    print(sensor_query)
    df = pd.read_sql(sensor_query.statement, sensor_query.session.bind)

    return dash_table.DataTable(
        id='sensor-table',
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        style_cell={'textAlign': 'center', 'min-width': '50px'},
    )

@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('interval-component', 'n_intervals')])
def display_value(value):
    return getSensorTable()