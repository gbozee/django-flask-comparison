from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# from .models import Service

class HealthierView(TemplateView):
    template_name = "myhealthier.html"

class DashboardView(TemplateView):
    template_name = "dashboard.html"

class HomeView(TemplateView):
    template_name = "index.html"



# class ServiceCreate(CreateView):
#     model = Service
#     fields = ['name']

# class ServiceUpdate(UpdateView):
#     model = Service
#     fields = ['name']

# class ServiceDelete(DeleteView):
#     model = Service
#     success_url = reverse_lazy('author-list')

class UserLoginView(FormView):
    #form_class = LoginForm
    template_name = "login.html"

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('login')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

class LogoutView(FormView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)





