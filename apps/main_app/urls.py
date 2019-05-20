from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^fullreset$', views.fullreset),
    url(r'^reset$', views.reset),
    url(r'^process_money$', views.process),
    url(r'^$', views.index),
]