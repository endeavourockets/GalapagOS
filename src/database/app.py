from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship
from base import Session


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Motor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    data_v = db.Column(db.String(32), nullable=False)
    motor_id = db.Column(db.Integer, db.ForeignKey('Motor.id'))
    motor = db.relationship("Motor")


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Motor.query.order_by(Motor.id)
        return render_template('index.html', tasks=tasks)


def sort_em(intry_vals):
    all_motors = Session.query(Motor).all()
    for i in range(len(intry_vals)):
        if all_motors.filter(Motor.title == intry_vals[i]['Motor']).all().count() > 0:
            keys = intry_vals[i].keys()
            for j in range(1, len(keys)):
                motor_id = all_motors.filter(
                    Motor.title == intry_vals[i]['Motor']).all()[0].id

                new_data_v = Data(title=keys[j], data_v=str(
                    intry_vals[i][keys[j]]), motor_id=motor_id)
                var_sd = 'Hello World'

                try:
                    db.session.add(new_data_v)
                    db.session.commit()
                except:
                    print('Damn it didnt work')
        else:
            new_motor = Motor(title=intry_vals[i]['Motor'])
            try:
                db.session.add(new_motor)
                db.session.commit()
            except:
                print('Damn it didnt work')
            all_motors = Motor.query.order_by(Motor.id)

            keys = intry_vals[i].keys()
            for j in range(1, len(keys)):
                motor_id = all_motors.filter(
                    Motor.title == intry_vals[i]['Motor']).all()[0].id
                new_data_v = Data(title=keys[j], data_v=str(
                    intry_vals[i][keys[j]]), motor_id=motor_id)
                var_sd = 'Hello World'
                try:
                    db.session.add(new_data_v)
                    db.session.commit()
                except:
                    print('Damn it didnt work')


test_array = [{'Motor': 'Tempreture sensor', 'Tempreture': 30.7}, {
    'Motor': 'GPS', 'Altitude': 57, 'Longitude': 23}]
sort_em(test_array)


if __name__ == "__main__":
    app.run(debug=True)
