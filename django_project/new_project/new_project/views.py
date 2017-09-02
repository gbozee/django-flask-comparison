from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView
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
from new_project.models import Provider
from new_project.models import ProviderRating
from new_project.models import OrderedService
from new_project.models import Requests
from new_project.models import ServiceGroup
from new_project.models import SentReport
from new_project.models import MyHealth
from new_project.models import MeasuredTest
from new_project.models import Customer
from .forms import SentReportForm
from .forms import MeasuredTestForm
from .forms import QuoteRequestForm
from .forms import CustomerForm
from .forms import MyHealthForm
from .forms import PersonalHealthForm
from .forms import UserRequestForm
from .forms import ProviderProfileForm

from .forms import UserReportForm
from django.views.generic.dates import MonthArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin
#import arrow






#MYHEALTH VIEWS
class HealthierView(TemplateView):
    template_name = "myhealthier.html"
    def post(self, request,*args, **kwargs):
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, " Registration Completed !!")            
        return render(request, "myhealthier", {})
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self,**kwargs):
        context = super(HealthierView, self).get_context_data(**kwargs)
        user = self.request.user
        context['profiles'] = Customer.objects.filter(user=user).first() # since a user should have only one profile,
        if 'form' not in context:
            context.update(form=CustomerForm())
        return context 


class TrendView(LoginRequiredMixin, TemplateView):
    template_name = "trend.html"
    def get_context_data(self, **kwargs):
        context = super(TrendView, self).get_context_data(**kwargs)
        form = MyHealthForm()
        context['services'] = MyHealth.objects.all()
        return context


class TrendView(TemplateView):
    template_name = 'trend.html'

    def get_context_data(self, **kwargs):
        context = super(TrendView, self).get_context_data(**kwargs)
        context['health_data'] = self.health_data()
        return context

    def health_data(self):
        final_data = []

        #date = arrow.now()
        # for day in xrange(1, 30):
        #     date = date.replace(days=-1)
        #     count = MyHealth.objects.filter(
        #         date_joined__gte=date.floor('day').datetime,
        #         date_joined__lte=date.ceil('day').datetime).count()
        #     final_data.append(count)

        return final_data


# class PersonalHealthView(LoginRequiredMixin, TemplateView):
#     template_name = "personal_health.html"
#     model = MyHealth

#     def post(self, request,*args, **kwargs):
#         form = MyHealthForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return render(request, "personal_health.html", {})
#         return self.render_to_response(self.get_context_data(form=form))

    
#     def get_context_data(self,**kwargs):
#         context = super(PersonalHealthView, self).get_context_data(**kwargs)
#         user = self.request.user
#         #context['profiles'] = Customer.objects.filter(user = self.request.user)
#         context['profiles'] = Customer.objects.all()
#         return context
    
        #request.user_report.set
class PersonalHealthView(TemplateView):
    template_name = "personal_health.html"
     
    def post(self, request,*args, **kwargs):
        form = MyHealthForm(request.POST, request.FILE)
        if form.is_valid():
            form.save()
        return redirect('personal_health')
        return self.render_to_response(self.get_context_data(form=form))

    

    # def get_context_data(self,**kwargs):
    #     context = super(PersonalHealthView, self).get_context_data(**kwargs)
    #     user = self.request.user
    #     context['profiles'] = Customer.objects.filter(user=user).first() # since a user should have only one profile,
    #     if 'form' not in context:
    #         context.update(form=MyHealthForm())
    #     return context   

    def get_context_data(self,**kwargs):
        context = super(PersonalHealthView, self).get_context_data(**kwargs)
        user = self.request.user
        context['profiles'] = MyHealth.objects.filter(customer=user).first() # since a user should have only one profile,
        if 'form' not in context:
            context.update(form=MyHealthForm())
        return context 

class RequestsView(TemplateView):
    template_name = "downloads_requests.html"
    def get_context_data(self, **kwargs):
        context = super(RequestsView, self).get_context_data(**kwargs)
        form = UserRequestForm()
        context['requests'] = Requests.objects.all()
        return context
    
    
    def my_views(request,id):
        my_object = Customer.objects.get(id=id)
        like_votes = my_object.customer_rating.filter(rate=1).count()
        dislike_votes = my_object.customer_rating.filter(rate=-1).count()



class TestReportView(TemplateView):
    template_name = "test_reports.html"
    model = OrderedService
    def get_context_data(self, **kwargs):
        context = super(TestReportView, self).get_context_data(**kwargs)
        context['reports'] = OrderedService.objects.all()
        return context
    
    
    def my_views(request,id):
        my_object = Customer.objects.get(id=id)
        like_votes = my_object.customer_rating.filter(rate=1).count()
        dislike_votes = my_object.customer_rating.filter(rate=-1).count()


class ConsultView(TemplateView):
    template_name = "consult.html"
    model = OrderedService
    def get_context_data(self, **kwargs):
        context = super(ConsultView, self).get_context_data(**kwargs)
        context['consults'] = OrderedService.objects.all()
        return context

    def my_views(request,id):
        my_object = Customer.objects.get(id=id)
        like_votes = my_object.customer_rating.filter(rate=1).count()
        dislike_votes = my_object.customer_rating.filter(rate=-1).count()

class ConsultMonthArchiveView(MonthArchiveView):
    queryset = SentReport.objects.all()
    date_field = "service_date"
    allow_future = True


#USER CREATION AND LOGIN
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
            customer_group = Group.objects.get(name="Customer")
            user.groups.add(customer_group)
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


@login_required
def logout_view(request):
    """Log the user out."""
    auth_logout(request)
    messages.info(request, "You have successfully logged out")
    return redirect('home')




class ProviderSignUpForm(UserCreationForm):
    org_name = forms.CharField()
    email = forms.EmailField()
  
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
            provider_group = Group.objects.get(name="Provider")
            prov.groups.add(provider_group)
        return prov

def provregister_view(request):
    """Register a new provider."""
  
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


# HOME AND CHOOSING SERVICE App
class HomeView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"

class CartView(LoginRequiredMixin, TemplateView):
    template_name = "cart.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CartView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context["servicost"] = OrderedService.objects.all()
        return context

    def post(self, request,*args, **kwargs):
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
        #      return HttpResponseRedirect(reverse('learning_logs:topics'))
        return redirect('index')
        context = {'form': form}
        return render(request, "cart.html", {})


class ProvregView(TemplateView):
    template_name = "proregister.html"

class ConsultView(TemplateView):
    template_name = "consult.html"

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
    #context_object_name = 'service_list'
    model = HealthService
    # queryset = HealthService.objects.filter(Service = '')
    #queryset = HealthService.objects.filter(service_name='#service chosen by user')
    #service_name is chosen by customer, servicelist can then be filtered with country, city, cost, customer rating
    def get_queryset(self):
        query = super().get_queryset()
        get_params = self.kwargs.get('service_name')
        # get_params = self.request.GET
        # if 'service_name' in get_params:
        #     value = get_params['service_name']
        if get_params:
            import pdb;
            return query.filter(Service=get_params)
        return query

    def get_context_data(self, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        context["services"] = HealthService.objects.all()
        
        return context
     
    def get_ratings(self, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        context["rating"] = ProviderRating.objects.all()
        
        return context
  

    # def get_context_data(self, **kwargs):
    #     context = super(ServiceListView, self).get_context_data(**kwargs)
    #     context["dislikes"] = ProviderRating.objects.filter(my_object__id=my_object.id, rate=-1).count()
    #     context["likes"] = ProviderRating.objects.filter(my_object__id=my_object.id, rate=1).count()
    #     return context 
    

    def saveserv(self, request,*args, **kwargs):
        model = OrderedService
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, " Service Ordered !!")
            return redirect('cart')
        return self.render_to_response(self.get_context_data(form=form))


class EmailOrUsernameBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        user = UserModel.objects.filter(username=username).first()
        email = UserModel.objects.filter(email=username).first()
        if user or email:
            new_user = user or email
            if new_user.check_password(password):
                return new_user




#Provider Dashboard Views
class DashboardView(TemplateView):
    template_name = "dashboard.html"
#search box code

class QuoteRequestView(TemplateView):
    template_name = "quote_request.html"
    def get_context_data(self, **kwargs):
        context = super(QuoteRequestView, self).get_context_data(**kwargs)
        context['qrequest'] = Requests.objects.all()
        context["form"]= QuoteRequestForm()
        return context
    

    def post(self, request,*args, **kwargs):
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, " Report Sent To User !!")                        
            return redirect('quote_request')
        return self.render_to_response(self.get_context_data(form=form))


class UserOrdersView(LoginRequiredMixin, ListView):
    template_name = "user_orders.html"
    model=OrderedService
    def get_context_data(self, **kwargs):
        context = super(UserOrdersView, self).get_context_data(**kwargs)
        context["orders"] = OrderedService.objects.all()
        return context



#@login_required
class ServiceUpdateView(LoginRequiredMixin, TemplateView):
    template_name = "service_update.html"
    def get_context_data(self, **kwargs):
        context = super(ServiceUpdateView, self).get_context_data(**kwargs)
        context['services'] = HealthService.objects.all()
        if 'form' not in context:
            context["form"]= ServiceUpdateForm()
        #context = {'form': form}
        return context
      

    def post(self, request,*args, **kwargs):
        form = ServiceUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, " Service Registered !!")
            return redirect('service_update')
        return self.render_to_response(self.get_context_data(form=form))


class ServiceDelete(DeleteView):
    model = HealthService
    success_url = reverse_lazy('registered_service.html')     
      



class SendReportView(LoginRequiredMixin, TemplateView):
    template_name = "send_report.html"

    def get_context_data(self, **kwargs):
        context = super(SendReportView, self).get_context_data(**kwargs)
        context['services'] = SentReport.objects.all()
        context["form"]= SentReportForm()
        return context


    def post(self, request,*args, **kwargs):
        form = SentReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, " Report Sent To User !!")            
            return redirect('send_report')
        return self.render_to_response(self.get_context_data(form=form))



class MeasuredTestView(LoginRequiredMixin, TemplateView):
    template_name = "mtest_report.html"

    def get_context_data(self, **kwargs):
        context = super(MeasuredTestView, self).get_context_data(**kwargs)
        context['qrequest'] = MeasuredTest.objects.all()
        context["form"]= MeasuredTestForm()
        return context

    def post(self, request,*args, **kwargs):
        form = MeasuredTestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, " Report Sent To User !!")                        
            return redirect('mtest_report')
        return self.render_to_response(self.get_context_data(form=form))



class RegisteredServiceView(TemplateView):
    template_name = "registered_service.html"  



class ProviderProfileView(TemplateView):
    template_name = "provider_profile.html"
    model=Provider
    def get_context_data(self,**kwargs):
            context = super(ProviderProfileView, self).get_context_data(**kwargs)
            user = self.request.user
            context['profiles'] = Provider.objects.filter(user=user).first() # since a user should have only one profile,
            # if 'form' not in context:
            #     context.update(form=ProviderProfileForm())
            return context   


    # def get_context_data(self, **kwargs):
    #     context = super(ServiceListView, self).get_context_data(**kwargs)
    #     context["services"] = Provider.objects.all()
        
    #     return context
    # template_name = "provider_profile.html"
    # model = Provider
    # fields = ['user', 'org_name', 'pro_logo', 'address','city', 'country', 'provider_ID', 'phone_number']
    # template_name_suffix = 'ProviderProfileForm'  

    # def get(self, request, **kwargs):
    #     self.object = Provider.objects.get(id=self.kwargs['id'])
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     context = self.get_context_data(object=self.object, form=form)
    #     return self.render_to_response(context)

    # def get_object(self, queryset=None):
    #     obj = Provider.objects.get(id=self.kwargs['provider_profile'])
    #     return obj
              

    # def get_object(self, queryset=None): 
    #     return self.request.us

    # def form_valid(self, form):
    #         #save cleaned post data
    #     clean = form.cleaned_data 
    #     context = {}        
    #     self.object = context.save(clean) 
    #     return super(UserUpdate, self).form_valid(form)


