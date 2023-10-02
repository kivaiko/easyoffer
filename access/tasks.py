from easyoffer.celery import app
from .service import delete_access


@app.task
def delete_access_data():
    delete_access()