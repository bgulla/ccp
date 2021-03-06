import logging
import sys
#import requests
from flask import Flask, render_template, redirect, url_for, request, session, flash, g, abort, Blueprint, jsonify, session
from flask_restplus import Api, Resource, fields
import json
import dbase
import os
import socket
from contextlib import closing

os.environ["USER"] = "1001"

app = Flask(__name__)
app.secret_key = '027f4073-a5ae-4ec6-a7e2-d730435a5867'

# Fix the swagger http proxy bug
URL_PREFIX = '/api/v1'
from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
api_v1 = Blueprint('api', __name__, url_prefix=URL_PREFIX)
api = Api(api_v1, version='1.0', title='Clarissa Cursing Portal API',
    description='A Dockerized microservice for serving the needs of absolutely no one.',)
ns = api.namespace('curse', description='Did you know? It is 100% impossible for any Clarissa in the world to go 24 days without cursing, let alone 40 days and 40 nights.')

@ns.route('/get')
class CurseCount(Resource):
    '''Show a single todo item and lets you delete them'''
    @api.doc(description='returns the current curse count as an integer')
    def get(self):
        '''Fetch a given resource'''
        return dbase.get_count()

@ns.route('/increment')
class CurseCount(Resource):
    '''Show a single todo item and lets you delete them'''
    @api.doc(description='increments the curse count and returns the updated count as an integer')
    def post(self):
        '''Fetch a given resource'''
        dbase.insert_new_record()
        return dbase.get_count()

@ns.route('/date')
class CurseCount(Resource):
    '''Show a single todo item and lets you delete them'''
    @api.doc(description='returns the last time a record was inserted')
    def get(self):
        '''Fetch a given resource'''

        return dbase.get_last_record()

@app.route('/', methods=['GET', 'POST']) #this is the meat
def home():
    if (request.method == 'POST'):
        dbase.insert_new_record()
    return render_template('index.html', theme="darkly", current_count=dbase.get_count(), last_record_date=dbase.get_last_record())
    #return render_template('404.html', theme="darkly"), 404


if __name__ == '__main__':
    app.config['SWAGGER_UI_DOC_EXPANSION'] = "full"
    app.register_blueprint(api_v1)
    app.run( debug=True, host="0.0.0.0")




