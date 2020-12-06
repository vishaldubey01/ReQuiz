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

def add_text_row(text, userid):
    id = str(uuid.uuid1())
    authtoken = get_auth_token()

    url = "https://1122957d-b459-4289-ae47-61e396ead93e-us-east1.apps.astra.datastax.com/api/graphql/fucknigel"
    
    
    headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://1122957d-b459-4289-ae47-61e396ead93e-us-east1.apps.astra.datastax.com',
    'x-cassandra-token': authtoken
    }
    response = requests.request("POST", url, headers=headers, json={"query":"mutation {\n  bruh: inserttext(\n    value: { id: \""+id+"\", text: \""+text+"\", userid: \""+text+"\" }\n    options: { consistency: LOCAL_QUORUM }\n  ) {\n    value {\n      id\n    }\n  }\n}\n"})
    

    print(response.json())

def add_question_row(question_content, answer, qtype, textid, rating):
    id = str(uuid.uuid1())
    authtoken = get_auth_token()

    url = "https://1122957d-b459-4289-ae47-61e396ead93e-us-east1.apps.astra.datastax.com/api/graphql/fucknigel"
    
    
    headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://1122957d-b459-4289-ae47-61e396ead93e-us-east1.apps.astra.datastax.com',
    'x-cassandra-token': authtoken
    }
    response = requests.request("POST", url, headers=headers, json={"query":"mutation {\n  bruh: insertquestions(\n    value: { id: \""+id+"\", question: \""+question_content+"\", answer: \""+answer+"\", rating: \""+str(rating)+"\", textid: \""+textid+"\", type: \""+qtype+"\" }\n    options: { consistency: LOCAL_QUORUM }\n  ) {\n    value {\n      id\n    }\n  }\n}\n"})
    
    print(response.json())


#add_text_row("hello its vishal", "132342")
add_question_row("What is a sample question?", "an example query", "free response", "23423", 0.91)

#curl 'https://1122957d-b459-4289-ae47-61e396ead93e-us-east1.apps.astra.datastax.com/api/graphql/fucknigel' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Connection: keep-alive' -H 'DNT: 1' -H 'Origin: https://1122957d-b459-4289-ae47-61e396ead93e-us-east1.apps.astra.datastax.com' -H 'x-cassandra-token: 4e27f5cf-d992-460b-9768-19cfe1d36bdd' --data-binary '{"query":"mutation {\n  bruh: inserttext(\n    value: { id: \"0d2aa48e-37ad-11eb-8853-acde48001122\", text: \"Ansh has a dig bick\", userid: \"54321\" }\n    options: { consistency: LOCAL_QUORUM }\n  ) {\n    value {\n      id\n    }\n  }\n}\n"}' --compressed
