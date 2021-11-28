from django.conf.urls import url
from .views import welcome,gallery,search_results
from django.conf import settings


urlpatterns=[
    url('',welcome,name='welcome'),
    # url('search/',search_results, name = 'search_results')
]
