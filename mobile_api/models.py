from django.db import models


class Worker(models.Model):
	worker_name = models.CharField(max_length=255, verbose_name='ФИО')
	worker_phone = models.CharField(max_length=255, verbose_name="Телефон")

	class Meta:
		verbose_name = 'Сотрудники'
		verbose_name_plural = 'Сотрудники'


class SalePoint(models.Model):
	worker = models.ForeignKey(Worker, on_delete=models.PROTECT, verbose_name="Сотрудник")
	sale_point_name = models.CharField(max_length=255, verbose_name="Наименование торговой точки")

	class Meta:
		verbose_name = 'Торговые точки'
		verbose_name_plural = 'Торговые точки'


class Visit(models.Model):
	sale_point = models.ForeignKey(SalePoint, on_delete=models.PROTECT, verbose_name="Торговая точка")
	date_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
	latitude = models.FloatField(verbose_name="Широта")
	longitude = models.FloatField(verbose_name="Долгота")

	class Meta:
		verbose_name = 'Посещения'
		verbose_name_plural = 'Посещения'