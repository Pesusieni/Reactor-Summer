from django.conf.urls import patterns, include, url
from django.conf import settings
from photo import views
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^$', views.index , name='photo.index'),
    url(r'^upload/$', views.upload , name='photo.upload'),
    url(r'^about/$', views.about , name='photo.about'),
    url(r'^picture/(?P<picture_id>\d+)/$', views.photo, name='photo.photo'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
