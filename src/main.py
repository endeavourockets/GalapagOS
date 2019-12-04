from app import app, dash
from pages.empty import empty
# pages
from pages.overview import display_value, overview
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
    app.run_server(debug=True)
