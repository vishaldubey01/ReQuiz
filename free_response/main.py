from flask import Flask, request, jsonify
from pipelines import pipeline

nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl", qg_format="prepend")

def get_free_questions(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    text = request.get_data()
    text = ''.join([i if ord(i) < 128 else ' ' for i in text])
    questions = nlp(text)
    corrects = []
    for question in questions:
        corrects.append(question['answer'].strip())
    types = ['free_response'] * len(questions)
    return questions, corrects, types
