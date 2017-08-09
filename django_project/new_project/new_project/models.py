from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
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


class ProviderProfile(models.Model):
    """Organization providing health services and sending reports to users"""
    user = models.OneToOneField(User, related_name='provider_profile')
    org_name = models.CharField(max_length=30)
    pro_logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    provider_ID = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=200)
   # provider_ratings = models.CharField(max_length=200)

 

    def __str__(self):
        """Return a string representation of the model."""
        return self.org_name


class HealthService(models.Model):
    """services inputed by providers"""
    service_name = models.CharField(max_length=30)
    sub_group = models.CharField(max_length=30)
    details = models.CharField(max_length=200)
    cost = models.CharField(max_length=20)
    cost_denom = models.CharField(max_length=50)
    service_ID = models.CharField(max_length=30)
    days_available = models.CharField(max_length=100)
    time_available = models.CharField(max_length=100)
    providers = models.ManyToManyField(ProviderProfile)
    def __str__(self):
        """Return a string representation of the model."""
        return self.service_name


class OrderedService(models.Model):
    """A paid for service request to the service organization"""
    healthier_ID = models.CharField(max_length=30)
    service_ID = models.CharField(max_length=30)
    payment_status = models.CharField(max_length=30, choices=(("","Payment Status"),('P',"Paid"),('NP',"Not Paid"),),blank=True)
    cost = models.CharField(max_length=30)
    order_ID = models.CharField(max_length=30)
    preferred_date = models.CharField(max_length=200)
    preferred_time = models.CharField(max_length=200)
    promo_code = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.healthier_ID



class MyHealth(models.Model):
    """A paid for service request to the service organization"""
    healthier_ID = models.CharField(max_length=30)
    service_date = models.CharField(max_length=200)
    health_data = models.CharField(max_length=200)
    data_value = models.CharField(max_length=200)


    def __str__(self):
        """Return a string representation of the model."""
        return self.service_date




class TestReport(models.Model):
    """A paid for service request to the service organization"""
    report_type = models.CharField(max_length=30)
    order_ID = models.CharField(max_length=30)
    service_date = models.CharField(max_length=200)
    service_time = models.CharField(max_length=200)
    attending_staff = models.CharField(max_length=200)
    presenting_complaints = models.CharField(max_length=30)
    exam_findings = models.CharField(max_length=30)
    treatment_plan = models.CharField(max_length=30)
    vaccine_expiry = models.CharField(max_length=30)
    vaccine_batch = models.CharField(max_length=30)
    next_appointment = models.CharField(max_length=30)

    def __str__(self):
        """Return a string representation of the model."""
        return self.report_type


class AmbulReport(models.Model):
    """A paid for service request to the service organization"""
    order_ID = models.CharField(max_length=30)
    healthier_ID = models.CharField(max_length=30)
    service_ID = models.CharField(max_length=30)
    pickup_date = models.CharField(max_length=30)
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
    order_ID = models.CharField(max_length=30)
    service_date = models.CharField(max_length=30)
    service_time = models.CharField(max_length=30)
    name_staff = models.CharField(max_length=50)
    presenting_complaints = models.TextField(max_length=30)
    exam_report = models.TextField(max_length=30)
    treatment_plan = models.TextField(max_length=30)
    vaccine_expirydate = models.CharField(max_length=200)
    vaccine_batchnumber = models.CharField(max_length=200)
    next_appointment = models.CharField(max_length=30)


    def __str__(self):
        """Return a string representation of the model."""
        return self.report_type 



class ServiceGroup(models.Model):
    """Initial services for providers to use as template"""
    Category = models.CharField(max_length=50)
    Group = models.CharField(max_length=30)
    servicename = models.CharField(max_length=30)
 

    def __str__(self):
        """Return a string representation of the model."""
        return self.service_group 



class ProviderRating(models.Model):
    """Organization providing health services and sending reports to users"""
    healthier_ID = models.CharField(max_length=30)
    provider_ID = models.CharField(max_length=30)
    org_name = models.CharField(max_length=30)    
    provider_ratings = models.CharField(max_length=200)

 

    def __str__(self):
        """Return a string representation of the model."""
        return self.org_name		