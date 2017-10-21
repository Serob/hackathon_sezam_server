#!flask/bin/python

from flask import request
from flask_restful import Resource
import prediction
from init_api import api, app
import flask_oauthlib

model_sbow = prediction.train(0)
model_sg = prediction.train(1)


@api.route('/prediction')
class User(Resource):
    def get(self):
        args = request.args
        method = 'sbow'
        if list(args.keys()).count('method') == 1:
            method = args['method']
        message = args['message']
        #print(args['method'])
        if method == 'sg':
            return {'predicted word': str(prediction.predict(message, model_sg))}
        else:
            return {'predicted word': str(prediction.predict(message, model_sbow))}

    def post(self, username):
        return {'post username': username}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
