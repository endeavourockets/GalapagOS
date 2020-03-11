from pages.components.component import Component
from app import html

class Row(Component):

    def __init__(self):
        pass

    def create(self, **args):
        return html.Div(args['children'], className="row")
