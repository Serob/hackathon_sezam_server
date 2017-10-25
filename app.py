#!flask/bin/python

from flask import request, Response, jsonify
from flask_restful import Resource, reqparse
import prediction
from init_api import api, app

model_sbow = prediction.train(0)
model_sg = prediction.train(1)


@api.route('/prediction')
class User(Resource):
    def get(self):
        JSON_NAME="predict worded"
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str, required=True)
        parser.add_argument('method', type=str)
        args = parser.parse_args(strict=True)
        message = args['message']

        if message == '':
            return {JSON_NAME: []}

        method = 'sbow'  # by default
        if list(args.keys()).count('method') == 1:
            method = args['method']
        model_method = model_sg if method == 'sg' else model_sbow

        pred_list = prediction.predict(message, model_method)
        pred_messages = list(map(lambda x: x[0], pred_list)) if pred_list is not None else []
        data = str({JSON_NAME: pred_messages}).replace("'", "\"")
        print(data)
        r = Response(response=data)
        return r

    def post(self, username):
        return {'post username': username}

# remove on uploading hosting server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
