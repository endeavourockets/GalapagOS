import dash as dash
import dash_core_components as dcc
import dash_html_components as html
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML as inner_html

app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

app.title = 'GalapagOS'


def load_html(name):
    with open(f'./src/assets/html/{name}.html', 'r') as file:
        return file.read().replace('\n', '')


template = load_html('dashboard')

app.index_string = template
