from pages.components.component import Component
from app import html

class Card(Component):

    def __init__(self):
        pass

    def create(self, **args):
        title = args['title']
        col_sizes = ' '.join([f'col-{key}-{val}' for key, val in args['col_sizes'].items()])
        header = html.Div([
            html.H3(title, className='card-title')
            ], 
            className='card-header')
        children = [header] + args['children']
        if 'footer_id' in args:
            children.append(html.Div('', id=args['footer_id'], className='card-footer'))
        return html.Div([
                    html.Div(children, className='card'),
                ],
                className=col_sizes)



