from celery import Celery

app = Celery(broker='memory://')
