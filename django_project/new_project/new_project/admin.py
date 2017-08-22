# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Customer
from .models import Provider
from .models import HealthService
from .models import OrderedService
from .models import MyHealth
from .models import Requests
from .models import AmbulReport
from .models import SentReport
from .models import ServiceGroup
from .models import ProviderRating
from .models import MeasuredTest





class CustomerAdmin(admin.ModelAdmin):
    class Meta:
        model = Customer


class ProviderAdmin(admin.ModelAdmin):
    class Meta:
        model = Provider


class HealthServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = HealthService


class OrderedServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = OrderedService


class MyHealthAdmin(admin.ModelAdmin):
    class Meta:
        model = MyHealth


class RequestsAdmin(admin.ModelAdmin):
    class Meta:
        model = Requests


class AmbulReportAdmin(admin.ModelAdmin):
    class Meta:
        model = AmbulReport


class SentReportAdmin(admin.ModelAdmin):
    class Meta:
        model = SentReport




class ServiceGroupResource(resources.ModelResource):
    def get_instance(self, instance_loaders, row):
        return False

    class Meta:
        model = ServiceGroup
        fields = ('id', 'category', 'group', 'service', 'group_id', 'category_id',)


class ServiceGroupAdmin(ImportExportModelAdmin):
        resource_class = ServiceGroupResource
    
    # class Meta:
    #     model = ServiceGroup
    #     import_id_fields = ('category id',)
    #     fields = ('id','category', 'group', 'service', 'group id', 'category id',)


class ProviderRatingAdmin(admin.ModelAdmin):
    class Meta:
        model = ProviderRating


class MeasuredTestAdmin(admin.ModelAdmin):
    class Meta:
        model = MeasuredTest


# class BookAdmin(ImportExportModelAdmin):
#     resource_class = ServiceResource


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(HealthService, HealthServiceAdmin)
admin.site.register(Requests, RequestsAdmin)
admin.site.register(MyHealth, MyHealthAdmin)
admin.site.register(OrderedService, OrderedServiceAdmin)
admin.site.register(AmbulReport, AmbulReportAdmin)
admin.site.register(SentReport, SentReportAdmin)
admin.site.register(ServiceGroup, ServiceGroupAdmin)
admin.site.register(ProviderRating, ProviderRatingAdmin)
admin.site.register(MeasuredTest, MeasuredTestAdmin)





# Register your models here.
