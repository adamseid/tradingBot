from django.shortcuts import render
from yahoo_fin.stock_info import *
import time
import queue
from threading import Thread
from django.http import HttpResponse

# Create your views here.
def stockPicker(request):
	stock_picker = tickers_sp500()
	print(stock_picker)
	return render(request, 'mainapp/stockpicker.html', {'stockpicker':stock_picker})

def stockTracker(request):
	stockpicker = request.GET.getlist('stockpicker')
	print(stockpicker)
	data = {}
	available_stocks = tickers_sp500()
	for i in stockpicker:
		if i in available_stocks:
			pass
		else:
			return HttpResponse('Error')

	n_threads = len(stockpicker)
	thread_list = []
	que = queue.Queue()

	start = time.time()
	print(start)
	'''
	for i in stockpicker:
		result = get_quote_table(i)
		data.update(result)
		print(data)
	'''
	for i in range(n_threads):
		thread = Thread(target = lambda q, arg1: q.put({stockpicker[i]: get_quote_table(arg1)}), args=(que, stockpicker[i]))
		thread_list.append(thread)
		thread_list[i].start()

	for thread in thread_list:
		thread.join()

	while not que.empty():
		result = que.get()
		data.update(result)

	end = time.time()
	time_taken = end - start
	print(data)
	print(time_taken)

	return render(request, 'mainapp/stocktracker.html', {'data': data, 'room_name': 'track'})