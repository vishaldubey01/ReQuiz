import os
from os.path import join, dirname
import dotenv
from dotenv import load_dotenv
import requests
import json
import uuid

load_dotenv()

ASTRA_CLUSTER_ID = os.getenv('ASTRA_CLUSTER_ID')
ASTRA_CLUSTER_REGION = os.getenv('ASTRA_CLUSTER_REGION')
ASTRA_DB_USERNAME = os.getenv('ASTRA_DB_USERNAME')
ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')
ASTRA_DB_PASSWORD = os.getenv('ASTRA_DB_PASSWORD')

# from cassandra.cluster import Cluster
# from cassandra.auth import PlainTextAuthProvider

# cloud_config= {
#         'secure_connect_bundle': 'secure-connect-hackduke.zip'
# }
# auth_provider = PlainTextAuthProvider('ansh', 'password')
# cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
# session = cluster.connect()

# row = session.execute("select release_version from system.local").one()
# if row:
#     print(row[0])
# else:
#     print("An error occurred.")



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
    print("AUTH TOKEN: "+process_res)
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

def add_text_row(id, text, userid):
    authtoken = get_auth_token()

    url = "https://1122957d-b459-4289-ae47-61e396ead93e-us-east1.apps.astra.datastax.com/api/graphql/fucknigel"
    payload={
        "query": "mutation {book: inserttext(data:{id: \""+id+"\", text: \""+text+"\", userid: \""+userid+"\"} options: { consistency: LOCAL_QUORUM }){value {id}}}"
    }
    headers = {
    'Content-Type': 'application/json',
    'x-cassandra-token': authtoken
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    print(response.json())

# curl --request POST \
#   --url https://$ASTRA_CLUSTER_ID-$ASTRA_CLUSTER_REGION.apps.astra.datastax.com/api/graphql/{keyspaceName} \
#   --header 'accept: application/json' \
#   --header 'content-type: application/json' \
#   --header 'x-cassandra-request-id: {unique-UUID}' \
#   --header "x-cassandra-token: $ASTRA_AUTHORIZATION_TOKEN" \
#   --data-raw '{"query":"mutation {objectName: insertName(data:{columnName1:\"value1 A1\" columnName2:\"value2 A.\"columnName3: \"value3\" columnName4: \"value1\"}){value {columnName1 columnName2 columnName3 columnName4}}}","variables":{}}'

ia = str(uuid.uuid1())
print("ID: "+ia)
add_text_row(ia, "hello ansh", "132342")
