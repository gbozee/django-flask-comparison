from django import forms
from .models import HealthService


class ServiceUpdateForm(forms.ModelForm):
        class Meta:
            model = HealthService
       # your_name = forms.CharField(label='Your name', max_length=100)
            fields = ['service_name', 'sub_group', 'details', 'cost', 'cost_denom', 'service_ID','days_available', 'time_available']

# class UserProfileForm(forms.ModelForm):
#     class Meta:

#         model = UserProfile


# class ProviderProfileForm(forms.ModelForm):
#     class Meta:
#         model = ProviderProfile


# # class HealthServiceForm(forms.ModelForm):
# #     class Meta:
# #         model = HealthService


# class OrderedServiceForm(forms.ModelForm):
#     class Meta:
#         model = OrderedService


# class MyHealthForm(forms.ModelForm):
#     class Meta:
#         model = MyHealth


# class TestReportForm(forms.ModelForm):
#     class Meta:
#         model = TestReport


# class AmbulReportForm(forms.ModelForm):
#     class Meta:
#         model = AmbulReport


# class SentReportForm(forms.ModelForm):
#     class Meta:
#         model = SentReport