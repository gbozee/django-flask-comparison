from __future__ import unicode_literals
from django.contrib.auth.backends import ModelBackend,UserModel
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

class EmailOrUsernameBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        user = UserModel.objects.filter(username=username).first()
        email = UserModel.objects.filter(email=username).first()
        if user or email:
            new_user = user or email
            if new_user.check_password(password):
                return new_user