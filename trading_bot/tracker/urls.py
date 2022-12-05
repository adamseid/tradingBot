from django.urls import path, include
from . import views

urlpatterns = [
	path('tracker/', views.tracker, name='tracker'),
]