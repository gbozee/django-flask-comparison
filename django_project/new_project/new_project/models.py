# from django.db import models


# class User(models.Model):
#     """A customer interested in health services using Healthier"""
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     text = models.CharField(max_length=200)
#     email = models.EmailField(max_length=254)
#     password = models.CharField(max_length=200)
#     healthier_ID = models.ForeignKey(User)
#     phone_number = models.CharField(max_length=200)
#     date_birth = models.DateField(auto_now=False, auto_now_add=False, )
#     gender = models.BooleanField()

#     def __str__(self):
#         """Return a string representation of the model."""
#         return self.text


# class Provider(models.Model):
#     """Organization providing health services and sending reports to users"""
#     org_name = models.CharField(max_length=30)
#     pro_logo = models.ImageField(
#         upload_to=None, height_field=None, width_field=None, max_length=100, **options)
#     address = models.CharField(max_length=30)
#     city = models.CharField(max_length=200)
#     country = models.CharField(max_length=200)
#     email = models.EmailFieldEmail(max_length=254, **options)
#     password = models.CharField(max_length=200)
#     provider_ID = models.ForeignKey(User)
#     phone_number = models.CharField(max_length=200)
#     provider_ratings = models.CharField(max_length=200)

#     class Meta:
#         verbose_name_plural = 'entries'

#     def __str__(self):
#         """Return a string representation of the model."""
#         return self.text[:50] + "..."


# class Service(models.Model):
#     """services to be chosen by users"""
#     service_name = models.CharField(max_length=30)
#     sub_group = models.CharField(max_length=30)
#     details = models.CharField(max_length=200)
#     cost = models.CharField(max_length=200)
#     cost_denom = models.CharField(max_length=200)
#     service_ID = models.ForeignKey(User)
#     days_available = models.CharField(max_length=200)
#     time_available = models.CharField(max_length=200)

#     def __str__(self):
#         """Return a string representation of the model."""
#         return self.text


# class Ordered(models.Model):
#     """A paid for service request to the service organization"""
#     healthier_ID = models.ForeignKey(User)
#     service_ID = models.ForeignKey(User)
#     payment_status = models.CharField(max_length=30)
#     cost = models.CharField(max_length=30)
#     order_ID = models.ForeignKey(User)
#     preferred_date = models.CharField(max_length=200)
#     preferred_time = models.CharField(max_length=200)
#     promo_code = models.CharField(max_length=200)

#     def __str__(self):
#         """Return a string representation of the model."""
#         return self.text


