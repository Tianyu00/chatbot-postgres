from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template
from flask_socketio import SocketIO
import os
import re
from collections import Counter
from string import punctuation
from math import sqrt
# import json
from sqlalchemy import create_engine

db_string = os.environ['DATABASE_URL']

db = create_engine(db_string)

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)























#
# migrate = Migrate(app, db)
#
# class CarsModel(db.Model):
#     __tablename__ = 'cars'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     model = db.Column(db.String())
#     doors = db.Column(db.Integer())
#
#     def __init__(self, name, model, doors):
#         self.name = name
#         self.model = model
#         self.doors = doors
#
#     def __repr__(self):
#         return f"<Car {self.name}>"
#
#
# @app.route('/')
# def hello():
#     return {"hello": "world"}
#
#
# # Imports and CarsModel truncated
#
# @app.route('/cars', methods=['POST', 'GET'])
# def handle_cars():
#     if request.method == 'POST':
#         if request.is_json:
#             data = request.get_json()
#             new_car = CarsModel(name=data['name'], model=data['model'], doors=data['doors'])
#             db.session.add(new_car)
#             db.session.commit()
#             return {"message": f"car {new_car.name} has been created successfully."}
#         else:
#             return {"error": "The request payload is not in JSON format"}
#
#     elif request.method == 'GET':
#         cars = CarsModel.query.all()
#         results = [
#             {
#                 "name": car.name,
#                 "model": car.model,
#                 "doors": car.doors
#             } for car in cars]
#
#         return {"count": len(results), "cars": results}
#
#
#
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
