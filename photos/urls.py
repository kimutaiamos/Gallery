from django.conf.urls import url
from django.urls.resolvers import URLPattern
from .import views

urlPattern=[
    url('^',views.welcome,name= 'welcome'),
]