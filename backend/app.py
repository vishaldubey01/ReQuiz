#!flask/bin/python
from flask import Flask, request, jsonify
from pipelines import pipeline
import db
from db import add_text_row, add_question_row, get_all_text_questions, add_session_row, add_interaction_row
import requests
import json
import random
import uuid

#nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl", qg_format="prepend")

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

'''
def get_free_questions(text):
    #text = ''.join([i if ord(i) < 128 else ' ' for i in text])
    questions = nlp(text)
    corrects = []

    for question in questions:
        corrects.append(question['answer'].strip())
    types = ['free_response'] * len(questions)
    return questions, corrects, types


def get_mc_questions(text):
    #text = ''.join([i if ord(i) < 128 else ' ' for i in text])
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

    return questions
'''

@app.route('/gen_questions', methods=['GET', 'POST']) #allow both GET and POST requests
def gen_questions(text, title, userid):
    text = ''.join([i if ord(i) < 128 else ' ' for i in text])
    mc_url = 'https://us-central1-duke-classes-285719.cloudfunctions.net/get_mc_questions'
    response = requests.post(mc_url, json={"text" : text})
    print(response)
    print(response.text)
    mc_questions = json.loads(response.text)

    mc_corrects = []
    for question in mc_questions:
        for answer in question['answer']:
            if answer['correct']:
                mc_corrects.append(answer['answer'])
                break

    #free_questions, free_corrects, free_types = get_free_questions(text)

    #textid = url
    # insert into text: text_id, text, userid
    # insert into questions: each generated id (autoinc), content, answåår, 'multiple_choice', text_id, 5

    textid = add_text_row(title, userid)
    print('text id', textid)

    for i in range(len(mc_questions)):
        question_content = mc_questions[i]['question']
        question_content = question_content[0].upper() + question_content[1:] # capitalize
        answer = mc_corrects[i]
        qtype = 'multiple_choice'
        add_question_row(question_content, answer, qtype, textid)

    # first add text to db
    # ^ response includes an id like eda433e6-37bb-11eb-b96f-acde48001122
    # add each question to db using add_question_row function and passing in the id above as textid parameter

'''
with open('question_generator/articles/innovate.txt') as f:
    text = f.read()
    print(text)
    gen_questions(text, 'ramisbahi')
'''

def gensession(textid):
    # select 10 questions with textid
    questions_and_info = get_all_text_questions(textid)
    questions = questions_and_info['questions']
    textid = questions_and_info['textInformation']['id']
    userid = 'ramisbahi'
    sessionid = str(uuid.uuid1())
    session_questions = random.sample(questions, min(len(questions) / 2, 10)) # half of questions or 10, whichever is less
    questionids = []
    for question in session_questions:
        add_interaction_row(question['id'], sessionid)
        questionids.append(question['id'])

    add_session_row(sessionid, userid, textid, questionids)

def availablesessions(userid):
    #get_all_text
    pass


def answer(textid, questionid, useranswer):
    # select answer where id = question_id
    if answer == useranswer:
        print('correct')
    else:
        print('false')

def getsession(sessionid):
    # select interactions with session id
    # sort by id (ascending b/c serial)
    pass

def sessionhistory(userid):
    # select sessions with user id
    for session in sessions:
        # select interactions with session id =
        continue


# #test questions
# with open('question_generator/articles/innovate.txt') as f:
#     text = f.read()
#     print()
#     print(get_free_questions(text))
#     print()
#     print(get_mc_questions(text))


if __name__ == '__main__':
    app.run(debug=True)
