import dash
import dash_core_components
import dash_html_components
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML
import dash_defer_js_import
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# to be imported from other modules
dji = dash_defer_js_import
inner_html = DangerouslySetInnerHTML
dcc = dash_core_components
html = dash_html_components

app = dash.Dash(__name__, assets_ignore='.*dashlocal.*')
app.config.suppress_callback_exceptions = True

app.server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app.server)

app.title = 'GalapagOS'

class Sensor(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    datas = db.relationship('Data', backref='Sensor', lazy=True)

class Data(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    data_v = db.Column(db.String(32), nullable=False)
    Sensor_id = db.Column(db.Integer, db.ForeignKey(Sensor.id), nullable=False)

def load_html(name):
    with open(f'./assets/html/{name}.html', 'r') as file:
        return file.read().replace('\n', '')

def add_sensor_reading(entry):
    all_Sensors = Sensor.query.order_by(Sensor.id)
    for i in range(len(entry)):
        if all_Sensors.filter(Sensor.title == entry[i]['Sensor']).first() :
            keys = list(entry[i])
            print(keys)
            for j in range(1,len(keys)):
                Sensor_id = all_Sensors.filter(Sensor.title == entry[i]['Sensor']).all()[0].id
                print(keys[j])
                data_v = str(entry[i][keys[j]])
                new_data_v = Data(title = keys[j],data_v = data_v ,Sensor_id = Sensor_id)
                db.session.add(new_data_v)
                db.session.commit()
        else :
            new_Sensor = Sensor(title = entry[i]['Sensor'])
            db.session.add(new_Sensor)
            db.session.commit()
            all_Sensors = Sensor.query.order_by(Sensor.id)
            keys = list(entry[i])
            for j in range(1,len(keys)):
                Sensor_id = all_Sensors.filter(Sensor.title == entry[i]['Sensor']).first().id
                print(keys[j])
                data_v = str(entry[i][keys[j]])
                new_data_v = Data(title = keys[j], data_v = data_v ,Sensor_id = Sensor_id)
                db.session.add(new_data_v)
                db.session.commit()

template = load_html('dashboard')

app.index_string = template
