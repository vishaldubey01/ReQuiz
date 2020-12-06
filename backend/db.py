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

    url = "https://"+ASTRA_CLUSTER_ID+"-"+ASTRA_CLUSTER_REGION+".apps.astra.datastax.com/api/graphql/fucknigel"


    headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://'+ASTRA_CLUSTER_ID+'-'+ASTRA_CLUSTER_REGION+'.apps.astra.datastax.com',
    'x-cassandra-token': authtoken
    }
    text = "hi" # why do we need to store text?
    response = requests.request("POST", url, headers=headers, json={"query":"mutation {\n  bruh: inserttext(\n    value: { id: \""+id+"\", text: \""+text+"\", userid: \""+text+"\" }\n    options: { consistency: LOCAL_QUORUM }\n  ) {\n    value {\n      id\n    }\n  }\n}\n"})


    print(response.json())
    retid = response.json()['data']['bruh']['value']['id']
    print(retid)
    return retid

def add_question_row(question_content, answer, qtype, textid):
    id = str(uuid.uuid1())
    authtoken = get_auth_token()

    url = "https://"+ASTRA_CLUSTER_ID+"-"+ASTRA_CLUSTER_REGION+".apps.astra.datastax.com/api/graphql/fucknigel"


    headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://'+ASTRA_CLUSTER_ID+'-'+ASTRA_CLUSTER_REGION+'.apps.astra.datastax.com',
    'x-cassandra-token': authtoken
    }
    response = requests.request("POST", url, headers=headers, json={"query":"mutation {\n  bruh: insertquestions(\n    value: { id: \""+id+"\", question: \""+question_content+"\", answer: \""+answer+"\", rating: \""+str(1.00)+"\", textid: \""+textid+"\", type: \""+qtype+"\" }\n    options: { consistency: LOCAL_QUORUM }\n  ) {\n    value {\n      id\n    }\n  }\n}\n"})

    print(response.json())
    return response.json()

def get_all_text_questions(textid):
    authtoken = get_auth_token()

    url = "https://"+ASTRA_CLUSTER_ID+"-"+ASTRA_CLUSTER_REGION+".apps.astra.datastax.com/api/graphql/fucknigel"


    headers = {
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://'+ASTRA_CLUSTER_ID+'-'+ASTRA_CLUSTER_REGION+'.apps.astra.datastax.com',
    'x-cassandra-token': authtoken
    }
    responseQuestions = requests.request("POST", url, headers=headers, json={"query":"query {\n  questions(options:{limit: 10000}) {\n    values {\n      id\n      question\n      answer\n    textid\n    type\n    }\n  }\n}"})
    responseTexts = requests.request("POST", url, headers=headers, json={"query":"query {\n  text(options:{limit: 10000}) {\n    values {\n      id\n      text\n      userid\n    }\n  }\n}"})


    questionRes = responseQuestions.json()
    textRes = responseTexts.json()

    questionsMatch = []
    textMatch = {}

    for question in questionRes['data']['questions']['values']:
        if question['textid'] == textid:
            questionsMatch.append(question)

    for text in textRes['data']['text']['values']:
        if text['id'] == textid:
            textMatch = text

    ret = {
        "questions": questionsMatch,
        "textInformation": textMatch
    }
    print(ret)
    return ret



# THESE ARE TESTING RUNS:
get_all_text_questions("7aa65814-37d5-11eb-9df7-acde48001122")
#get_all_text_questions("d6354fb8-37bd-11eb-8ef2-acde48001122")
#get_all_text_questions("91fc7528-37c8-11eb-a809-acde48001122")
#get_all_text_questions("bf679b14-37c8-11eb-a614-acde48001122")
#text_id_returned = add_text_row("I'm a cool guy", "69")
#add_question_row("What is a sam?", "an example dmb query", "free response", text_id_returned)
