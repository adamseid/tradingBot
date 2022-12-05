from rest_framework import serializers
from .models import Status

class SnippetSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False, allow_blank=True, max_length=100)



class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = '__all__'
