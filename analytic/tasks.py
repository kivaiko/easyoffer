from easyoffer.celery import app
from .service import count_words


@app.task
def get_analytic_from_hh_api():
    count_words()

