

from flask import Flask, make_response, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class FlaskHealthCheck(Resource):
    def get(self):
        print('flask-health-check hit')
        return make_response(jsonify({'MSG': 'This is Flask health check'}), 200)


class NginxHealthCheck(Resource):
    def get(self):
        print('nginx-health-check hit')
        return make_response(jsonify({'MSG': 'This is nginx health check'}), 200)


api.add_resource(FlaskHealthCheck, '/health-check')
api.add_resource(NginxHealthCheck, '/v1/health-check')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
