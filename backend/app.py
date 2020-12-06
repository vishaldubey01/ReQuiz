#!flask/bin/python
import os
from os.path import join, dirname
import dotenv
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import requests
from pipelines import pipeline
from question_generator.run_qg import get_questions

nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl", qg_format="prepend")

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

def get_free_questions(text):
    text = ''.join([i if ord(i) < 128 else ' ' for i in text])
    questions = nlp(text)
    corrects = []
    for question in questions:
        corrects.append(question['answer'].strip())
    types = ['free_response'] * len(questions)
    return questions, corrects, types

def get_mc_questions(text):
    text = ''.join([i if ord(i) < 128 else ' ' for i in text])
    questions = get_questions(None,
        text,
        num_questions=100,
        answer_style='multiple_choice',
        use_evaluator=True
    )
    corrects = []
    for question in questions:
        for answer in question['answer']:
            if answer['correct']:
                corrects.append(answer['answer'])
                break
    types = ["multiple_choice"] * len(questions)
    return questions, corrects, types

get_auth_token()


'''
test questions
with open('question_generator/articles/innovate.txt') as f:
    text = f.read()
    print()
    print(get_free_questions(text))
    print()
    print(get_mc_questions(text))
'''

if __name__ == '__main__':
    app.run(debug=True)
