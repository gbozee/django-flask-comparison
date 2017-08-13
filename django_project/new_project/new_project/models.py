from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Customer(models.Model):
    user= models.OneToOneField(User, related_name='user_profile')
    """A customer interested in health services using Healthier"""
    
    healthier_ID = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=200)
    date_birth = models.DateField(auto_now=False, auto_now_add=False, )
    gender = models.CharField(max_length=5, choices=(("","Select Gender"),('M',"Male"),("F","Female"),),blank=True)
    text =models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.user


class Provider(models.Model):
    """Organization providing health services and sending reports to users"""
    user = models.OneToOneField(User, related_name='provider_profile')
    org_name = models.CharField(max_length=30)
    pro_logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    provider_ID = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    

 

    def __str__(self):
        """Return a string representation of the model."""
        return self.org_name


class HealthService(models.Model):
    """services inputed by providers"""
    sub_group = models.ForeignKey("ServiceGroup")
    Category = models.CharField(max_length=200)            
    Service = models.CharField(max_length=200)    
    details = models.CharField(max_length=200)
    cost = models.CharField(max_length=20)
    cost_denom = models.CharField(max_length=50)
    service_ID = models.CharField(max_length=30)
    days_available = models.CharField(max_length=100)
    time_available = models.CharField(max_length=100)
    providers = models.ManyToManyField(Provider)

    def __str__(self):
        """Return a string representation of the model."""
        return self.Service


class OrderedService(models.Model):
    """A paid for service request to the service organization"""
    healthier_ID = models.ForeignKey("Customer")
    service_ID = models.CharField(max_length=30)
    payment_status = models.CharField(max_length=30, choices=(("","Payment Status"),('P',"Paid"),('NP',"Not Paid"),),blank=True)
    cost = models.CharField(max_length=30)
    order_ID = models.CharField(max_length=30)
    preferred_date = models.DateField(auto_now=False, auto_now_add=False, )
    preferred_time = models.CharField(max_length=200)
    promo_code = models.CharField(max_length=10)
    order_date = models.DateField(auto_now=False, auto_now_add=False, )
    # service = models.CharField(max_length=50)
    # serv_provider = models.CharField(max_length=50)
    

    def __str__(self):
        """Return a string representation of the model."""
        return self.healthier_ID



class MyHealth(models.Model):
    """A paid for service request to the service organization"""
    healthier_ID = models.ForeignKey("Customer")
    service_date = models.DateField(auto_now=False, auto_now_add=False, )
    health_data = models.CharField(max_length=200)
    data_value = models.CharField(max_length=200)


    def __str__(self):
        """Return a string representation of the model."""
        return self.service_date




class Requests(models.Model):
    """A paid for service request to the service organization"""
    healthier_ID = models.ForeignKey("Customer")
    request_date = models.DateField(auto_now=False, auto_now_add=False, )    
    request_type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    duration = models.CharField(max_length=30)
    rate = models.CharField(max_length=30)
   
    def __str__(self):
        """Return a string representation of the model."""
        return self.request_type


class AmbulReport(models.Model):
    """A paid for service request to the service organization"""
    order_ID = models.ForeignKey("OrderedService")
    healthier_ID = models.ForeignKey("Customer")
    service_ID = models.CharField(max_length=30)
    pickup_date = models.DateField(auto_now=False, auto_now_add=False, )
    pickup_address = models.CharField(max_length=30)
    pickup_city = models.CharField(max_length=30)
    destination_address = models.CharField(max_length=30)
    destination_city = models.CharField(max_length=200)
    destination_country = models.CharField(max_length=200)


    def __str__(self):
        """Return a string representation of the model."""
        return self.order_ID


class SentReport(models.Model):
    """A paid for service request to the service organization"""
    report_type = models.CharField(max_length=50)
    order_ID = models.ForeignKey("OrderedService")
    service_date = models.DateField(auto_now=False, auto_now_add=False, )
    service_time = models.CharField(max_length=30)
    name_staff = models.CharField(max_length=50)
    presenting_complaints = models.TextField(max_length=30)
    exam_findings = models.TextField(max_length=30)
    treatment_plan = models.TextField(max_length=30)
    vaccine_expirydate = models.DateField(auto_now=False, auto_now_add=False, )
    vaccine_batchnumber = models.CharField(max_length=200)
    next_appointment = models.DateField(auto_now=False, auto_now_add=False, )
    healthier_ID = models.ForeignKey("Customer")        


    def __str__(self):
        """Return a string representation of the model."""
        return self.report_type 



class ServiceGroup(models.Model):
    """Initial services for providers to use as template""" 
    Categories = models.CharField(max_length=50)
    Group = models.CharField(max_length=30)
    servicename = models.CharField(max_length=30)
 

    def __str__(self):
        """Return a string representation of the model."""
        return self.Categories 



class ProviderRating(models.Model):
    """Organization providing health services and sending reports to users"""
    healthier_ID = models.CharField(max_length=30)
    provider_ID = models.CharField(max_length=30)
    org_name = models.CharField(max_length=30)    
    provider_ratings = models.CharField(max_length=200)

 

    def __str__(self):
        """Return a string representation of the model."""
        return self.org_name		

class MeasuredTest(models.Model):
    """Db for measured tests including range"""
    healthier_ID = models.ForeignKey("Customer")
    order_ID = models.ForeignKey("OrderedService")
    service_date = models.DateField(auto_now=False, auto_now_add=False, )
    service_test = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    lower_range = models.CharField(max_length=30)
    upper_range = models.CharField(max_length=30)

 
    def __str__(self):
        """Return a string representation of the model."""
        return self.service_test
