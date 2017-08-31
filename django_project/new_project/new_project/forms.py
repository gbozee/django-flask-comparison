from django import forms
from .models import (HealthService,OrderedService,SentReport,Customer,
Provider,MeasuredTest,Requests,ServiceGroup,ProviderRating, MyHealth)
from django.forms import (TextInput,DateInput,SelectDateWidget,extras, )
from django.contrib.admin.widgets import AdminDateWidget
import datetime
from datetimewidget.widgets import DateTimeWidget



#USER FORMS
class CustomerForm(forms.ModelForm):
    user_pix = forms.ImageField(label='Choose Profile Image') 
    class Meta:
        model = Customer
        fields = ['user_pix', 'date_birth','phone_number', 'last_name','first_name', 'gender','text',]



class MyHealthForm(forms.ModelForm):
    SYSTOLIC_BLOOD_PRESSURE = 'Systolic Blood Pressure'
    DIASTOLIC_BLOOD_PRESSURE = 'Diastolic Blood Pressure'
    RANDOM_BLOOD_SUGAR = 'Random Blood Sugar'
    FASTING_BLOOD_SUGAR = 'Fasting Blood Sugar'
    WEIGHT = 'Weight'
    CHOLESTEROL = 'Cholseterol'
    CURRENT_DRUGS = 'Current Drugs'
    health_data = forms.ChoiceField(choices=(
                           (SYSTOLIC_BLOOD_PRESSURE, 'Systolic Blood Pressure'),
                           (DIASTOLIC_BLOOD_PRESSURE, 'Diastolic Blood Pressure'),
                           (RANDOM_BLOOD_SUGAR, 'Random Blood Sugar'),
                           (FASTING_BLOOD_SUGAR, 'Fasting Blood Sugar'),
                           (WEIGHT, 'Weight'),
                           (CHOLESTEROL, 'Cholesterol'),
                           (CURRENT_DRUGS,'Current Drugs')), widget=forms.Select(attrs={'class':'form-control'}))
    service_date = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class':"w3-input w3-border w3-round-large"}))
                           
    class Meta:
        model = MyHealth
        fields = ['service_date', 'health_data','data_value', ]
        
        widgets = {
            'data_value': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
        }


class PersonalHealthForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name','date_birth', 'phone_number', ]


class MeasuredUserForm(forms.ModelForm):
    result = forms.ModelChoiceField(queryset=MeasuredTest.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))       
    class Meta:
        model = MeasuredTest
        fields = ['service_date', 'service_test',
                  'value', 'lower_range', 'upper_range']
        widgets = {
            'service_date': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'service_test': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'value': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'lower_range': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'upper_range': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}), }

class UserReportForm(forms.ModelForm):
    class Meta:    
        model = SentReport
        fields = ['service_date','report_type', 'general_findings', 'treatment_plan', 'next_appointment','name_staff',
                  'vaccine_expirydate', 'vaccine_batchnumber', ]


  
class OrderedServiceForm2(forms.ModelForm):
    class Meta:
        model = OrderedService
        fields = ['serv_ordered', 'serv_provider']


class UserRequestForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ['request_date','request_type', 'name', 'duration', 'rate']
        

        
class ConsultForm(forms.ModelForm):
    class Meta:    
        model = SentReport
        fields = ['service_date','presenting_complaints', 'general_findings', 'treatment_plan', 'next_appointment','name_staff',
                   ]




#SERVICE FORMS
class CartForm(forms.ModelForm):
    class Meta:
        model = OrderedService
        fields = ['promo_code','serv_provider', 'cost', 'serv_ordered']
#service provider, service,
# 

class ServiceListForm(forms.ModelForm):
    pro_logo = forms.FileField(label='service provider logo')
    class Meta:
        model = Provider
        fields = ['org_name', 'pro_logo', 'address', 'city', 'country',  ] 


class ServiceListForm1(forms.ModelForm):
    class Meta:
        model = HealthService
        fields = ['Service', 'details', 'cost', 'days_available','time_available', ] 

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = OrderedService
        fields = ['serv_provider',  'cost','serv_ordered', 'preferred_time', 'preferred_date', 'promo_code', 'order_date', ]



class RatingForm(forms.ModelForm):
    class Meta:
        model = ProviderRating
        fields = ['likes', 'dislikes', 'comments', ]

# class AmbulReportForm(forms.ModelForm):
#     class Meta:
#         model = AmbulReport






#DASHBOARD FORMS
class UserOrderForm(forms.ModelForm):
    class Meta:
        model = OrderedService
        fields = ['customer', 'serv_ordered', 'payment_status','cost','preferred_date','preferred_time','promo_code',
                  'order_date', ]                 

class QuoteRequestForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Requests.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))        
    request_type = forms.ModelChoiceField(queryset=Requests.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))        
    request_date = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class':"w3-input w3-border w3-round-large"}))
    
    class Meta:
        model = Requests
        fields = ['customer','request_type', 'request_date',
                   'name', 'duration', 'rate']
        



class SentReportForm(forms.ModelForm):
    CONSULTATION = 'CO'
    VACCINE = 'VA'
    MICROBIOLOGY = 'MI'
    OTHERS = 'OT'
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))        
    report_type = forms.ChoiceField(choices=((CONSULTATION,'Consultation'),
                           (VACCINE, 'Vaccine'),
                           (MICROBIOLOGY, 'Microbiology'),
                           (OTHERS,'Other Reports')), widget=forms.Select(attrs={'class':'form-control'}))
    ordered_service = forms.ModelChoiceField(queryset=OrderedService.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    service_date = forms.DateField(initial=datetime.date.today,  widget=forms.DateInput(attrs={'class':"w3-input w3-border w3-round-large"}))
    general_findings = forms.CharField(widget=forms.Textarea(attrs={'cols': 75, 'rows': 10}))
    vaccine_expirydate = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class':"w3-input w3-border w3-round-large"}))
    next_appointment = forms.DateField(initial=datetime.date.today,  widget=forms.DateInput(attrs={'class':"w3-input w3-border w3-round-large"}))
    file_upload = forms.FileField(label='Choose File', widget=forms.ClearableFileInput(attrs={'class':"w3-input w3-border w3-round-large"}))
    class Meta:
        model = SentReport
        fields = ['customer', 'report_type', 'ordered_service', 'service_date', 'service_time',  'presenting_complaints',
                  'general_findings', 'treatment_plan', 'vaccine_expirydate', 'vaccine_batchnumber', 'next_appointment','name_staff', 'file_upload',]
      
        widgets = {
            #'report_type': select(attrs={'class': "form-control"}),
           # 'service_date' : DateInput(attrs={'type': 'date'}),
            'service_time': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'presenting_complaints': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
           # 'exam_findings': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'treatment_plan': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            #'vaccine_expirydate': DateInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'vaccine_batchnumber': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            #'next_appointment': DateInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'name_staff': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            
        }


class MeasuredTestForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))       
    ordered_service = forms.ModelChoiceField(queryset=MeasuredTest.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    service_date = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class':"w3-input w3-border w3-round-large"}))
    
    class Meta:
        model = MeasuredTest
        fields = ['customer', 'ordered_service', 'service_date', 'service_test',
                  'value', 'lower_range', 'upper_range']
        widgets = {
                   'service_date': DateTimeWidget(attrs={'id':"service_date"}, usel10n = True, bootstrap_version=3)
}


class OrderedServiceForm(forms.ModelForm):
    class Meta:
        model = OrderedService
        fields = ['preferred_time', 'preferred_date', 'cost', 'promo_code',
         'payment_status', 'serv_ordered', 'customer']


class ServiceUpdateForm(forms.ModelForm):
    Category = forms.ModelChoiceField(queryset=ServiceGroup.objects.only('Categories'), widget=forms.Select(attrs={'class':'form-control'}))    
    sub_group = forms.ModelChoiceField(queryset=ServiceGroup.objects.only('Group'), widget=forms.Select(attrs={'class':'form-control'}))
    Service = forms.ModelChoiceField(queryset=ServiceGroup.objects.only('servicename'), widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = HealthService
        fields = ['Category','sub_group','Service', 'details', 'cost',
                  'cost_denom', 'days_available', 'time_available']

        widgets = {
            'Category': TextInput(attrs={'class': "form-control"}),
            'sub-group': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'Service': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'details': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'cost': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'cost_denom': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'days_available': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
            'time_available': TextInput(attrs={'class': "w3-input w3-border w3-round-large"}),
        }


        
class ProviderProfileForm(forms.ModelForm):
    #org_name = forms.ModelChoiceField(queryset=Provider.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))        
    class Meta:
        model = Provider
        fields = ['pro_logo', 'user', 'org_name', 'address',
                  'city', 'country', 'portal', 'phone_number']


class RequestsForm(forms.ModelForm):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))            
    class Meta:
        model = Requests
        fields = ['request_date','request_type', 'name', 'duration', 'rate']
