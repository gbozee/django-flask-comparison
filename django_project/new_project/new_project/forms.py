from django import forms
from .models import HealthService
from .models import OrderedService
from .models import SentReport
from .models import UserProfile
from .models import ProviderProfile
from .models import MeasuredTest
from .models import Requests




class ServiceUpdateForm(forms.ModelForm):
        class Meta:
            model = HealthService
       # your_name = forms.CharField(label='Your name', max_length=100)
            fields = ['service_name', 'sub_group', 'details', 'cost', 'cost_denom', 'service_ID','days_available', 'time_available']


class AppointmentForm(forms.ModelForm):
       class Meta:
            model =  OrderedService
            fields = ['preferred_time', 'preferred_date', 'cost', 'promo_code','order_ID','payment_status', 'service_ID','healthier_ID']
            
# class UserProfileForm(forms.ModelForm):
#     class Meta:

#         model = UserProfile


class ProviderProfileForm(forms.ModelForm):
    class Meta:
        model = ProviderProfile
        fields = ['user', 'org_name', 'pro_logo', 'address','city','country', 'provider_ID','phone_number']


class CartForm(forms.ModelForm):
    class Meta:
        model = OrderedService
        fields = ['promo_code', 'cost', 'payment_status', 'service_ID','healthier_ID']


# class OrderedServiceForm(forms.ModelForm):
#     class Meta:
#         model = OrderedService


# class MyHealthForm(forms.ModelForm):
#     class Meta:
#         model = MyHealth


class RequestsForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ['healthier_ID', 'request_date', 'request_type','name','duration', 'rate']
       


class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ['healthier_ID', 'request_date', 'request_type','name','duration', 'rate']
       

# class AmbulReportForm(forms.ModelForm):
#     class Meta:
#         model = AmbulReport


class SentReportForm(forms.ModelForm):
    class Meta:
        model = SentReport
        fields = ['report_type', 'order_ID', 'service_date', 'service_time','name_staff','presenting_complaints', 'exam_findings','treatment_plan','vaccine_expirydate', 'vaccine_batchnumber','next_appointment']
        
class MeasuredTestForm(forms.ModelForm):
    class Meta:
        model = MeasuredTest
        fields = ['order_ID', 'service_date', 'service_test','value','lower_range', 'upper_range']
        

class HealthierForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user','healthier_ID', 'phone_number', 'date_birth', 'gender','text']