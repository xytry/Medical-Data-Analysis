"""muypicky URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView, LogoutView

from profiles.views import RegisterView, activate_user_view

from patients.views import HomeView
from patients.views import (
    patients_listview,
    PatientsListView,
    PatientsDetailView,
    #patients_createview,
    PatientCreateView
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^register/$', RegisterView.as_view(),name='register'),
    url(r'^activate/(?P<code>[a-z0-0].*)/s', activate_user_view, name='activate'),
    url(r'^login/$', LoginView.as_view(),name='login'),
    url(r'^logout/$', LogoutView.as_view(),name='logout'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^patients/', include('patients.urls', namespace='patients')),
    url(r'^u/', include('profiles.urls', namespace='profiles')),
    url(r'^items/', include('diseases.urls', namespace='diseases')),
    #url(r'^patients/$', patients_listview),
    #url(r'^patients/$', PatientsListView.as_view(), name='patients'),
    #url(r'^patients/create/$', patients_createview),
    #url(r'^patients/create/$', PatientCreateView.as_view(), name='patients-create'),
    #url(r'^patients/(?P<slug>\w+)/$', PatientsListView.as_view()),
    #url(r'^patients/(?P<slug>[\w-]+)/$', PatientsDetailView.as_view(), name='patients-detail'),
    #url(r'^patients/(?P<patient_id>\w+)/$', PatientsDetailView.as_view()),
    url(r'^about/$',TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$',TemplateView.as_view(template_name='contact.html'), name='contact'),
]
