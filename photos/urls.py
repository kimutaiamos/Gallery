from django.conf.urls import url
from .views import welcome,gallery,search_results
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('',welcome,name='welcome'),
    url('',search_results, name = 'search_results'),
    url('',gallery, name='gallery') 
]


