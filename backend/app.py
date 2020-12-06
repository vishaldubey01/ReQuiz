#!flask/bin/python
from flask import Flask, request, jsonify
from pipelines import pipeline
#from question_generator.run_qg import get_questions
import db

#nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl", qg_format="prepend")

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


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

@app.route('/gen_questions', methods=['GET', 'POST']) #allow both GET and POST requests
def gen_questions(url, text):
    mc_questions, mc_corrects, mc_types = get_mc_questions(text)
    free_questions, free_corrects, free_types = get_free_questions(text)

    textid = url
    # insert into text: text_id, text, userid
    # insert into questions: each generated id (autoinc), content, answer, 'multiple_choice', text_id, 5


    return questions, corrects, types

def gensession(textid):
    # select 10 questions with textid
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
