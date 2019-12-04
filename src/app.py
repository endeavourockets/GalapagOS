import dash
import dash_core_components
import dash_html_components
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML
import dash_defer_js_import

# to be imported from other modules
dji = dash_defer_js_import
inner_html = DangerouslySetInnerHTML
dcc = dash_core_components
html = dash_html_components

app = dash.Dash(__name__, assets_ignore='.*dashlocal.*')
app.config.suppress_callback_exceptions = True

app.title = 'GalapagOS'


def load_html(name):
    with open(f'./assets/html/{name}.html', 'r') as file:
        return file.read().replace('\n', '')


template = load_html('dashboard')

app.index_string = template
