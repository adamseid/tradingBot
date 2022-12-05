from django.shortcuts import render, redirect
from django.views import View
from .models import Status, Snippet
from .serializers import SnippetSerializer, StatusSerializer



class MainView(View):
	def get(self, request):
		print('MainView: get')

		



		status = Status()
		serializer = StatusSerializer(status)


		return render(request, 'display/main.html', serializer.data)

