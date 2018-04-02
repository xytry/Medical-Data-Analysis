from django.conf.urls import url

from .views import (
    patients_listview,
    PatientsListView,
    PatientsDetailView,
    #patients_createview,
    PatientCreateView,
    PatientUpdateView
)

urlpatterns = [
    url(r'^create/$', PatientCreateView.as_view(), name='create'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', PatientUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', PatientUpdateView.as_view(), name='detail'),
    url(r'$', PatientsListView.as_view(), name='list'),
]
