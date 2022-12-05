from celery import shared_task
from yahoo_fin.stock_info import *
from threading import Thread
import queue
from channels.layers import get_channel_layer
import asyncio
import logging
import simplejson as json


@shared_task()
def printHi():
	print('Hi there')


@shared_task(bind=True)
def update_stock(self, stockpicker):
	print('update_stock: STARTED')
	data = {}
	available_stocks = tickers_sp500()
	for i in stockpicker:
		if i in available_stocks:
			pass
		else:
			stockpicker.remove(i)

	n_threads = len(stockpicker)
	thread_list = []
	que = queue.Queue()

	for i in range(n_threads):
		thread = Thread(target = lambda q, arg1: q.put({stockpicker[i]: json.loads(json.dumps(get_quote_table(arg1), ignore_nan = True))}), args = (que, stockpicker[i]))		
		thread_list.append(thread)
		thread_list[i].start()
		logging.info("Main    : wait for the thread to finish")

	print('thread_list: ', thread_list)

	for thread in thread_list:
		thread.join()
		logging.info("Main    : all done")

	while not que.empty():
		result = que.get()
		data.update(result)

	print('data: ', data)
	print('finished creating threads')

	# Send data to group
	channel_layer = get_channel_layer()
	loop = asyncio.new_event_loop()

	asyncio.set_event_loop(loop)

	loop.run_until_complete(channel_layer.group_send('stock_track', {
		'type': 'send_stock_update',
		'message': data,
		}))

	print('update_stock: FINISHED')
	
	return 'Done'








