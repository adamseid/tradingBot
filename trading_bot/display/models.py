from django.db import models

class Status(models.Model):
	time = models.DateTimeField(auto_now_add=True)
	BUTTON_1 = models.CharField(max_length=100, default='OFF')
	BUTTON_2 = models.CharField(max_length=100, default='OFF')



class Snippet(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='chicken')


	class Meta:
		ordering = ['created']

