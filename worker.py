from celery import Celery
import os


app = Celery(
    'skipper_celery_api',
    broker=os.getenv('RABBITMQ_BROKER'),
    backend='rpc://',
    include=['tasks']
)

# app.control.time_limit('process_workflow',
#                            soft=1, hard=2, reply=True)
