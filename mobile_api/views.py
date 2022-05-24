from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import serializers

from .models import Worker, SalePoint, Visit
from .serializers import WorkerSerializer, SalePointSerializer, VisitSerializer


class WorkerAPIView(generics.ListAPIView):
	queryset = Worker.objects.all()
	serializer_class = WorkerSerializer

class SalePointAPIView(generics.ListAPIView):
	queryset = SalePoint.objects.all()
	serializer_class = SalePointSerializer

	def get(self, request, worker_phone):
		worker = Worker.objects.filter(worker_phone=worker_phone)[0]
		queryset = SalePoint.objects.filter(worker=worker)
		return Response({'sale_points': SalePointSerializer(queryset, many=True).data})


class VisitAPIView(generics.ListAPIView):
	queryset = SalePoint.objects.all()
	serializer_class = SalePointSerializer

	def post(self, request, worker_phone):
		worker = Worker.objects.filter(worker_phone=worker_phone)
		if not worker:
			raise serializers.ValidationError({"error":"Not registered"})
		worker_phone_requested = worker[0].worker_phone
		serializer = VisitSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		worker_phone = serializer.validated_data['sale_point'].worker.worker_phone
		if worker_phone != worker_phone_requested:
			raise serializers.ValidationError({"error":"Not allowed"})
		serializer.save()

		return Response({'post': serializer.data})