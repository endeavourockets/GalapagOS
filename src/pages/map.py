from app import app, html, dcc, inner_html, load_html

map = html.Div([
    inner_html(load_html('worldwind'))
])