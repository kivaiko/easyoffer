from easyoffer.celery import app
from .service import count_words


@app.task
def count_words_for_search(url):
    count_words(url)


# @app.task
# def printer():
#     print("i'm task")