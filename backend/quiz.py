from pipelines import pipeline

nlp = pipeline("question-generation", model="valhalla/t5-base-qg-hl", qg_format="prepend")

def get_questions(text):
    text = ''.join([i if ord(i) < 128 else ' ' for i in text])
    return nlp(text)
