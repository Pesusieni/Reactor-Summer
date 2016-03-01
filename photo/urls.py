from django.conf.urls import patterns, include, url
from django.conf import settings
from photo import views
from django.conf.urls.static import static


urlpatterns =[
    url('^upload/$', views.upload , name='photo.upload'),
    url('^about/$', views.about , name='photo.about'),
    url('^picture/(?P<picture_id>\d+)/$', views.photo, name='photo.photo'),
    url('^search/$', views.search , name='photo.search'),
    url('^search/(?P<photo_tag>\w+)/?$', views.specific_search , name='photo.specific_search'),
    url('^$', views.index , name='photo.index'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
