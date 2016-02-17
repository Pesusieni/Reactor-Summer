from django.conf.urls import patterns, include, url
from photo import views

urlpatterns = patterns('',
    url(r'^$', views.frontpage , name='views.frontpage'),

    url(r'^picture/(?P<picture_id>\d+)/$', views.picture, name='store.picture'),

)
