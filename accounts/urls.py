from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin



urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'accounts:login'}, name='logout'),
    
]

# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html