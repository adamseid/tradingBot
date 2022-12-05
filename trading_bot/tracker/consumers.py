from channels.generic.websocket import AsyncWebsocketConsumer
import json
from urllib.parse import parse_qs
from asgiref.sync import sync_to_async, async_to_sync
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from .task_modules.misc import Misc
import os
from .consumer_modules import Navigator, Connect, Display




class Tracker(AsyncWebsocketConsumer):
    @sync_to_async
    def addToCeleryBeat(self):
        print('Tracker.addToCeleryBeat(): STARTED')
        try:
            schedule, created = IntervalSchedule.objects.get_or_create(every=10, period=IntervalSchedule.SECONDS)
            task = PeriodicTask.objects.create(interval=schedule, name='tracker', task='tracker.tasks.test')
            print('Tracker.addToCeleryBeat(): FINISHED')
        except:
            print('Tracker.addToCeleryBeat():  ERROR')



    async def connect(self):
        print('StockConsumer.connect(): STARTED')

        Connect.run()

        self.room_name = 'tracker'
        self.room_group_name = 'crypto'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        print('joined room')

        # add to celery beat
        await self.addToCeleryBeat()

        await self.accept()
        await self.send(text_data=json.dumps({
            'response': 'hi',
            'data': {
                'location': []
            }
        }))

        print('StockConsumer.connect(): FINISHED')

    async def receive(self, text_data):
        Misc.printDebug('Tracker.receive(): STARTED')
        print(text_data)
        
        request = json.loads(text_data)['request']
        data = json.loads(text_data)['data']
        response = request

        if request == 'listdir':
            response = request
            data = Navigator.listdir(data)
            print('request: listdir')

        if request == 'select':
            print('request == select')

        if request == 'connect':
            print('reqeust == connect')
            print(request)
            print(data)
            response = request
            data = Display.connect(data)

        await self.send(text_data=json.dumps({
            'response': response,
            'data': data
        }))



        Misc.printDebug('Tracker.receive(): FINISHED')




    async def updateCurrent(self, event):
        print(event)
        data = event['data']
        await self.send(text_data=json.dumps({
            'command': 'update-current',
            'data': data
        }))

    async def updateGraph(self, event):
        print(event)
        data = event['data']
        await self.send(text_data=json.dumps({
            'command': 'update-graph',
            'data': data
        }))


    async def disconnect(self, data):
        Misc.printDebug('Tracker.disconnect(): STARTED')
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        Misc.printDebug('Tracker.disconnect(): FINISHED')
