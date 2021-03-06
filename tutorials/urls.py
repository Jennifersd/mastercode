from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^series/(?P<slug>[-\w]+)/$', views.tutorial_series_detail, name="tutorial_series_detail"),
    #url(regex=r'^series/(?P<slug>[-\w]+)/$', view=views.TutorialSeriesDetailView.as_view(), name="tutorial_series_detail"),
    #url(regex=r'^series/(?P<tutorial_series>[-\w]+)/(?P<slug>[-\w]+)/$', view=views.LessonDetailView.as_view(), name="lesson_detail"),
    
    #url(r'^series/$', views.TutorialSeriesListView.as_view(), name="tutorial_series_list_view"),
    url(regex=r'^series/(?P<slug>[-\w]+)/$', view=views.tutorial_series_detail, name="tutorial_series_detail"),
    url(regex=r'^series/(?P<tutorial_series>[-\w]+)/(?P<slug>[-\w]+)/$', view=views.lesson_detail, name="lesson_detail"),
    url(r'^series/$', views.tutorial_series_list, name="tutorial_series_list"),
    
]
