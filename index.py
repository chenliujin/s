#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by vellhe 2017/7/9
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

class price_distribute(Resource):
  def get(self):
    return jsonify([
        {
          'price': 11.75,
          'buy': 1000,
          'sale': 0 
        },
        {
          'price': 13.5,
          'buy': 300,
          'sale': 400
        },
        {
          'price': 14.5,
          'buy': 500,
          'sale': 500
        },
        {
          'price': 15,
          'buy': 0,
          'sale': 500
        },
        {
          'price': 16,
          'buy': 200,
          'sale': 200
        }
    ])

api.add_resource(price_distribute, '/v1/price_distribute/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


