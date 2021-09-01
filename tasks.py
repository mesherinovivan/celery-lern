from worker import app
from celery.utils.log import get_task_logger
import os

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)



@app.task(name='process_workflow', time_limit=5, soft_time_limit=1, queue='edb')
def process_workflow(payload):
    celery_log.info("test")
    for item in range(100000000):
        item += item * 100
        celery_log.info(item)

