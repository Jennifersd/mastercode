from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^series/(?P<slug>[-\w]+)/$', views.tutorial_series_detail, name="tutorial_series_detail"),
]
