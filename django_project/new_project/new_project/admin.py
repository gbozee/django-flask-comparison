# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import UserProfile
from .models import ProviderProfile
from .models import HealthService
from .models import OrderedService
from .models import MyHealth
from .models import Requests
from .models import AmbulReport
from .models import SentReport
from .models import ServiceGroup
from .models import ProviderRating
from .models import MeasuredTest





class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile


class ProviderProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = ProviderProfile


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



class ServiceGroupAdmin(admin.ModelAdmin):
    class Meta:
        model = ServiceGroup


class ProviderRatingAdmin(admin.ModelAdmin):
    class Meta:
        model = ProviderRating


class MeasuredTestAdmin(admin.ModelAdmin):
    class Meta:
        model = MeasuredTest


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProviderProfile, ProviderProfileAdmin)
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
