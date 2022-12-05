from django.shortcuts import render
from yahoo_fin.stock_info import *


# Create your views here.
def tracker(request):
	stock_picker = tickers_sp500()
	print(stock_picker)
	return render(request, 'tracker.html', {'stockpicker':stock_picker})
