from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^employee/$', views.EmployeeApi.as_view()),
    url(r'^employee/(?P<pk>[0-9]+)/$', views.EmployeeApi.as_view())
]
