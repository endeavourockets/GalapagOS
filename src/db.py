from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app.server)

class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    datas = db.relationship('Data', backref='Sensor', lazy=True)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    data_v = db.Column(db.String(32), nullable=False)
    Sensor_id = db.Column(db.Integer, db.ForeignKey(Sensor.id), nullable=False)


class Simulation(db.Model):
    title = db.Column(db.String(32), primary_key=True)
    running = db.Column(db.Boolean, nullable=False)

def set_simulation_status(value, running=True):
    sim = get_simulation_status(value)
    if sim is not None:
        db.session.delete(sim)
    db.session.add(Simulation(title=value, running=running))
    db.session.commit()


def get_simulation_status(value):
    return Simulation.query.get(value)


def add_sensor_reading(entry):
    all_Sensors = Sensor.query.order_by(Sensor.id)
    for i in range(len(entry)):
        if all_Sensors.filter(Sensor.title == entry[i]['Sensor']).first():
            keys = list(entry[i])
            for j in range(1, len(keys)):
                Sensor_id = all_Sensors.filter(
                    Sensor.title == entry[i]['Sensor']).all()[0].id
                data_v = str(entry[i][keys[j]])
                new_data_v = Data(
                    title=keys[j], data_v=data_v, Sensor_id=Sensor_id)
                db.session.add(new_data_v)
                db.session.commit()
        else:
            new_Sensor = Sensor(title=entry[i]['Sensor'])
            db.session.add(new_Sensor)
            db.session.commit()
            all_Sensors = Sensor.query.order_by(Sensor.id)
            keys = list(entry[i])
            for j in range(1, len(keys)):
                Sensor_id = all_Sensors.filter(
                    Sensor.title == entry[i]['Sensor']).first().id
                data_v = str(entry[i][keys[j]])
                new_data_v = Data(
                    title=keys[j], data_v=data_v, Sensor_id=Sensor_id)
                db.session.add(new_data_v)
                db.session.commit()