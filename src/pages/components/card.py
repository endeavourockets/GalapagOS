from pages.components.component import Component
from app import html


class Card(Component):

    def __init__(self):
        pass

    def create(self, **args):
        title = args['title']
        col_sizes = ' '.join(
            [f'col-{key}-{val}' for key, val in args['col_sizes'].items()])
        header_children = [html.H3(title, className='card-title')]
        if 'card_options' in args:
            header_children.append(
                html.Div(args['card_options'], className='card-options'))
        header = html.Div(header_children, className='card-header')
        children = [header] + args['children']
        if 'footer_id' in args:
            children.append(
                html.Div('', id=args['footer_id'], className='card-footer'))
        return html.Div([
            html.Div(children, className='card'),
        ],
            className=col_sizes)
