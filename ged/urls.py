from django.conf.urls import patterns, url

from ged import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
