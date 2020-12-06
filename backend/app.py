#!flask/bin/python
import os
from os.path import join, dirname
import dotenv
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import requests

load_dotenv()

ASTRA_CLUSTER_ID = os.getenv('ASTRA_CLUSTER_ID')
ASTRA_CLUSTER_REGION = os.getenv('ASTRA_CLUSTER_REGION')
ASTRA_DB_USERNAME = os.getenv('ASTRA_DB_USERNAME')
ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')
ASTRA_DB_PASSWORD = os.getenv('ASTRA_DB_PASSWORD')

#print(ASTRA_CLUSTER_ID)
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

def get_auth_token():
    url = "https://"+ASTRA_CLUSTER_ID+"-"+ASTRA_CLUSTER_REGION+".apps.astra.datastax.com/api/rest/v1/auth"
    obj = {
        "username":ASTRA_DB_USERNAME,
        "password":ASTRA_DB_PASSWORD
    }
    print(url)
    print(obj)
    x = requests.post(url, data = obj)
    print(x.json())


get_auth_token()

if __name__ == '__main__':
    app.run(debug=True)