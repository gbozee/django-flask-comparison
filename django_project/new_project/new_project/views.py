from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .backends import EmailOrUsernameBackend
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.backends import ModelBackend,UserModel
from .forms import ServiceUpdateForm
from .forms import SentReportForm
from .forms import RequestsForm
from django.views.generic.list import ListView
from new_project.models import HealthService
from new_project.models import ProviderProfile
from new_project.models import ProviderRating
from new_project.models import OrderedService
from new_project.models import Requests
from new_project.models import ServiceGroup



class HealthierView(TemplateView):
    template_name = "myhealthier.html"
    def post(self, request,*args, **kwargs):
        form = HealthierForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return render(request, "myhealthier.html", {})


class DashboardView(TemplateView):
    template_name = "dashboard.html"
#search box code

class HomeView(TemplateView):
    template_name = "index.html"

class TrendView(TemplateView):
    template_name = "trend.html"


class RequestsView(TemplateView):
    template_name = "downloads_requests.html"
    def get_context_data(self, **kwargs):
        context = super(RequestsView, self).get_context_data(**kwargs)
        form = RequestsForm()
        context['services'] = Requests.objects.all()
        return context

class ReportView(TemplateView):
    template_name = "test_reports.html"



class AboutView(TemplateView):
    template_name = "about.html"

class CartView(TemplateView):
    template_name = "cart.html"
    def post(self, request,*args, **kwargs):
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
        #      return HttpResponseRedirect(reverse('learning_logs:topics'))
        context = {'form': form}
        return render(request, "cart.html", {})


class ProvregView(TemplateView):
    template_name = "proregister.html"



class ConsultView(TemplateView):
    template_name = "consult.html"

# class ServiceCreate(CreateView):
#     model = Service
#     fields = ['name']

# class ServiceUpdate(UpdateView):
#     model = Service
#     fields = ['name']

# class ServiceDelete(DeleteView):
#     model = Service
#     success_url = reverse_lazy('author-list')

# class UserLoginView(FormView):
#     #form_class = LoginForm
#     template_name = "login.html"

#     def post(self, request):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             if user.is_active:
#                 login(request, user)

#                 return HttpResponseRedirect('login')
#             else:
#                 return HttpResponse("Inactive user.")
#         else:
#             return HttpResponseRedirect(settings.LOGIN_URL)

#         return render(request, "index.html")

# class LogoutView(FormView):
#     def get(self, request):
#         logout(request)
#         return HttpResponseRedirect(settings.LOGIN_URL)



class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('myhealthier')
    return render(request,'login.html',{'login_form':form})


class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    # date_of_birth = forms.DateInput()
    # phone_number = forms.CharField()
    # gender = forms.CharField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email already exists")
            return email

    #
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = user.email
        if commit:
            user.save()
        return user

def register_view(request):
    """Register a new user."""
    # if request.method != 'POST':
    #     # Display blank registration form.
    form = UserSignUpForm()
    if request.method == 'POST':
        form = UserSignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('home')
    return render(request,'register.html',{'reg_form':form})
    messages.info(request, "Account successfully created")

    # else:
    #     # Process completed form.
    #     form = UserCreationForm(data=request.POST)
    #     if form.is_valid():
    #         new_user = form.save()
    #         # Log the user in and then redirect to home page.
    #         authenticated_user = authenticate(username=new_user.username,
    #             password=request.POST['password1'])
    #         login(request, authenticated_user)
    #         return HttpResponseRedirect(reverse('users:index'))

@login_required
def logout_view(request):
    """Log the user out."""
    auth_logout(request)
    messages.info(request, "You have successfully logged out")
    return redirect('home')




class ProviderSignUpForm(UserCreationForm):
    org_name = forms.CharField()
    email = forms.EmailField()
    # date_of_birth = forms.DateInput()
    # phone_number = forms.CharField()
    # gender = forms.CharField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email already exists")
            return email

    #
    def save(self, commit=True):
        prov = super().save(commit=False)
        prov.first_name = self.cleaned_data['org_name']
        prov.email = self.cleaned_data['email']
        prov.username = user.email
        if commit:
            prov.save()
        return prov

def provregister_view(request):
    """Register a new provider."""
    # if request.method != 'POST':
    #     # Display blank registration form.
    form = ProviderSignUpForm()
    if request.method == 'POST':
        form = ProviderSignUpForm(data=request.POST)
        if form.is_valid():
            prov = form.save()
            # auth_login(request,user, EmailOrUsernameBackend())
            return redirect('dashboard')
       
    return render(request,'proregister.html',{'provreg_form':form})
    messages.info(request, "Account successfully created")



def prologin_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('dashboard')
    return render(request,'prologin.html',{'prologin_form':form})



class PasswordResetView(FormView):
    template_name = "registration/password_reset_form.html"
    success_url = '/new_project/login'
    form_class = PasswordResetForm

        #     @staticmethod
        # def validate_email_address(email):
        # '''
        # This method here validates the if the input is an email address or not. Its return type is boolean, True if the input is a email address or False if its not.
        # '''
        #     try:
        #         validate_email(email)
        #         return True
        #     except ValidationError:
        #         return False

        # def post(self, request, *args, **kwargs):
        # '''
        # A normal post request which takes input from field "email_or_username" (in ResetPasswordRequestForm).
        # '''
        #     form = self.form_class(request.POST)
        #     if form.is_valid():
        #         data= form.cleaned_data["email_or_username"]
        #     if self.validate_email_address(data) is True:                 #uses the method written above
        #         '''
        #         If the input is an valid email address, then the following code will lookup for users associated with that email address. If found then an email will besent to the address, else an error message will be printed on the screen.
        #         '''
        #         associated_users= User.objects.filter(Q(email=data)|Q(username=data))
        #         if associated_users.exists():
        #             for user in associated_users:
        #                     c = {
        #                         'email': user.email,
        #                         'domain': request.META['HTTP_HOST'],
        #                         'site_name': 'your site',
        #                         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #                         'user': user,
        #                         'token': default_token_generator.make_token(user),
        #                         'protocol': 'http',
        #                         }
        #                     subject_template_name='registration/password_reset_subject.txt'
        #                     # copied from django/contrib/admin/templates/registration/password_reset_subject.txt to templates directory
        #                     email_template_name='registration/password_reset_email.html'
        #                     # copied from django/contrib/admin/templates/registration/password_reset_email.html to templates directory
        #                     subject = loader.render_to_string(subject_template_name, c)
        #                     # Email subject *must not* contain newlines
        #                     subject = ''.join(subject.splitlines())
        #                     email = loader.render_to_string(email_template_name, c)
        #                     send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
        #             result = self.form_valid(form)
        #             messages.success(request, 'An email has been sent to ' + data +". Please check its inbox to continue reseting password.")
        #             return result
        #         result = self.form_invalid(form)
        #         messages.error(request, 'No user is associated with this email address')
        #         return result
        #     else:
        #         '''
        #         If the input is an username, then the following code will lookup for users associated with that user. If found then an email will be sent to the user's address, else an error message will be printed on the screen.
        #         '''
        #         associated_users= User.objects.filter(username=data)
        #         if associated_users.exists():
        #             for user in associated_users:
        #                 c = {
        #                     'email': user.email,
        #                     'domain': 'example.com', #or your domain
        #                     'site_name': 'example',
        #                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #                     'user': user,
        #                     'token': default_token_generator.make_token(user),
        #                     'protocol': 'http',
        #                     }
        #                 subject_template_name='registration/password_reset_subject.txt'
        #                 email_template_name='registration/password_reset_email.html'
        #                 subject = loader.render_to_string(subject_template_name, c)
        #                 # Email subject *must not* contain newlines
        #                 subject = ''.join(subject.splitlines())
        #                 email = loader.render_to_string(email_template_name, c)
        #                 send_mail(subject, email, DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
        #             result = self.form_valid(form)
        #             messages.success(request, 'Email has been sent to ' + data +"'s email address. Please check its inbox to continue reseting password.")
        #             return result
        #         result = self.form_invalid(form)
        #         messages.error(request, 'This username does not exist in the system.')
        #         return result
        #     messages.error(request, 'Invalid Input')
        #     return self.form_invalid(form)

class PasswordResetDoneView(FormView):
    template_name = "registration/password_reset_done.html"


class PasswordResetConfirmView(FormView):
    template_name = "registration/password_reset_confirm.html"
    form_class = SetPasswordForm
    success_url = '/login/'

    def post(self, request, uidb64=None, token=None, *arg, **kwargs):
        """
        View that checks the hash in a password reset link and presents a
        form for entering a new password.
        """
        UserModel = get_user_model()
        form = self.form_class(request.POST)
        assert uidb64 is not None and token is not None  # checked by URLconf
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            if form.is_valid():
                new_password= form.cleaned_data['new_password2']
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password has been reset.')
                return self.form_valid(form)
            else:
                messages.error(request, 'Password reset has not been unsuccessful.')
                return self.form_invalid(form)
        else:
            messages.error(request,'The reset password link is no longer valid.')
            return self.form_invalid(form)

class PasswordResetCompleteView(FormView):
     template_name = "registration/password_reset_complete.html"



class ServiceUpdateView(TemplateView):
    template_name = "service_update.html"
    def get_context_data(self, **kwargs):
        context = super(ServiceUpdateView, self).get_context_data(**kwargs)
        context['services'] = HealthService.objects.all()
        context["form"]= ServiceUpdateForm()
        return context
        #  #Category, Group and service_name from ServiceGrouping Model         
        # form = ServiceUpdateForm()
        # context['services'] = HealthService.objects.all()
        
        # return context
        # # servicer= ServiceGroup.objects.all()
        # # servicer = ServiceGroup.objects.all().order_by('Group')
        # # return render(request, 'service_update.html', {'servicer': servicer})


    def post(self, request,*args, **kwargs):
          form = ServiceUpdateForm(request.POST)
          if form.is_valid():
            form.save()
          return render(request,"service_update.html", {})


class ServiceDelete(DeleteView):
    model = HealthService
    success_url = reverse_lazy('registered_service.html')     
      
    # def get_context_data(self, **kwargs):
    #      context = super(ServiceUpdateView, self).get_context_data(**kwargs)
    #      context['modelone'] = HealthService.objects.get(*query logic*)
    #      context['modeltwo'] = ServiceGrouping.objects.get(*query logic*)
    #      return context



class SendReportView(TemplateView):
    template_name = "send_report.html"
    def post(self, request,*args, **kwargs):
        form = SentReportForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return render(request, "send_report.html", {})

class MeasuredTestView(TemplateView):
    template_name = "mtest_report.html"
    def post(self, request,*args, **kwargs):
        form = MeasuredTestForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return render(request, "mtest_report.html", {})


class RegisteredServiceView(TemplateView):
    template_name = "registered_service.html"


class ProviderProfileView(TemplateView):
    template_name = "provider_profile.html"
    def post(self, request,*args, **kwargs):
        form = ProviderProfileForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return render(request, "provider_profile.html", {})

class QuoteRequestView(TemplateView):
    template_name = "quote_request.html"
    def post(self, request,*args, **kwargs):
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return render(request, "quote_requests.html", {})


class UserOrdersView(TemplateView):
    template_name = "user_orders.html"
    def post(self, request,*args, **kwargs):
        form = ServiceUpdateForm(request.POST)
        if form.is_valid():
            form.save()
        #      return HttpResponseRedirect(reverse('learning_logs:topics'))
        context = {'form': form}
        return render(request, "user_orders.html", {})

class VaccineView(TemplateView):
    template_name = "vaccines.html"


class CancerScreenView(TemplateView):
    template_name = "cancer_screen.html"


class ClinicsView(TemplateView):
    template_name = "clinics.html"


class DiagnosticsView(TemplateView):
    template_name = "diagnostics.html"


class DrugsView(TemplateView):
    template_name = "drugs.html"


class ProceduresView(TemplateView):
    template_name = "procedures.html"


class AmbulanceView(TemplateView):
    template_name = "ambulance.html"

class HealthChecksView(TemplateView):
    template_name = "health_checks.html"

class ServiceListView(ListView):
    template_name = "service_list.html"
    context_object_name = 'service_list'
    model=HealthService
    # model=ProviderProfile
    # model=ProviderRating
     # model=OrederedService
    queryset = HealthService.objects.all()
    #queryset = HealthService.objects.filter(service_name='#service chosen by user')
    #service_name is chosen by customer, servicelist can then be filtered with country, city, cost, customer rating
    def get_context_data(self, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
         #service details,days ,time available, cost for HealthService Model         
        context["provider"] = ProviderProfile.objects.all()
         #Organization, Logo, Address, City, Country,          
        context["rating"] = ProviderRating.objects.all()
        #Rating from ProviderRating Model

        return context
    
    def make_appointment(request):
        if request.method == 'POST':
           form = AppointmentForm(request.POST)
           if form.is_valid():
             preferred_time = form.cleaned_data['time']
             preferred_date = form.cleaned_data['date']
             appointment = OrderedService.objects.create(
                            preffered_time = time,
                            preffered_date = date,)
             return render(request,'service_list.html',{'AppointmentForm':form})




class EmailOrUsernameBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        user = UserModel.objects.filter(username=username).first()
        email = UserModel.objects.filter(email=username).first()
        if user or email:
            new_user = user or email
            if new_user.check_password(password):
                return new_user




