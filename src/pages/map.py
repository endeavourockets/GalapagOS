from app import html, inner_html, load_html, dji

map = html.Div([
    inner_html(load_html('worldwind')),
    dji.Import(src="./assets/js/dashlocal-map.js"),
])
