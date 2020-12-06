from flask import Flask, request, jsonify
from run_qg import get_questions

def get_mc_questions(request):
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
