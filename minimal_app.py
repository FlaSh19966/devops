import datetime

from flask import Flask, make_response, jsonify
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)
db = mongo.db


class Default(Resource):
    def get(self):
        print('Default endpoint')
        endpoint_name = 'default'
        try:
            db.test.insert_one({'name': endpoint_name, 'datetime': datetime.datetime.now()})
            data = list(db.test.find({}, {'_id': 0}))
            return make_response(jsonify({'MSG': 'This is default endpoint',
                                          'data': data}), 200)
        except Exception as e:
            return make_response(jsonify({'MSG': 'This is default endpoint exception',
                                          'error': str(e)}), 500)


class FlaskHealthCheck(Resource):
    def get(self):
        print('flask-health-check hit')
        endpoint_name = 'flask'
        try:
            db.test.insert_one({'endpoint_name': endpoint_name, 'datetime': datetime.datetime.now()})
            data = list(db.test.find({}, {'_id': 0}))
            return make_response(jsonify({'MSG': 'flask-health-check hit',
                                          'data': data}), 200)
        except Exception as e:
            return make_response(jsonify({'MSG': 'flask-health-check hit exception',
                                          'error': str(e)}), 500)

class NginxHealthCheck(Resource):
    def get(self):
        print('nginx-health-check hit')
        endpoint_name = 'nginx'
        try:
            db.test.insert_one({'endpoint_name': endpoint_name, 'datetime': datetime.datetime.now()})
            data = list(db.test.find({}, {'_id': 0}))
            return make_response(jsonify({'MSG': 'nginx-health-check hit',
                                          'data': data}), 200)
        except Exception as e:
            return make_response(jsonify({'MSG': 'nginx-health-check hit exception',
                                          'error': str(e)}), 500)


api.add_resource(Default, '/')
api.add_resource(FlaskHealthCheck, '/health-check')
api.add_resource(NginxHealthCheck, '/v1/health-check')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
