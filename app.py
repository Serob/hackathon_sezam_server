#!flask/bin/python

from flask import request
from flask_restful import Resource
import prediction
from init_api import api, app

model = prediction.train()


@api.route('/prediction/<string:message>')
class User(Resource):
    def get(self, message):
        return {'predicted word': str(prediction.predict(message, model))}

    def post(self, username):
        return {'post username': username}


if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.1', port=5000)
