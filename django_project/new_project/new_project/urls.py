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
from .views import UserLoginView
from users import views as user_views

urlpatterns = [

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^myhealthier/$', HealthierView.as_view(), name='myhealthier'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^login/$',user_views.login_view,name="login"),
    # url(r'^register/$',user_views.register_view,name="register"),
    # url(r'^logout/$',user_views.logout,name="logout"),
    url(r'^users/', include('users.urls', namespace='users')),

    # url (r'^login/', login_required(UserloginView.as_view(template_name="login.html"))),
    # (r'^logout/', login_required(ProviderView.as_view(template_name="index.html"))),
]  # Add Django site authentication urls (for login, logout, password management)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
