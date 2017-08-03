# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import UserProfile
from .models import ProviderProfile
from .models import HealthService
from .models import OrderedService
from .models import MyHealth
from .models import TestReport
from .models import AmbulReport
from .models import SentReport




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


class TestReportAdmin(admin.ModelAdmin):
    class Meta:
        model = TestReport


class AmbulReportAdmin(admin.ModelAdmin):
    class Meta:
        model = AmbulReport


class SentReportAdmin(admin.ModelAdmin):
    class Meta:
        model = SentReport


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProviderProfile, ProviderProfileAdmin)
admin.site.register(HealthService, HealthServiceAdmin)
admin.site.register(TestReport, TestReportAdmin)
admin.site.register(MyHealth, MyHealthAdmin)
admin.site.register(OrderedService, OrderedServiceAdmin)
admin.site.register(AmbulReport, AmbulReportAdmin)
admin.site.register(SentReport, SentReportAdmin)




# Register your models here.
