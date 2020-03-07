from pages.components.component import Component
from app import html


class Orientation(Component):

    def __init__(self):
        self.rocket_style = {
            'transform': 'translateX(-51.2%)',
            'left': '50%',
            'position': 'absolute',
            'transition': 'all 1s',
            'opacity': '0.8',
        }
        self.circle_style = self.rocket_style.copy()
        self.circle_style['transform'] = 'translateX(-50%)'
        self.circle_img = 'assets/images/rocket/circle.svg'
        self.rocket_img = 'assets/images/rocket/rocket_black.svg'
        self.height = 300

    def create(self, **args):
        id = args['id']
        return html.Div([
            html.Img(src=self.circle_img,
                     height=f'{self.height}', style=self.rocket_style),
            html.Img(src=self.rocket_img,
                     height=f'{self.height}', style=self.circle_style, id=id),
            html.Div('', style={'height': f'{self.height}px'}),
        ], className='card-body')

    def get_style(self, angle):
        new_style = self.rocket_style.copy()
        new_style['transform'] += f' rotate({angle}deg)'
        return new_style
