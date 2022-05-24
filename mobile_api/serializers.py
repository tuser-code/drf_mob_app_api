from rest_framework import serializers
from .models import Worker, SalePoint, Visit


class WorkerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Worker
		fields = ('worker_name', 'worker_phone')


class SalePointSerializer(serializers.ModelSerializer):
	class Meta:
		model = SalePoint
		fields = ('id', 'sale_point_name',)

class VisitSerializer(serializers.ModelSerializer):
	class Meta:
		model = Visit
		fields = ('sale_point', 'latitude', 'longitude',)

	# def validate(self):
	# 	