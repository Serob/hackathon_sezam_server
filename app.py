#!flask/bin/python

from flask import request, Response
from flask_restful import Resource
import prediction
from init_api import api, app

model_sbow = prediction.train(0)
model_sg = prediction.train(1)


@api.route('/prediction')
class User(Resource):
    def get(self):
        args = request.args
        method = 'sbow'  # by default
        if list(args.keys()).count('method') == 1:
            method = args['method']
        message = args['message']

        if method == 'sg':
            data = str({'predicted word': str(prediction.predict(message, model_sg))})
            r = Response(response=data)
            return r
        else:
            data = str({'predicted word': str(prediction.predict(message, model_sbow))})
            r = Response(response=data)
            return r

    def post(self, username):
        return {'post username': username}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80, threaded=True)
