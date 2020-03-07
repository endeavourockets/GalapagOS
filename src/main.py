from app import app, dash, db, Sensor, Data, add_sensor_reading
from pages.empty import empty
# pages
from pages.overview import overview
from pages.map import map

server = app.server
app.layout = empty

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname in ['/', '/overview']:
        return overview
    if pathname == '/map':
        return map
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    db.create_all()
    test_array = [
        {'Sensor': 'Temperature', 'Temperature': 30.7},
        {'Sensor': 'GPS', 'Altitude': 57, 'Longitude': 23, 'Latitude': 23}
    ]
    add_sensor_reading(test_array)
    app.run_server(debug=True, host='0.0.0.0')
