from django import forms
from .models import (HealthService,OrderedService,SentReport,Customer,
Provider,MeasuredTest,Requests,ServiceGroup,)
from django.forms import (TextInput,DateInput,SelectDateWidget,extras)
from django.contrib.admin.widgets import AdminDateWidget




# class UserProfileForm(forms.ModelForm):
#     class Meta:

#         model = UserProfile





class CartForm(forms.ModelForm):
    class Meta:
        model = OrderedService
        fields = ['promo_code', 'cost', 'service_ID', 'healthier_ID']
#service provider, service,
# 

class ServiceListForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['org_name', 'pro_logo', 'address', 'city', 'country', 'likes', 'dislike', ] 


class ServiceListForm1(forms.ModelForm):
    class Meta:
        model = HealthService
        fields = ['Service', 'details', 'cost','service_ID', 'days_available','time_available', ] 

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = OrderedService
        fields = ['preferred_time', 'preferred_date', 'cost', ]


# class MyHealthForm(forms.ModelForm):
#     class Meta:
#         model = MyHealth

# class AmbulReportForm(forms.ModelForm):
#     class Meta:
#         model = AmbulReport


class RequestsForm(forms.ModelForm):
    healthier_ID = forms.ModelChoiceField(queryset=OrderedService.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))            
    class Meta:
        model = Requests
        fields = ['request_date','request_type', 'name', 'duration', 'rate']


class HealthierForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user', 'healthier_ID', 'phone_number',
                  'date_birth', 'gender', 'text']

#Dashboard Forms                  

class QuoteRequestForm(forms.ModelForm):
    healthier_ID = forms.ModelChoiceField(queryset=Requests.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))        
    request_type = forms.ModelChoiceField(queryset=Requests.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))        
    
    class Meta:
        model = Requests
        fields = ['healthier_ID', 'request_date',
                  'request_type', 'name', 'duration', 'rate']



class SentReportForm(forms.ModelForm):
    healthier_ID = forms.ModelChoiceField(queryset=SentReport.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))        
    report_type = forms.ModelChoiceField(queryset=SentReport.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))    
    order_ID = forms.ModelChoiceField(queryset=SentReport.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
   # service_date = forms.DateField(widget=extras.SelectDateWidget),
    service_date = forms.DateField(widget=AdminDateWidget())
    
    class Meta:
        model = SentReport
        fields = ['healthier_ID', 'report_type', 'order_ID', 'service_date', 'service_time', 'name_staff', 'presenting_complaints',
                  'exam_findings', 'treatment_plan', 'vaccine_expirydate', 'vaccine_batchnumber', 'next_appointment']
      
        widgets = {
           # 'service_date': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
           # 'service_date' : DateInput(attrs={'type': 'date'}),
            'service_time': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'name_staff': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'presenting_complaints': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'exam_findings': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'treatment_plan': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'vaccine_expirydate': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'vaccine_batchnumber': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'next_appointment': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
        }


class MeasuredTestForm(forms.ModelForm):
    healthier_ID = forms.ModelChoiceField(queryset=MeasuredTest.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))       
    order_ID = forms.ModelChoiceField(queryset=MeasuredTest.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = MeasuredTest
        fields = ['healthier_ID', 'order_ID', 'service_date', 'service_test',
                  'value', 'lower_range', 'upper_range']
        widgets = {
            'service_date': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'service_test': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'value': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'lower_range': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'upper_range': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}), }


class OrderedServiceForm(forms.ModelForm):
    class Meta:
        model = OrderedService
        fields = ['preferred_time', 'preferred_date', 'cost', 'promo_code',
                  'order_ID', 'payment_status', 'service_ID', 'healthier_ID']


class ServiceUpdateForm(forms.ModelForm):
    Category = forms.ModelChoiceField(queryset=ServiceGroup.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))    
    sub_group = forms.ModelChoiceField(queryset=ServiceGroup.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    Service = forms.ModelChoiceField(queryset=ServiceGroup.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = HealthService
        fields = ['Category','sub_group','Service', 'details', 'cost',
                  'cost_denom', 'service_ID', 'days_available', 'time_available']

        widgets = {
            'Category': TextInput(attrs={'class': "form-control"}),
            'sub-group': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'Service': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'details': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'cost': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'cost_denom': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'service_ID': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'days_available': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'time_available': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
        }


        
class ProviderProfileForm(forms.ModelForm):
    org_name = forms.ModelChoiceField(queryset=Provider.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))        
    class Meta:
        model = Provider
        fields = ['user', 'org_name', 'pro_logo', 'address',
                  'city', 'country', 'provider_ID', 'phone_number']