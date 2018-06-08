#!/usr/bin/env python

from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

class priceDistribute(Resource):
  def get(self):
    from model import price_distribute

    parser = reqparse.RequestParser()
    parser.add_argument('starttime')
    parser.add_argument('endtime')

    params = parser.parse_args()

    return price_distribute.index(params)

api.add_resource(priceDistribute, '/v1/price_distribute/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


