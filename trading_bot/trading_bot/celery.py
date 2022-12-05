from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trading_bot.settings')

#app = Celery('celery_tutorial')
app = Celery('trading_bot')
app.conf.update(timezone='US/Eastern')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {

#    'every-10-seconds' : {
#        'task': 'mainapp.tasks.update_stock',
#        'schedule': 10,
#        'args': (['CVX', 'AAPL'],)
#    },

    "see-you-in-ten-seconds-task": {
        "task": "mainapp.tasks.printHi",
        "schedule": 10.0
    },

    
    "backup-tables" : {
        'task': 'tracker.tasks.backup',
        'schedule': 600.0,
    },
    
    "update": {
        'task': 'tracker.tasks.update',
        'schedule': 60.0
    },

    "test": {
        'task': 'tracker.tasks.test',
        'schedule': 10.0
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))




