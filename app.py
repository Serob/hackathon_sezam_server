#!flask/bin/python

from flask import request
from flask_restful import Resource
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from init_api import api, app

@api.route('/users/<string:username>')
class User(Resource):
   
    def get(self, username):
        return {'get username': username}

    def post(self, username):
        return {'post username': username}
		
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)