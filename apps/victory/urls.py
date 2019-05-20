from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^conditions$', views.conditions),
    url(r'^victory$', views.index),
]