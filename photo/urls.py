from django.conf.urls import patterns, include, url
from photo import views

urlpatterns = patterns('',
    url(r'^$', views.index , name='photo.index'),
    url(r'^upload/$', views.upload , name='photo.upload'),
    url(r'^about/$', views.about , name='photo.about'),
    url(r'^picture/(?P<picture_id>\d+)/$', views.picture, name='picture'),

)
