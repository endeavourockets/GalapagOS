from app import app, html, dcc

empty = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])