import os
from os.path import join, dirname
import dotenv
from dotenv import load_dotenv
import requests
import json

load_dotenv()

ASTRA_CLUSTER_ID = os.getenv('ASTRA_CLUSTER_ID')
ASTRA_CLUSTER_REGION = os.getenv('ASTRA_CLUSTER_REGION')
ASTRA_DB_USERNAME = os.getenv('ASTRA_DB_USERNAME')
ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')
ASTRA_DB_PASSWORD = os.getenv('ASTRA_DB_PASSWORD')


def get_auth_token():
    url = "https://"+ASTRA_CLUSTER_ID+"-"+ASTRA_CLUSTER_REGION+".apps.astra.datastax.com/api/rest/v1/auth"
    payload={
        "username": "ansh",
        "password": "password"
    }
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    process_res = response.json()['authToken']
    print(process_res)
    return process_res



def create_text_table():
    authtoken = get_auth_token()

    url = "https://"+ASTRA_CLUSTER_ID+"-"+ASTRA_CLUSTER_REGION+".apps.astra.datastax.com/api/rest/v1/keyspaces/"+ASTRA_DB_KEYSPACE+"/tables"
    payload={
        "name": "text",
        "ifNotExists":True,
        "columnDefinitions": [
            {
                "name":"id",
                "typeDefinition":"uuid",
                "static":False
            },
            {
                "name":"text",
                "typeDefinition":"text",
                "static":False
            },
            {
                "name":"userid",
                "typeDefinition":"text",
                "static":False
            }
        ],
        "primaryKey": {
            "partitionKey": ["id"]
        },
        "tableOptions": {
            "defaultTimeToLive": 0
        }
    }
    headers = {
    'Content-Type': 'application/json',
    'x-cassandra-token': authtoken
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    print(response.json())

def create_sessions_table():
    authtoken = get_auth_token()

    url = "https://"+ASTRA_CLUSTER_ID+"-"+ASTRA_CLUSTER_REGION+".apps.astra.datastax.com/api/rest/v1/keyspaces/"+ASTRA_DB_KEYSPACE+"/tables"
    payload={
        "name": "sessions",
        "ifNotExists":True,
        "columnDefinitions": [
            {
                "name":"id",
                "typeDefinition":"uuid",
                "static":False
            },
            {
                "name":"userid",
                "typeDefinition":"text",
                "static":False
            },
            {
                "name":"textid",
                "typeDefinition":"text",
                "static":False
            },
            {
                "name":"lastdate",
                "typeDefinition":"timestamp",
                "static":False
            },
            {
                "name":"questionids",
                "typeDefinition":"set<text>",
                "static":False
            }
        ],
        "primaryKey": {
            "partitionKey": ["id"]
        },
        "tableOptions": {
            "defaultTimeToLive": 0
        }
    }
    headers = {
    'Content-Type': 'application/json',
    'x-cassandra-token': authtoken
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    print(response.json())


def create_questions_table():
    authtoken = get_auth_token()

    url = "https://"+ASTRA_CLUSTER_ID+"-"+ASTRA_CLUSTER_REGION+".apps.astra.datastax.com/api/rest/v1/keyspaces/"+ASTRA_DB_KEYSPACE+"/tables"
    payload={
        "name": "questions",
        "ifNotExists":True,
        "columnDefinitions": [
            {
                "name":"id",
                "typeDefinition":"uuid",
                "static":False
            },
            {
                "name":"question",
                "typeDefinition":"text",
                "static":False
            },
            {
                "name":"answer",
                "typeDefinition":"text",
                "static":False
            },
            {
                "name":"type",
                "typeDefinition":"text",
                "static":False
            },
            {
                "name":"textid",
                "typeDefinition":"text",
                "static":False
            },
            {
                "name":"rating",
                "typeDefinition":"decimal",
                "static":False
            }
        ],
        "primaryKey": {
            "partitionKey": ["id"]
        },
        "tableOptions": {
            "defaultTimeToLive": 0
        }
    }
    headers = {
    'Content-Type': 'application/json',
    'x-cassandra-token': authtoken
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    print(response.json())

#create_questions_table()