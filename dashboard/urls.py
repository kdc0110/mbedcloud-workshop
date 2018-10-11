from django.conf.urls import include, url
from dashboard import views

urlpatterns = [
    url(r'$', views.index),
]