from django.contrib import admin
from .models import Worker, SalePoint, Visit

class WorkerAdmin(admin.ModelAdmin):
	list_display = ("worker_name", "worker_phone")
	search_fields = ("worker_name", "worker_phone")


class SalePointAdmin(admin.ModelAdmin):
	list_display = ("id", "sale_point_name",)
	search_fields = ("worker",)


class VisitAdmin(admin.ModelAdmin):
	list_display = ("display_sale_point_name", "date_time", "latitude", "longitude")
	search_fields = ("sale_point__sale_point_name", "sale_point__worker_id__worker_name")

	def display_sale_point_name(self, arg):

		return SalePoint.objects.filter(id=arg.sale_point_id)[0].sale_point_name

	display_sale_point_name.short_description = 'Торговая точка'


admin.site.register(Worker, WorkerAdmin)
admin.site.register(SalePoint, SalePointAdmin)
admin.site.register(Visit, VisitAdmin)
