"""new_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .views import HealthierView
from .views import DashboardView
from .views import HomeView
from users import views as user_views
from .import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^myhealthier/$', HealthierView.as_view(), name='myhealthier'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^login/$',views.login_view,name="login"),
    url(r'^prologin/$',views.prologin_view,name="prologin"),
    # url(r'^register/$',user_views.register_view,name="register"),
    url(r'^logout/$',views.logout_view,name="logout"),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^trend/$', views.TrendView.as_view(), name='trend'),
    url(r'^requests/$', views.RequestsView.as_view(), name='requests'),
    url(r'^reports/$', views.ReportView.as_view(), name='reports'),
    url(r'^consult/$', views.ConsultView.as_view(), name='consult'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^cart/$', views.CartView.as_view(), name='cart'),
    url(r'^vaccines/$', views.VaccineView.as_view(), name='vaccines'),
    url(r'^cancer_screen/$', views.CancerScreenView.as_view(), name='cancer_screen'),
    url(r'^service_list/$', views.ServiceListView.as_view(), name='service_list'),
    url(r'^service_list/(?P<service_name>[\w-]+)/$', views.ServiceListView.as_view(), name='s_list_name'),
    url(r'^clinics/$', views.ClinicsView.as_view(), name='clinics'),
    url(r'^diagnostics/$', views.DiagnosticsView.as_view(), name='diagnostics'),
    url(r'^health_checks/$', views.HealthChecksView.as_view(), name='health_checks'),
    url(r'^procedures/$', views.ProceduresView.as_view(), name='procedures'),
    url(r'^drugs/$', views.DrugsView.as_view(), name='drugs'),
    url(r'^ambulance/$', views.AmbulanceView.as_view(), name='ambulance'),
    url(r'^service_update/$', views.ServiceUpdateView.as_view(), name='service_update'),
    url(r'^registered_service/$', views.RegisteredServiceView.as_view(), name='registered_service'),
    url(r'^send_report/$', views.SendReportView.as_view(), name='send_report'),
    url(r'^mtest_report/$', views.MeasuredTestView.as_view(), name='mtest_report'),    
    url(r'^provider_profile/$', views.ProviderProfileView.as_view(), name='provider_profile'),
    url(r'^quote_request/$', views.QuoteRequestView.as_view(), name='quote_request'),
    url(r'^user_orders/$', views.UserOrdersView.as_view(), name='user_orders'),
    url (r'^proregister/$', views.provregister_view, name='proregister'),
    url (r'^register/$', views.register_view, name='register'),
    url(r'^password_reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #url('^', include('django.contrib.auth.urls')),
     # url(r'^proregister/$', views.ProvregView.as_view(), name='prore
    # url (r'^login/', login_required(UserloginView.as_view(template_name="login.html"))),
    # (r'^logout/', login_required(ProviderView.as_view(template_name="index.html"))),
]  # Add Django site authentication urls (for login, logout, password management)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
